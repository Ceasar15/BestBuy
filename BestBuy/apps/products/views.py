from django.db.models import Count
from django.http import request, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


from taggit.models import Tag

from .models import Product
from apps.cart.forms import CartAddProductForm

# Create your views here.


def home(request):
    template = 'home.html'
    cart_product_form = CartAddProductForm()
    queryset = Product.objects.all().order_by('-created_on').active()

    context = {
        'object_list': queryset,
        'cart_product_form': cart_product_form,
    }
    return render(request, template, context)


def contact(request):
    template = 'contact.html'
    return render(request, template)

def faq(request):
    template = 'faq.html'
    return render(request, template)

class CatalogView(TemplateView):
    template_name = 'products/catalog.html'

class GalleryView(TemplateView):
    template_name = 'products/gallery.html'


class ProductFeaturedListView(ListView):
    template_name = 'products/gallery.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()



class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"


def product_list_view(request, tag_slug=None):
    queryset = Product.objects.all().order_by('-created_on').distinct()
    cart_product_form = CartAddProductForm()
    tagv = [] 
    for all_tags in queryset:
        for each_tag in all_tags.tags.order_by('name').distinct():
            tagv.append(each_tag)
    
    from collections import Counter
    uniq =  Counter(tagv)
    seacc = queryset.search('Laptops')
    print(seacc)
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        queryset = queryset.filter(tags__name__in=[tag]).distinct()

    paginator = Paginator(queryset, 9)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    

    
    context = {
        'object_list': queryset,
        'cart_product_form': cart_product_form,
        'tag': tag,
        'page': page,
        'uniq': uniq
    }
    return render(request, "products/list.html", context)


def recom_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/recommendation.html", context)



class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"
    cart_product_form = CartAddProductForm()

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance


def product_detail_view(request, slug, *args, **kwargs):
    queryset = Product.objects.all()
    cart_product_form = CartAddProductForm()
    instance = get_object_or_404(Product, slug=slug, active=True)
    if instance is None:
        raise Http404("Product doesn't exist")
    similar_products = instance.tags.similar_objects()[:2]
    
    context = {
        'object': instance,
        'object_list': queryset,
        'cart_product_form': cart_product_form,
        'similar_products': similar_products,
        
    }
    return render(request, "products/detail.html", context)

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''



