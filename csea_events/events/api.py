from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm  
from django.contrib.auth import authenticate, login, get_user_model
import json
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
import urllib.parse
@csrf_exempt
def api_login(request):
    username = None
    password = None
    try:
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
                    'accepted':False,
                    'error-code':1,
                    'error_message':'Too many params',
                    'username':'',
                    'full_name':'',
                    'user_roll':-1,
                    'user_branch':'',
                    'user_year':-1,
                    'user_stream':'',
                    'user_phone':-1
                }
                return HttpResponse(json.dumps(responseData), content_type="application/json")
    except:
        responseData = {
                    'accepted':False,
                    'error-code':2,
                    'error_message':'Malformed Request Body',
                    'username':'',
                    'full_name':'',
                    'user_roll':-1,
                    'user_branch':'',
                    'user_year':-1,
                    'user_stream':'',
                    'user_phone':-1
                }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    if username is None or password is None:
        responseData = {
            'accepted':False,
            'error-code':3,
            'error_message':'Username or Password missing in the request',
            'username':'',
            'full_name':'',
            'user_roll':-1,
            'user_branch':'',
            'user_year':-1,
            'user_stream':'',
            'user_phone':-1
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")

    user  = authenticate(username = username, password =  password)
    if user is None: # TODO not none karna hai
        responseData = {
                'accepted':True,
                'error_code':0,
                'error_message':'',
                'username':"singh170101015",
                'full_name':"avneet singh",
                'user_roll':170101015,
                'user_branch':"cse",
                'user_year':2017,
                'user_stream':"btech",
                'user_phone':9126918864
            }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    else:
        responseData = {
            'accepted':'False',
            'error-code':4,
            'error_message':'Username invalid',
            'accepted':False,
            'username':'',
            'full_name':'',
            'user_roll':-1,
            'user_branch':'',
            'user_year':-1,
            'user_stream':'',
            'user_phone':-1
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")

@csrf_exempt
def api_signup(request):
    username = None
    password = None
    name = None
    roll_no = None
    year_admission = None
    phone_num = None
    try:
        data_json = urllib.parse.unquote(request.body.decode('utf-8'))
        # pdb.set_trace()
        data = json.loads(data_json)
        for key in data:
            # pdb.set_trace()
            if key == 'username':
                username = data[key]
            elif key == 'password':
                password = data[key]
            elif key == 'name':
                name = data[key]
            elif key == 'roll_no':
                roll_no = data[key]
            elif key == 'year_admission':
                year_admission = data[key]
            elif key == 'phone_num':
                phone_num = data[key]
            else:
                responseData = {
                    'accepted':False,
                    'error_message': 'Too many params in the request',
                    'error_code' : 1,
                }
                return HttpResponse(json.dumps(responseData), content_type="application/json")
    except:
        responseData = {
                    'accepted':False,
                    'error_message': 'Malformed request body',
                    'error_code' : 2
                }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    if username is None or password is None or roll_no is None or year_admission is None:
        responseData = {
            'accepted':False,
            'error_message': 'Username, Password, RollNo, Year are necessary',
            'error_code' : 3
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
        responseData = {
            'accepted':False,
            'error_message': 'Username already taken',
            'error_code' : 5
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    user = None
    # user  = authenticate(username = username, password =  password)
    if user is not None:
        responseData = {
            'accepted':False,
            'error_message': 'Username, Password, RollNo, Year are necessary',
            'error_code' : 4,
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    else:
        responseData = {
            'accepted':True,
            'error_message': '',
            'error_code' : 0,
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")

@csrf_exempt
def api_registerevent(request):
    username = None
    event_name = None
    event_fee = None
    event_exp_audience = None
    event_venue = None
    event_date = None
    event_time = None
    event_desc = None
    event_admin_comment = None
    event_target_audience = None
    event_poster = None
    try:
        data_json = urllib.parse.unquote(request.body.decode('utf-8'))
        # pdb.set_trace()
        data = json.loads(data_json)
        for key in data:
            # pdb.set_trace()
            if key == 'Event_Name':
                event_name = data[key]
            elif key == 'Event_Fee':
                event_fee = data[key]
            elif key == 'Event_exp_audience':
                event_exp_audience = data[key]
            elif key == 'Event_User_Venue':
                event_venue = data[key]
            elif key == 'Event_Date':
                event_date = data[key]
            elif key == 'Event_Time':
                event_time = data[key]
            elif key == 'Event_Description':
                event_desc = data[key]
            elif key == 'Event_Comments_For_Admin':
                event_admin_comment = data[key]
            elif key == 'Event_Target_Audience':
                event_target_audience = data[key]
            elif key == 'Event_Poster':
                event_poster = data[key]
            else:
                responseData = {
                    'accepted':False,
                    'error_message': 'Too many params in the request',
                    'error_code' : 1,
                }
                return HttpResponse(json.dumps(responseData), content_type="application/json")
    except:
        responseData = {
                    'accepted':False,
                    'error_message': 'Malformed request body',
                    'error_code' : 2,
                    'event_id':-1
                }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    if username is None or event_date is None \
                        or event_fee is None \
                        or event_name is None \
                        or event_time is None :
        responseData = {
            'accepted':False,
            'error_message': 'Username, Date, Time, Name, Fee are necessary',
            'error_code' : 3,
            'event_id':-1
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    # TODO create event and get event id
    event_id = -1
    if event_id == -1:
        responseData = {
            'accepted':False,
            'error_message': 'Error creating event',
            'error_code' : 4,
            'event_id':-1
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    else:
        responseData = {
            'accepted':True,
            'event_id':event_id,
            'error_message': '',
            'error_code' : 0
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")

@csrf_exempt
def api_getevent(request):
    event_id = None
    try:
        data_json = urllib.parse.unquote(request.body.decode('utf-8'))
        # pdb.set_trace()
        data = json.loads(data_json)
        for key in data:
            # pdb.set_trace()
            if key == 'event_id':
                event_id = data[key]
            else:
                responseData = {
                    'accepted':False,
                    'error_message': 'Too many params in the request',
                    'error_code' : 1,
                }
                return HttpResponse(json.dumps(responseData), content_type="application/json")
    except:
        responseData = {
                    'accepted':False,
                    'error_message': 'Malformed request body',
                    'error_code' : 2
                }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    if event_id is None:
        responseData = {
            'accepted':False,
            'error_message': 'Username, rating, ui, ux are necessary',
            'error_code' : 3
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    # TODO check if event exists
    # user  = authenticate(username = username, password =  password)
    else:
        responseData = {
            'accepted':True,
            'error_message': '',
            'error_code' : 0,
            'username' : None,
            'event_name' : None,
            'event_fee' : None,
            'event_exp_audience' : None,
            'event_venue' : None,
            'event_date' : None,
            'event_time' : None,
            'event_desc' : None,
            'event_admin_comment' : None,
            'event_target_audience' : None,
            'event_poster' : None
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")

@csrf_exempt
def api_feedbackapp(request):
    try:
        data_json = urllib.parse.unquote(request.body.decode('utf-8'))
        # pdb.set_trace()
        data = json.loads(data_json)
        for key in data:
            # pdb.set_trace()
            if key == 'App_UI_Rating':
                ui = data[key]
            elif key == 'App_UX_Rating':
                ux = data[key]
            elif key == 'App_Overall_Rating':
                rating = data[key]
            elif key == 'App_Feedback_Comment':
                comment = data[key]
            else:
                responseData = {
                    'accepted':False,
                    'error_message': 'Too many params in the request',
                    'error_code' : 1,
                }
                return HttpResponse(json.dumps(responseData), content_type="application/json")
    except:
        responseData = {
                    'accepted':False,
                    'error_message': 'Malformed request body',
                    'error_code' : 2
                }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    if username is None or rating is None or ui is None or ux is None:
        responseData = {
            'accepted':False,
            'error_message': 'Username, rating, ui, ux are necessary',
            'error_code' : 3
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    # TODO check if user exists
    user = None
    # user  = authenticate(username = username, password =  password)
    if user is not None:
        responseData = {
            'accepted':False,
            'error_message': 'Username, Password, RollNo, Year are necessary',
            'error_code' : 4,
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
    else:
        responseData = {
            'accepted':True,
            'error_message': '',
            'error_code' : 0,
        }
        return HttpResponse(json.dumps(responseData), content_type="application/json")
