from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Profile
class LoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your @iitg email'
    }), required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your password'}), required=True)

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

department_values = (
        ('cse', 'Computer Science & Engineering'),
        ('ece', 'Electronics & Communication Engineering'),
        ('me', 'Mechanical Engineering'),
        ('ce', 'Civil Engineering'),
        ('dd', 'Design'),
        ('bsbe', 'Biosciences & Bioengineering'),
        ('cl', 'Chemical Engineering'),
        ('cst', 'Chemical Science & Technology'),
        ('eee', 'Electronics & Electrical Engineering'),
        ('ma', 'Mathematics & Computing'),
        ('ph', 'Engineering Physics'),
        ('rt', 'Rural Technology'),
        ('hss', 'Humanities & Social Sciences'),
        ('enc', 'Centre for Energy'),
        ('env', 'Centre for Environment'),
        ('nt', 'Centre for Nanotechnology'),
        ('lst', 'Centre for Linguistic Science & Technology')
    )
program_values = (
        ('btech', 'BTech'),
        ('mtech', 'MTech'),
        ('phd', 'PhD'),
        ('msc', 'MSc'),
        ('msr', 'MS-R'),
        ('ma', 'MA'),
        ('bdes', 'BDes'),
        ('mdes', 'MDes')
    )

class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
                           required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your @iitg email'
    }), required=True)
    department = forms.CharField(widget=forms.Select(choices=department_values,attrs={'class': 'form-control'}),required=True)
    program = forms.CharField(widget=forms.Select(choices=program_values, attrs={'class': 'form-control'}),
                                 required=True)
    roll_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your Roll Number'}),
                           required=True)
    phone_no = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
                           required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your password'}), required=True)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Your password (again)'}), required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(1,email)
        queryset = User.objects.filter(email=email)


        if queryset.exists():
            print(1)
            raise forms.ValidationError("Email already active")

    def clean_confirm_password(self):
        passw = self.cleaned_data.get('confirm_password')
        passw_orig = self.cleaned_data.get('password')

        if passw != passw_orig:
            raise forms.ValidationError('Both passwords must match')

        return passw