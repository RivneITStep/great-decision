from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def login(request):
    data = {"header_h1": "Вхід",
            "header_p": "Головна >> Вхід"}
    return render(request, 'account/login.html', context=data)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['Name']
        last_name = request.POST['Surname']
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                print("user exists")
                return redirect("register")
            if User.objects.filter(email=email).exists():
                print("Email exists")
                return redirect("register")
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
            print('registered')
            return redirect('login')
        else:
            print("passwords do not match")
            return redirect('register')
    data = {"header_h1": "Реєстрація",
            "header_p": "Головна >> Реєстрація"}
    return render(request, 'account/register.html', context=data)


def logout(request):
    return render(request, 'account/logout.html')


def dashboard(request):
    return render(request, 'account/dashboard.html')
