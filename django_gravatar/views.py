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


@login_required
def IndexView(request):
    size = 500
    gravatar_mail = mailMD5(request.user.email) 
    gravatar_url = "https://www.gravatar.com/avatar/" + gravatar_mail + "?size="+str(size)
    
    context={
        "gravatar_url": gravatar_url
    }
    return render(request,'index.html',context)