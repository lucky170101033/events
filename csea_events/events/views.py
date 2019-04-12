from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm  
from django.contrib.auth import authenticate, login, get_user_model
import json
from django.http import JsonResponse
import urllib.parse
# Create your views here.

def loginPage(request):
    lform = LoginForm(request.POST or None)
    context ={'form':lform}
    print(request.user.is_authenticated)

    if lform.is_valid():
        print(lform.cleaned_data)
        username = lform.cleaned_data.get('email')
        password = lform.cleaned_data.get('password')
        user = authenticate(request, username = username, password = password)
        
        login(request, user)
        if request.user.is_authenticated:
            return render(request, 'home.html', {'display_id':username})
            
    return render(request, 'login.html', context)

User = get_user_model()
def registerPage(request):
    rform = RegisterForm(request.POST or None)
    context = {
        'form':rform
    }
    if rform.is_valid():
        mail = rform.cleaned_data.get('email')
        password = rform.cleaned_data.get('password')
        # name = rform.cleaned_data.get('name')
        username = rform.cleaned_data.get('username')
        # print(username)
        add_user = User.objects.create_user(username=username, password=password)
        return render(request, 'register_success.html', context)
        print(add_user)
    return render(request, 'register.html', context)

def create_event(request):
    return render(request, 'create_event.html', {'display_id':request.user})

def api_resp(request):

    body_unicode = request.body.decode('utf-8')
    username= request.GET.get('username')
    password = request.GET.get('password')
    # body = json.loads(request.body)
    # content = body['content']
    # username = body['username']
    # password = body['password']
    data = urllib.parse.unquote(request.body.decode('utf-8')).split('&')
    username = None
    password = None
    for i in data:
        if "username=" in i:
            username = i[9:]
            print(username)
        elif "password=" in i:
            password = i[9:]
            print(password)
    if username is None or password is None:
        responseData = {
            'authentication':'False',
            'reason': 'Username or Password missing in the request'
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")

    user  = authenticate(username =username,password=  password)
    print(user)
    if user is not None:
        responseData = {
                'username': username,
                'authenticated':'True',
                'eventList(example)' : [
                    'xyz',
                    'pqr',
                    'abc'
                ],
                'eventDates(example)' : [
                    '201904231415',
                    '201904292000'
                ]
            }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    else:
        responseData = {
            'username':username,
            'authenticated':'False',
            'reason':'Password or Username is incorrect'
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
