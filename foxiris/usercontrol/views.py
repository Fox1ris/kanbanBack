from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User


def login_page(request):
    print('hello')
    return render(request, 'usercontrol/login.html')



def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        if user is not None:
            user.save()
            print(username, password, email)
            return redirect('home')
    return render(request, 'usercontrol/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('zaebumba')
            return redirect('home')
        else:
            print('not zaebumba')
    return render(request, 'usercontrol/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')
