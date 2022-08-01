from django.shortcuts import redirect, render
from .models import Card, Banner
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def index(request):
    cards = Card.objects.all()
    banners = Banner.objects.all()

    return render(request, 'index.html', {'cards': cards, 'banners': banners})

def userlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are successfully Logged In.')
            return redirect('index')
        else:
            messages.warning(request, "Your credentials doesn't match with our database.")

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']

            if password == password2:
                myuser = User.objects.create_user(name, email, password)
                myuser.save()

                messages.success(request, 'You are successfully Registered...')
            else:
                messages.warning(request, 'Password is not same. Please check It.')
        except:
            messages.error(request, 'Username is already taken. Please use something else.')

    return render(request, "login.html")

def userlogout(request):
    logout(request)
    messages.success(request, 'You are successfully Logged Out...')
    return redirect('index')
    