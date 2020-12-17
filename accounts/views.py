from django.shortcuts import render, redirect
from .forms import UserRegisterForm,UserChange
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User



def userChecker(request):
    username = request.GET.get('username', None)
    email = request.GET.get('email',None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists(),
        'email_taken': User.objects.filter(email__iexact=email).exists()
        }
    return JsonResponse(data)

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            user = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {user}')
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)



def userlogin(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome {username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def userlogout(request):
    logout(request)
    messages.info(request, "Your Successfully logged out!")
    return redirect('login')

