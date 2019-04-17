"""csea_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage, name='loginPage'),
    path('register/', views.registerPage, name='register'),
    path('api/login/', views.api_login, name='api_login'),
    path('api/signup/', views.api_signup, name='api_signup'),
    path('api/registerevent/', views.api_registerevent, name='api_registerevent'),
    # path('api/eventdetails/', views.api_eventdetails, name='api_eventdetails'),
    path('api/feedbackapp/', views.api_feedbackapp, name='api_feedbackapp'),
    path('api/', views.create_event, name='creator')
    
]
