from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm  
from django.contrib.auth import authenticate, login, get_user_model
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
import urllib.parse
# import pdb
# Create your views here.

@csrf_protect
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

@csrf_protect
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

@csrf_protect
def create_event(request):
    return render(request, 'create_event.html', {'display_id':request.user})


@csrf_exempt
def api_resp(request):
    username = None
    password = None
    # username = request.GET.get('username')
    # password = request.GET.get('password')
    # body = json.loads(request.body)
    # content = body['content']
    # username = body['username']
    # password = body['password']
    if username is None or password is None:
        try:
            # asd = request.query_parms.get('content')
            # body_unicode = request.body.decode('utf-8')

            # data_json = urllib.parse.unquote(body_unicode)
            data_json = urllib.parse.unquote(request.body.decode('utf-8'))
            # pdb.set_trace()
            data = json.loads(data_json)
            for key in data:
                # pdb.set_trace()
                if key == 'username':
                    username = data[key]
                elif key == 'password':
                    password = data[key]
                else:
                    responseData = {
                        'authentication':'False',
                        'reason': 'Too many params in the request'
                    }
                    return HttpResponse(json.dumps(responseData), content_type="application/json")
        except:
            pass

    # print(data)
    # for i in data:
    #     if "username=" in i:
    #         username = i[9:]
    #         print(username)
    #     elif "password=" in i:
    #         password = i[9:]
    #         print(password)
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
                'password': password,
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
            'password': password,
            'authenticated':'False',
            'reason':'Password or Username is incorrect'
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
