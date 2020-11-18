from django.shortcuts import redirect, render
from django.http import request
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import logout

from .forms import SignUpForm

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        print(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            
            return render(request, 'registration/login.html')
        
        else:
            context = {
                'form': form
            }
            return render(request, 'users/signup.html', context)

    template = 'users/signup.html'
    context = {
            'form': SignUpForm
            }
    return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect('home.html')

