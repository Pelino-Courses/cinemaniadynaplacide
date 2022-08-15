from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthorised_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
# Create your views here.
@unauthorised_user
def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email,password=password)
        if user is not None:
            login(request, user)
            return redirect('/movies')
        else:
            messages.info(request, 'Incorect email OR password.')
    template_name = "signin.html"
    return render(request, template_name, {})

@unauthorised_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully for user '+username)
            return redirect("/login")
    template_name = "signup.html"
    context = { 'form':form }
    return render(request, template_name, context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    movies = Movie.objects.all().order_by('release_date')
    template_name = "index.html"
    context = { 'movies' : movies }
    return render(request, template_name, context)

@login_required(login_url="login")
def movies_page(request):
    movies = Movie.objects.all().order_by('release_date')
    template_name = "movielist.html"
    context = { 'movies': movies }
    return render(request, template_name, context)

@login_required(login_url="login")
def single_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    template_name = "moviesingle.html"
    context = { 'movie': movie }
    return render(request, template_name, context)

@login_required(login_url='login')
def user_profile(request):
    template_name = "userprofile.html"
    context = {}
    return render(request, template_name, context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def add_movie(request):
    template_name = "add-movie.html"
    form  = MovieForm()
    if request.method == 'POST' or request.FILES:
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            Movie.objects.create(
                release_date=request.POST["release_date"],
                genre=request.POST["genre"],
                movie_title=request.POST["movie_title"],
                main_actor=request.POST["main_actor"],
                caption=request.POST["caption"],
                movie_link=request.POST["movie_link"],
                posted=f"{request.user.firstname} {request.user.lastname}",
                trailler=request.FILES["trailler"],
                wallpaper=request.FILES["wallpaper"]
            )
            # form.save()
            messages.success(request, 'Movie added successfully')
            return redirect("/")
    context = { 'form': form }
    return render(request, template_name, context)

def about(request):
    return HttpResponse('about')