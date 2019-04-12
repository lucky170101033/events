from django import forms
from django.contrib.auth import get_user_model
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
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Full Name'}),required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Your college email (@iitg.ac.in)'
        }), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'select a username'
        }), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your password'}), required=True)
    confirm_password = forms.CharField( label = 'Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your password (again)'}), required=True)


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

class EventCreatorForm(forms.Form):

    #complete and test by saturday 
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Event Name'}),required=True)
    event_date = forms.DateField( required=True)
    event_time = forms.TimeField( required=True)
    capacity = forms.PositiveIntegerField()
    fee = forms.PositiveIntegerField()
