from django.shortcuts import render, redirect
from posts.models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def index(request):
    posts = Post.objects.all()
    #get all of the objects from the database Posts
    return render(request, 'index.html', {'posts': posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2: #if passwords match,check and see if we can create the user
            if User.objects.filter(email=email).exists():
                messages.info(request, "email already used")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already in use")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
            #need to create a login page and change it to login
        else: #passwords did not match
            messages.info(request, "Passwords did not match, try again")
            return redirect('register')

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Credentials do not match")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')