from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from myapp.models import Users, Courses
from django.utils.timezone import now


def showDemoPage(request):
    return render(request, "demo.html")

def showLoginPage(request):
    return render(request, "login_page.html")

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
    else:
         email = request.POST.get("email")
         password = request.POST.get("password")
         user = authenticate(request, email=email, password=password)
         if user != None:
             login(request, user)
             return HttpResponseRedirect('/admin_home')
         else:
             messages.error(request, "Invalid Login Details")
             return HttpResponseRedirect("/")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def register(request):
    return render(request, "registration.html")

def viewusers(request):
    user = Users.objects.all()
    return render(request, "viewusers.html", {'userdata': user})

def viewcourses(request):
    courses = Courses.objects.all()
    return render(request, "viewcourses.html", {'userdata': courses})