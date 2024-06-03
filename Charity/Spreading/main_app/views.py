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
