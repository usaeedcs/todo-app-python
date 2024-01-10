from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm, TODOForm
from .models import TODO
from django.contrib.auth import authenticate, login as _login, logout as _logout
from django.contrib.auth.decorators import login_required
# GET /


def home(request):
    '''
    This function handles request to home page.
    if user is authenticated, it displays the home page with TODO form and list of TODOs.
    else it will redirect back to login page
    '''
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request, 'home.html', {'form': form, 'todos': todos})

    else:
        return redirect('login')


# GET|POST /login
def login(request):
    """
    This function handles request to /login
    if request type is GET it will display login form else it will
    authenticate the user and redirect to the home page
    """
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "login.html", {"form": login_form})
    else:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                _login(request, user)
                return redirect('home')
        # If the form is invalid, render the same login template with errors
        return render(request, 'login.html', {'form': login_form, 'errors': ["Invalid username or password"]})


# GET|POST /signup
def signup(request):
    """
    This function handles request to /signup
    if request type is get, it will display signup form else
    it will create a new user and redirect to login page
    """
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form': form})


# POST /add-todo/
@login_required(login_url='login')
def add_todo(request):
    """
    This function is responsible for handling add todo request
    """
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect("home")
        else:
            return render(request, 'home.html', context={'form': form})


# POST /update-todo/<int:id>/<str:status>/
@login_required(login_url='login')
def update_todo(request, id, status):
    """
    This function is responsible for handling update todo request
    """
    todo = TODO.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')


# DELETE /delete-todo/<int:id>/
@login_required(login_url='login')
def delete_todo(request, id):
    """
    This function is responsible for handling delete request
    """
    TODO.objects.get(pk=id).delete()
    return redirect('home')

# POST /logout


def logout(request):
    """
    This function handles request to /logout
    """
    _logout(request)
    return redirect('login')
