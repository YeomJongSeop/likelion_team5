from django.shortcuts import render , redirect
import json
from django.http import JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            id = form.cleaned_data.get('id')
            password = form.cleaned_data.get('password')
            user = authenticate(id=id, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'workhol/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user.last_login = timezone.now()  # 마지막 로그인 시간 갱신
                user.save()
                login(request, user)
                return redirect('home')  # 로그인 후 이동할 페이지
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'workhol/home.html')

def workhol_site(request):
    return render(request, 'workhol/workhol_site.html')

def language_study_site(request):
    return render(request, 'workhol/language_study_site.html')

def intern_site(request):
    return render(request, 'workhol/intern_site.html')

