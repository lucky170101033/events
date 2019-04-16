from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from .models import Profile

# Create your views here.

def loginPage(request):

    if request.method == 'GET':
        lform = LoginForm()
        context = {
            'form':lform
        }
        return render(request,'login.html',context)
    else:
        lform = LoginForm(request.POST)
        if lform.is_valid():
            username = lform.cleaned_data.get('name')
            print(username)
            password = lform.cleaned_data.get('password')
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None and request.user.is_authenticated:
                login(request, user)
                return render(request, 'home.html', {'display_id': username})


User = get_user_model()


def registerPage(request):

    if request.method == 'GET':
        rform = RegisterForm()
        context = {
            'form': rform
        }
        return render(request, 'register.html', context)
    else:
        rform = RegisterForm(request.POST)
        if rform.is_valid():

            department = rform.cleaned_data.get('department')
            program = rform.cleaned_data.get('program')
            roll_no = rform.cleaned_data.get('roll_no')
            phone_no = rform.cleaned_data.get('phone_no')
            print(roll_no, type(roll_no))
            email = rform.cleaned_data.get('email')
            print(email)
            password = rform.cleaned_data.get('password')
            username = rform.cleaned_data.get('name')
            add_user = User.objects.create_user(username=username, email=email, password=password)

            add_profile = Profile.objects.create(user=add_user,department=department,program=program,roll_no=str(roll_no),phone_no=str(phone_no))
            return redirect('/')
        else:
            return redirect('/register/')

