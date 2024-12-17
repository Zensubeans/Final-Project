from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Role, Users, Courses, Scan
from django.contrib import messages
from django.contrib.auth import login, authenticate

def user_home(request):
    return render(request, "user_template/home.html")

def scan(request):
    return render(request, "user_template/scan.html")

def userviewstudents(request):
    user = Users.objects.all()
    return render(request, "user_template/userviewstudents.html", {'userdata': user})

def userviewcourses(request):
    courses = Courses.objects.all()
    return render(request, "user_template/userviewcourses.html", {'userdata': courses})