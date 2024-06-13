from django.shortcuts import render
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from _ast import Pass
# from main_app.app_forms import Employee_form
# from main_app.models import Employee, Contacts
# from main_app.users import people
from django.template import RequestContext


# Create your views here.
def home(request):
    return render(request, "index.html", )


def About(request):
    pass
    return render(request, "About.html")


def Causes(request):
    pass
    return render(request, "causes.html")


def Volunteer(request):
    pass
    return render(request, "Volunteer.html")


def Events(request):
    pass
    return render(request, "News.html")


def all_volunteers(request):
    pass
    return render(request, "All_volunteers.html", )


def Contact(request):
    pass
    return render(request, "Contact.html")


def Donation(request):
    pass
    return render(request, "Donate.html")


def signin(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        myuser = authenticate(username=get_email, password=get_password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, 'Login.html')


def signout(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == "POST":
        get_first_name = request.POST.get('first')
        get_last_name = request.POST.get('last')
        get_email = request.POST.get('email')
        get_date = request.POST.get('date')
        get_number = request.POST.get('number')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')

        if get_password != get_confirm_password:
            messages.info(request, 'password not matching!')
            return redirect('/signup')
        try:
            if User.objects.get(username=get_email):
                messages.warning(request, "Email already taken!")

        except Exception as identifier:
            pass
        myuser = User.objects.create_user(  get_email, get_email, get_password)
        myuser.save
        messages.success(request, "User Created Successfully")
        return redirect('signin')

    return render(request, 'Signup.html')
