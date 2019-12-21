import urllib, hashlib

from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from django_gravatar.forms import LoginForm


def LoginView(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Kullanıcı Adı veya Şifre Hatalı.')
            return render(request, 'django_gravatar/login.html', context)
        login(request, user)
        return redirect('django_gravatar:homepage')
    return render(request, 'login.html', context)


def mailMD5(email):
    return hashlib.md5(email.strip().lower().encode("utf-8")).hexdigest()

def get_gravatar_url(email,size):
    default = "mp" # default photo image url (.jpg or .png) or Gravatar defaults= mp, identicon, monsterid, wavatar, retro, robohash, blank 
    return "https://www.gravatar.com/avatar/" + mailMD5(email) + "?s="+ str(size) +"&d="+ default


@login_required
def IndexView(request):
    gravatar_url = get_gravatar_url(request.user.email,200) 
    
    context={
        "gravatar_url": gravatar_url
    }
    return render(request,'index.html',context)