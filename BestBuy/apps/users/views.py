from django.shortcuts import redirect, render
from django.http import request
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .forms import CustomUserCreationForm

# Create your views here.




class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

# def sign_up(request):
#     if request.method == 'POST':
#         print(request.POST)
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.save()
            
#             return render(request, 'registration/login.html')
        
#         else:
#             context = {
#                 'form': form
#             }
#             return render(request, 'users/signup.html', context)

#     template = 'users/signup.html'
#     context = {
#             'form': SignUpForm
#             }
#     return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect('home.html')

