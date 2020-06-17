from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from apartments.models import Apartments
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('User logged in')
            messages.success(request, 'User logged in')
            return redirect('dashboard')
        else:
            print("Incorrect login or password")
            messages.error(request, 'Incorrect login or password')
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
                messages.error(request, "user exists")
                return redirect("register")
            if User.objects.filter(email=email).exists():
                print("Email exists")
                messages.error(request, "email exists")
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
            messages.success(request, 'registered')
            return redirect('login')
        else:
            print("passwords do not match")
            messages.error(request, "passwords do not match")
            return redirect('register')
    data = {"header_h1": "Реєстрація",
            "header_p": "Головна >> Реєстрація"}
    return render(request, 'account/register.html', context=data)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        print("Logged out")
        messages.success(request, "Logged out")
    return redirect('index')


@login_required
def dashboard(request):
    apartments = Apartments.objects.order_by(
        '-list_date').filter(is_published=True, favorits=request.user)

    paginator = Paginator(apartments, 2)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        "apartments": page,
        "header_h1": "Dashboard",
        "header_p": "Головна >> Dashboard",
    }

    return render(request, 'account/dashboard.html', context)
