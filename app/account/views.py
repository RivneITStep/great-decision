from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from apartments.models import Apartments


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('User logged in')
            return redirect('dashboard')
        else:
            print("Incorrect login or password")
            return redirect('login')
    #request.method == GET
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
    if request.method == "POST":
        auth.logout(request)
        print("Logged out")
    return redirect('index')


def dashboard(request):
    apartments = Apartments.objects.order_by(
        '-list_date').filter(is_published=True, favorits=request.user)

    paginator = Paginator(apartments, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    # print("page: ", page)

    context = {
        "apartments": page,
        "header_h1": "Dashboard",
        "header_p": "Головна >> Dashboard",
    }

    return render(request, 'account/dashboard.html', context)
