from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from posts.models import Post
from users.models import Profile
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout

def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', context={"form":form})
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'users/register.html', context={"form":form})
        elif form.is_valid():
            form.cleaned_data.__delitem__("password_confirm")
            age = form.cleaned_data.pop("age",None)
            image = form.cleaned_data.pop("image",None)
            if User.objects.filter(email=form.cleaned_data["email"]).exists():
                form.add_error(None, "User with given email already exists")
                return render(request, 'users/register.html', context={"form":form, "error":"email already exists"})
            user = User.objects.create_user(**form.cleaned_data)
            if user:
                Profile.objects.create(user=user, age=age, image=image)
                return redirect('home')
            else:
                return HttpResponse('error')


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', context={"form":form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'users/login.html', context={"form":form})
        elif form.is_valid():
            user = authenticate(**form.cleaned_data)
            if not user:
                form.add_error(None, "Invalid username or password")
                return render(request, 'users/login.html', context={"form":form})
            elif user:
                login(request, user)
                return redirect('home')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile_view(request):
    posts= Post.objects.filter(author=request.user)
    return render(request, 'users/profile.html', context={"posts":posts})