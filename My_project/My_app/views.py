from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import details

# Create your views here.
@login_required(login_url='login')
def insert(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        year_of_joining = request.POST['year_of_joining']
        rollno = request.POST['rollno']
        mobile_no = request.POST['mobile_no']
        place = request.POST['place']

        # Save the details
        data = details(
            name=name,
            age=age,
            email=email,
            year_of_joining=year_of_joining,
            rollno=rollno,
            mobile_no=mobile_no,
            place=place
        )
        data.save()
        return redirect("home")
    return render(request, "index.html",{'username': request.user.username})

# def home(request):
#     data_1 = details.objects.all()
#     return render(request, "home.html", {'student': data_1})


@login_required(login_url='login')  # Redirects to login page if user is not authenticated
def home(request):
    data_1 = details.objects.all()
    return render(request, "home.html", {'student': data_1, 'username': request.user.username})





@login_required(login_url='login')
def edit(request, id):
    data = details.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        year_of_joining = request.POST['year_of_joining']
        rollno = request.POST['rollno']
        mobile_no = request.POST['mobile_no']
        place = request.POST['place']

        # Update fields
        data.name = name
        data.age = age
        data.email = email
        data.year_of_joining = year_of_joining
        data.rollno = rollno
        data.mobile_no = mobile_no
        data.place = place
        data.save()

        return redirect("home")
    return render(request, "edit.html", {'data': data, 'username': request.user.username})

def delete(request, id):
    data = details.objects.get(id=id)
    data.delete()
    return redirect("home")

# Sign up view
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists, please choose another one.")
            return render(request, "signup.html")
        
        # Create the user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("login")  
    return render(request, "signup.html")

# Login view

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to home page after login
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


# Logout view
def user_logout(request):
    logout(request)
    return redirect("login")
