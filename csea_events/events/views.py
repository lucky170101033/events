from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm, EventCreatorForm ,PollCreatorForm
# , EventFormSet
from django.contrib.auth import authenticate, login, get_user_model, logout
import json
from django.http import JsonResponse
import urllib.parse
from django.contrib.auth.decorators import login_required
from .models import Event
from .models import Poll,Vote
from  django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# Create your views here.
# 
#  The Login Page, if the user already logged in this redirects to homepage
# sd

def loginPage(request):
    lform = LoginForm(request.POST or None)
    context ={'form':lform}
    # print(request.user.is_authenticated)


    
    if request.user.is_authenticated:
        return redirect('home_page')

    if lform.is_valid():
        # print(lform.cleaned_data)
        username = lform.cleaned_data.get('email')
        password = lform.cleaned_data.get('password')
        user = authenticate(request, username = username, password = password)
        
        
        if user is not None:
            login(request, user)
            
            return redirect('home_page')
        else:
            return redirect('loginPage')
            
    return render(request, 'login.html', context)

User = get_user_model()

# @login_required(login_url='loginPage')
# def admin_view(request):

#     return render(request, 'admin.html',{})
# # 
#  The register page, temporary and will be replaced with proper cide from partha
# 

@login_required(login_url='loginPage')
def profile_view(request):
    return render(request, 'profile.html',{'username':request.user})

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
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'register.html', context)
        
        print(add_user)
    return render(request, 'register.html', context)


# 
# Create event form page, redirects to login page if user is un-authenticated
# 
# 
@login_required(login_url='loginPage')
def create_event(request):
    form = EventCreatorForm(request.POST or None)

    if form.is_valid():
        new_event=form.save()
        form = EventCreatorForm()
    #     capacity = form.cleaned_data.get('capacity')
    #     name= form.cleaned_data.get('name')
    #     event_date = form.cleaned_data.get('event_date')
    #     event_time = form.cleaned_data.get('event_time')
    #     fee = form.cleaned_data.get('fee')
    #     summary = form.cleaned_data.get('summary')
    #     invitees  =form.cleaned_data.get('invitees')
    #     event_instance = Event(name = name, fee=fee,capacity=capacity,date=event_date, time=event_time, faq=summary, invitees = invitees) 
    #     event_instance.save()
    # print(request.user)
    return render(request, 'create_event.html', {'form':form})
#
#Homepage, requires login, has links for everything
#
@login_required(login_url='loginPage')
def home_page(request):
    events=Event.objects.all().order_by('date') 
   
    # if str(request.user) == 'admin@iitg.ac.in':
    #     return redirect('admin-page')
    return render(request, 'home.html', {'display_id':request.user, 'events':events})

#
# logout view, logs user out and redirects user to login page
#
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('loginPage')

def poll_view(request, event_id):
    events=Event.objects.filter(event_id=event_id)
    print(events[0].summary)
    context = {
        'event_name': events[0].name,
        'event_date': events[0].date,
        'event_time': events[0].time,
        'event_fee':events[0].fee,
        'contact_info':events[0].contact_info,
        'summary':events[0].summary,

    }
    return render(request,'event_info.html',context)


#
#REST Api, will be redone once web is finished
#


@login_required(login_url='loginPage')
def change_password(request):
    if request.method=='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            logout(request)
            return redirect('loginPage')
        else:
            return redirect('change_passwd')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'change_password.html',args)

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
                    print(data[key])
                    username = data[key]
                elif key == 'password':
                    print(data[key])
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
    event_list = []
    for i in Event.objects.all():
        event_list += [i.event_id]

    
    if user is not None:
        responseData = {
                'username': username,
                'password': password,
                'authenticated':'True',
                'eventList(example)' : event_list,
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

@login_required(login_url='loginPage')
def poll_count_view(request,event_id):
    poll= Event.objects.filter(event_id=event_id)
    temp=Poll.objects.filter(event_id=event_id)
    if not temp:
        temp = Poll(event_id=event_id,response_coming=0,response_not_coming=0,response_not_sure=0)
        response_coming=temp.response_coming
        response_not_coming=temp.response_not_coming
        response_not_sure=temp.response_not_sure
        id_event=temp.event_id
        temp.save()
    else:
            response_coming=temp[0].response_coming
            response_not_coming=temp[0].response_not_coming
            response_not_sure=temp[0].response_not_sure
            id_event=temp[0].event_id   
       # print(temp.event_id)
    context = {
        'response_coming' : response_coming,
        'response_not_coming' : response_not_coming,
        'response_not_sure' : response_not_sure ,
        'kk':id_event,

    }  
    #temp.save()    
    return render(request,'poll_view.html',context)

@login_required(login_url='loginPage')
def poll_vote(request,event_id):   
    poll=Poll.objects.get(event_id=event_id)
    id_user=str(request.user)
    temp1=Poll.objects.filter(event_id=event_id)
    flag=0
    temp_str=str(temp1[0].user_id)
    if (temp_str.find(id_user)!=-1):
        flag=1
    else :
        pass    

    if (flag==0):
        poll.user_id=poll.user_id + id_user + ', '
        vote=Vote(vote_id=event_id,user_id=id_user,user_vote=4)
        form = PollCreatorForm(data=request.POST)

        if(request.method=='POST'):
            if form.is_valid():
                data_temp=form.save(event_id,poll,request)
                #poll.save()
                if (data_temp=='response_not_coming'):
                    vote.user_vote=1
                elif (data_temp=='response_coming'):
                    vote.user_vote=2
                else:
                    vote.user_vote=3      
                vote.save()      
                form = PollCreatorForm()
                return redirect('poll_count',event_id)
            else :
                return redirect('poll_count_vote', event_id)
    else :
        context ={
            'kk':event_id,
            'everything':id_user
        }
        return render(request,'done.html',context=context)        
    return render(request, 'poll_vote.html', {'form':form})

@login_required(login_url='loginPage')
def poll_modify(request,event_id):
    id_user=request.user
    vote=Vote.objects.filter(vote_id=event_id,user_id=id_user)

    if vote:
        poll=Poll.objects.filter(event_id=event_id)
        # temp_data=vote[0].user_vote
        
        # if (temp_data==1):
        #     poll[0].response_not_coming=poll[0].response_not_coming -1
        # elif (temp_data==2):
        #     poll[0].response_coming=poll[0].response_coming - 1
        # else :
        #     poll[0].response_not_sure=poll[0].response_not_sure -1 
        # poll[0].save()
        form = PollCreatorForm(data=request.POST)

        if(request.method=='POST'):
            if form.is_valid():
                data_temp=form.save(event_id,poll[0],request)
                #poll.save()
                if (data_temp=='response_not_coming'):
                    vote[0].user_vote=1
                elif (data_temp=='response_coming'):
                    vote[0].user_vote=2
                else:
                    vote[0].user_vote=3      
                vote[0].save()      
                form = PollCreatorForm()
                return redirect('poll_count',event_id)
            else :
                return redirect('poll_count_vote', event_id)
    else :
        context = {
            'kk' : event_id,
        }
        return render(request,'error.html',context)  

    return render(request, 'poll_vote.html', {'form':form})
  
    