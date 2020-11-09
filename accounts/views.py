from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import psycopg2
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.template.loader import get_template 
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('/')
    context = {'form': form}
    return render(request, 'registration/signup.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        messages.success(request, 'You have been succesfully logged ')
        return redirect('pages/home.html')
    else:
        messages.error(request, 'Username OR password is incorrect ')
        
    context = {}
    return render(request, 'accounts/login.html', context)    

def logoutUser(request):
    logout(request)
    return redirect('pages/login')


@login_required(login_url = 'login')
def home(request):

    conn = psycopg2.connect(dbname="votingdb", user="myuser", password="mypass")
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM auth_user")
    user_1 = cursor.fetchone()
    user = user_1[0]

    return render(request, 'pages/home.html', {'username':user})    

@login_required(login_url = 'login')
def profile(request):

    conn = psycopg2.connect(dbname="votingdb", user="myuser", password="mypass")
    cursor = conn.cursor()
    cursor2 = conn.cursor()
    cursor.execute("SELECT username FROM auth_user")
    cursor2.execute("Select date_joined FROM auth_user")
    user_1 = cursor.fetchone()
    user_date = cursor2.fetchone()
    user = user_1
    date = user_date[0]

    return render(request, "pages/profile.html", {'username':user, 'date':date})


