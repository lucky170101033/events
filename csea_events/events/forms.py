from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from . import models
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
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

        if queryset.exists():
            raise forms.ValidationError("Email already active")



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
        fields =['name','fee','capacity','target_audience','date','time','tags','invitees_btech','invitees_mtech','invitees_phd','organisors','contact_info','summary','faq']