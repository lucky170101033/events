from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from . import models
from .models import Event,Poll, Vote
from django.forms import formset_factory, modelformset_factory
import uuid

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Your @iitg email'
            }), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your password'}), required=True)


    # TODO This doesn't always work
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not 'iitg.ac.in' in email:
    #         raise forms.ValidationError('Email must be iitg.ac.in or iitg.ernet.in')
    #     if not 'iitg.ernet.in' in email:
    #         raise forms.ValidationError('Email must be iitg.ac.in or iitg.ernet.in')
    #     if 'ad@gc.com' in email:
    #         return email
    #     return email

User = get_user_model()


class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Full Name'}),required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your college email (@iitg.ac.in)'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'select a username' }), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Your password'}), required=True)
    confirm_password = forms.CharField( label = 'Confirm Password', widget=forms.PasswordInput(attrs={'placeholder':'Your password (again)'}), required=True)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        queryset = User.objects.filter(username = email)

        if 'iitg.ac.in' not in email:
            raise forms.ValidationError("Enter a valid email")
        if queryset.exists():
            raise forms.ValidationError("Email already active")
        return email



    def clean_confirm_password(self):
        passw = self.cleaned_data.get('confirm_password')
        passw_orig = self.cleaned_data.get('password')

        if passw != passw_orig:
            raise forms.ValidationError('Both passwords must match')
        
        return passw
        # TODO fix this
    # def clean_email(self):
    #         email = self.cleaned_data.get('email')
    #         if not 'iitg.ac.in' in email or not 'iitg.ernet.in' in email:
    #              raise forms.ValidationError('Email must be iitg.ac.in or iitg.ernet.in')
    #         return email

# class EventCreatorForm(forms.Form):

#     #complete and test by saturday 
#     name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),required=True)
#     event_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Event date as DD/MM/YY'}), required=True)
#     event_time = forms.TimeField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Event Time as HH:MM:SS'}), required=True)
#     capacity = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'(Optional) Event capacity in integers'}), required=False)
#     fee = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'(Optional) Event fees in INR'}), required=False)
#     summary = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Event Summary'}), required=True)
#     invitees = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),queryset=User.objects.all(), required=True)
    
#     def clean_fee(self):
#         fee = self.cleaned_data.get('fee')

#         if fee<0:
#             raise forms.ValidationError("Fee can't be negative")
#         return fee

#     def clean_capacity(self):
#         capacity = self.cleaned_data.get('capacity')


#         if capacity <1:
#             raise forms.ValidationError("Capacity must be a positive integer")

#         return capacity

class EventCreatorForm(ModelForm):
    class Meta:
        model = models.Event
        fields =['name','fee','capacity','target_audience','date','time','tags','invitees_btech','invitees_mtech','invitees_phd','organisors','contact_info','summary','faq','comment_for_admin']


# EventFormSet = modelformset_factory(
#     Event,
#     fields =('name','fee','capacity','target_audience','date','time','tags','invitees_btech','invitees_mtech','invitees_phd','organisors','contact_info','summary','faq','comment_for_admin'),
#     extra = 1
# )

class PollCreatorForm(forms.Form):
    choices=[
        ('response_not_coming','Not Coming'),
        ('response_coming','Coming'),
        ('response_not_sure','Not Sure'),
    ]
    f_value=forms.ChoiceField(choices=choices)

    def save(self,event_id,poll,request):
        vote=Vote.objects.filter(vote_id=event_id,user_id=str(request.user))
        cleaned_data=self.cleaned_data.get('f_value')
        if vote:
            temp_data=vote[0].user_vote
        
            if (temp_data==1):
                poll.response_not_coming=poll.response_not_coming -1
            elif (temp_data==2):
                poll.response_coming=poll.response_coming - 1
            else :
                poll.response_not_sure=poll.response_not_sure -1 
        else :
            pass   
            
        if (cleaned_data=='response_not_coming'):
            poll.response_not_coming=poll.response_not_coming + 1 
        elif (cleaned_data=='response_coming'):
            poll.response_coming = poll.response_coming + 1
        else:
            poll.response_not_sure= poll.response_not_sure + 1
        poll.save()
        return cleaned_data

