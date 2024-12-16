from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Role, Users, Courses, Scan
from django.contrib import messages

def admin_home(request):
    return render(request, "hod_template/home_content.html")

def add_student(request):
    return render(request, "hod_template/add_student_template.html")

def add_student_save(request):
    if request.method != "POST":
        messages.error(request, "Failed")
        return HttpResponseRedirect("/add_student")
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        device = request.POST.get("device")
        password = request.POST.get("password")
        role_name = request.POST.get("role")
        user = Users(name=name, email=email, password=password, device=device, role=role_name)
        user.save()
        role_name = Role(role_name=role_name)
        role_name.save()
        messages.success(request, "Success")
        return HttpResponseRedirect("/add_student")

def add_course(request):
    return render(request, "hod_template/add_course_template.html")

def add_course_save(request):
    if request.method != "POST":
        messages.error(request, "Failed")
        return HttpResponseRedirect("/add_course")
    else:
        course = request.POST.get("course")
        course_model = Courses(course_name=course)
        course_model.save()
        messages.success(request, "Success")
        return HttpResponseRedirect("/add_course")

def scanner(request):
    return render(request, "hod_template/scanner.html")

def viewusers(request):
    user = Users.objects.all()
    return render(request, "viewusers.html", {'userdata': user})

def viewcourses(request):
    courses = Courses.objects.all()
    return render(request, "viewcourses.html", {'userdata': courses})

def deleteprofile(request, id):
    us = Users.objects.get(id=id)
    us.delete()
    return redirect("/viewusers")

def deletecourse(request, id):
    us = Courses.objects.get(id=id)
    us.delete()
    return redirect("/viewcourses")

def editprofile(request, id):
    user = Users.objects.get(id=id)
    return render(request, "editprofile.html", {'us':user})

def updateprofile(request, id):
    newname = request.POST['name']
    newemail = request.POST['email']
    newpassword = request.POST['password']
    newdevice = request.POST['device']
    us = Users.objects.get(id=id)
    us.name = newname
    us.email = newemail
    us.password = newpassword
    us.device = newdevice
    us.save()
    return redirect("/viewusers")
