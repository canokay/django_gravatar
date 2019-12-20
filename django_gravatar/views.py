from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

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
    return render(request, 'django_gravatar/login.html', context)



def IndexView(request):
    return render(request,'django_gravatar/index.html')