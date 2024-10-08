import json

from django.shortcuts import render
from datetime import datetime
import logging
from django.template.loader import render_to_string

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from _ast import Pass

from django.views.decorators.csrf import csrf_exempt
from main_app.app_forms import Volunteer_form, Causes_form, Event_forms, Happy_customers_form, Number_form
from main_app.models import Volunteers, Contacts, cause, Event, Number, happy_customers, Volunteer_application, multiple
from django.template import RequestContext
from django.core.mail import send_mail
# from Spreading.settings.base import EMAIL_HOST_USER



logger = logging.getLogger(__name__)


# Create your views here.


# Homepage
def home(request):
    return render(request, "index.html", )


# About page
def About(request):
    number = Number.objects.all()
    form = Number_form(request.POST)
    
    if request.method =="POST":
        if form.is_valid():
            number_instance = form.save()
            return redirect('about')
        else:
            number_instance = number.objects.first() or number()
            form = Number_form(instance=number_instance)
            
    return render(request, "About.html", {"number": number, "form":form})


# causes page
def Causes(request):
    causes = cause.objects.all()
    form = Causes_form()
    if request.method =="POST":
        form =Causes_form(request.POST, request.FILES)
        logger.debug(form)
        if form.is_valid():
            form.save()
            return redirect('/causes')    
    return render(request, "causes.html", {"form":form, "causes":causes})

def cause_delete(request, cause_id):
    cause_instance = get_object_or_404(cause, pk=cause_id)
    if request.method =="POST":
          logger.debug("Delete POST request received for cause ID: %s", cause_id)


          cause_instance.delete()
        
    return redirect('Causes')
    
    
    return render(request, "causes.html",  {"causes":causes})
    



# information about the causes we support
def more_causes(request, pk):
    more = get_object_or_404(cause,id=pk)
    images = multiple.objects.filter(causes=more) 
    
    try:

     if request.method == "POST":
           post_images = request.FILES.getlist('images')
           logger.debug(post_images)

           for img in post_images:
                causes_images = multiple.objects.create(
                    images=img,
                    causes=more
                )
                return redirect('more_causes', pk=pk)
            
                context = {
            'more': more,
            'images': images,
            }
    # except  Exception as e:
        
    #  print(e)
       
           return redirect('more_causes', pk=pk) 
    except Exception as e:
        logger.error(f"Error uploading images: {e}")
    # logger.debug(images)
    return render(request, "more_causes.html",{"more": more, "images": images})



def delete_image(request, image_id):
    if request.method == 'POST':
        image = get_object_or_404(multiple, id=image_id)
        image.delete()
        return redirect('more_causes', pk=image.causes.id)
    return redirect('more_causes', pk=image.causes.id)


    


# volunteer page
# @permission_required('main_app.add_employee', raise_exception=True)
@login_required

def Volunteer(request):
    if request.method == "POST":
        fname = request.POST.get('volunteer-name')
        femail = request.POST.get('volunteer-email')
        fsubject = request.POST.get('volunteer-subject')
        fdoc = request.FILES.get('volunteer-doc')
        fcomment = request.POST.get('volunteer-message')
        query = Volunteer_application(name=fname, Email=femail, subject=fsubject, post=fdoc, comment=fcomment)
        query.save()
        messages.success(request, "Thanks For Application. I will Get Back To You Soon!")
        return redirect('/volunteer')

    return render(request, "Volunteer.html")


@login_required
@permission_required('main_app.add_volunteer', raise_exception=True)
def add_volunteer(request):
    if request.method == "POST":
        form = Volunteer_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Added successfully")
            return redirect("all_volunteers")

    else:
        form = Volunteer_form()
    return render(request, "add_volunteer.html", {"form": form})


def add_images(request):
    events = Event.objects.all()
    return render(request, "add.html", {"events": events})


# information about upcoming events(donations)
def Events(request, ):
    events = Event.objects.all()
    happy = happy_customers.objects.all()
    form = Event_forms(request.POST, request.FILES)
   
    
    
    
    if request.method == "POST":
        
        if form.is_valid():
            form.save()
            
        return redirect('/events')
    else:
        form = Event_forms()
        

    
    return render(request, "News.html", {"events": events, "form":form})


def events_delete(request, events_id):
    event_instance = get_object_or_404(Event, pk=events_id)
    
    if request.method == "POST":
        event_instance.delete()
        return redirect('/events')
    return render(request, "News.html")


def testimonies(request):
     happy = happy_customers.objects.all()
     form = Happy_customers_form(request.POST, request.FILES)
    
     if request.method =="POST":
        if form.is_valid():
            form.save()
            return redirect('/testimonies') 
        else:
            form = Happy_customers_form()
     return render(request, "testimonies.html",{"happy": happy, "form":form} )
 
def testimonies_delete(request, testimonies_id):
   
   testimony = get_object_or_404(happy_customers, pk=testimonies_id)
    
   if request.method =="POST":
       testimony.delete()
       
       return redirect('/testimonies')
   
        
        



# more information about the event we are holding
def information(request, pk):
    event = Event.objects.get(id=pk)
    return render(request, "information.html", {"event": event})




# Displays all voluntees on the page
def all_volunteers(request):
    volunteer = Volunteers.objects.all()

    paginator = Paginator(volunteer, 30)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)

    return render(request, "All_volunteers.html", {"volunteer": data})


def volunteer_details(request, emp_id):
    volunteer = Volunteers.objects.get(pk=emp_id)  # SELECT * FROM Volunteers
    return render(request, 'volunteer_details.html', {"volunteer": volunteer})


@login_required
@permission_required('main_app.delete_volunteer')
def volunteer_delete(request, emp_id):
    employee = get_object_or_404(Volunteers, pk=emp_id)
    employee.delete()
    messages.warning(request, 'Deleted successfully')
    return redirect("all_volunteers")


@login_required
@permission_required('main_app.view_volunteer')
def search_volunteers(request):
    search_word = request.GET["search_word"]
    employees = Volunteers.objects.filter(Q(name__icontains=search_word) | Q(email__icontains=search_word)
                                          )

    paginator = Paginator(employees, 30)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    # Elastic search
    return render(request, "All_volunteers.html", {"employees": data, "search_word": search_word})


@login_required
@permission_required('main_app.change_volunteer')
def volunteer_update(request, emp_id):
    volunteer = get_object_or_404(Volunteers, pk=emp_id)  # SELECT *FROM Volunteers WHERE id = 1
    if request.method == "POST":
        form = Volunteer_form(request.POST, request.FILES, instance=volunteer)
        if form.is_valid():
            form.save()
            messages.success(request, "updated successfully")
            return redirect('details', emp_id)
    else:
        form = Volunteer_form(instance=volunteer)

    return render(request, 'update.html', {'form': form})


# contact form 

def Contact(request):
    if request.method == "POST":
       fname= request.POST.get("first-name")
       sname = request.POST.get("last-name")
       mail = request.POST.get("email")
       subj = request.POST.get("message")
    
       send_mail(
           fname,
           subj, 
           mail,
           recipient_list=['spreadingsmilescharityorg@gmail.com'],
           
           
       )
       logger.error(f"email sending{fname}, {subj}, {mail},")
       query = Contacts(name= fname, email=mail , subject=subj)
       query.save()
    #    messages.success("Thanks for contacting. we will get back to you soon!")
       return redirect('/contact')
   
        
    return render(request, "Contact.html")


# @login_required
# Donation page
# def Donation(request):
#     pass
#     return render(request, "Donate.html")


def map(request):
    pass
    return render(request, "map.html")



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


@login_required
def signout(request):
    logout(request)
    return redirect('home')



def signup(request):
    if request.method == "POST":
        get_first_name = request.POST.get('first')
        get_last_name = request.POST.get('last')
        user= get_first_name+ get_last_name
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
        myuser = User.objects.create_user(get_email,get_email, get_password)
        
        myuser.save
        messages.success(request, "User Created Successfully")
        return redirect('signin')

    return render(request, 'Signup.html')
