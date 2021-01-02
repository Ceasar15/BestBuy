from django.db import models
import random
import os
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.forms import widgets


from .utils import unique_slug_generator

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,4739628451)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)
    
    def search(self, query):
        lookups = (Q(title__icontains=query) | 
                  Q(description__icontains=query) |
                  Q(price__icontains=query))
        return self.filter(lookups).distinct()


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Product.objects.featured() 
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)
    

Laptops= 'Laptops'
Tablets = 'Tablets'
Phones = 'Phones'

HP = 'HP'
Dell = 'Dell'
Lenovo = 'Lenovo'
Acer = 'Acer'
Apple = 'Apple'
Samsung = 'Samsung'
Microsoft = 'Microsoft'
Sony = 'Sony'
Techno = 'Techno'
Infinix = 'Infinix' 

class Product(models.Model):
    # Category Choices
    CATEGORY = (
        (Laptops, 'Laptops'),
        (Tablets, 'Tablets'),
        (Phones, 'Phones'),
    )

    MANUFACTURER = (
        (HP, 'HP'),
        (Acer, 'Acer'),
        (Dell, 'Dell'),
        (Sony, 'Sony'),
        (Apple, 'Apple'),
        (Lenovo, 'Lenovo'),
        (Techno, 'Techno'),        
        (Infinix, 'Infinix'), 
        (Samsung, 'Samsung'),
        (Microsoft, 'Microsoft'),

    )

    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    operating_system = models.CharField(max_length=100, null=True)
    processor       = models.CharField(max_length=150, null=True)
    graphics        = models.CharField(max_length=150, null=True)
    memory          = models.CharField(max_length=150, null=True)
    hard_drive      = models.CharField(max_length=150, null=True)
    power_supply    = models.CharField(max_length=150, null=True)
    battery         = models.CharField(max_length=150, null=True)
    category        = models.CharField(max_length=150, choices=CATEGORY , default= Laptops)
    manufacturer    = models.CharField(max_length=150, choices=MANUFACTURER, default= Apple )
    updated_on      = models.DateField(auto_now_add=True, null=True)
    created_on      = models.DateField(auto_now_add=True, null=True)

    objects = ProductManager()

    # class Meta:
    #     app_label = 'apps.products'

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return "{id}/{slug}/".format(id=self.id,slug=self.slug)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title



def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
