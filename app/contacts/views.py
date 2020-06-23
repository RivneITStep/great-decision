from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        apartment_title = request.POST['apartment_title']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        apartment_id = request.POST['apartment_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            contact = Contact.objects.all().filter(
                apartment_id=apartment_id, user_id=user_id)
            if contact:
                print("Contact added")
                return redirect('/apartments/' + apartment_id)

        contact = Contact(title=apartment_title, apartment_id=apartment_id, name=name,
                          email=email, phone=phone, message=message, user_id=request.user.id)
        contact.save()

        send_mail(
            "New connect",
            "Apartment for " + apartment_title + " contact witch new client " +
            message + " " + name + " " + email + " " + phone,
            "denus.denisovuch@gmail.com",
            [realtor_email],
            fail_silently=False
        )

        return redirect('/apartments/' + apartment_id)
