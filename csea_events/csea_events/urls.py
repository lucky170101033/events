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
    path('home/',views.home_page, name='home_page'),
    path('register/', views.registerPage, name='register'),
    path('api/', views.api_resp, name='api_resp'),
    path('create/', views.create_event, name='create_event'),
    path('logout/', views.logout_user, name='logout'),
    path('event/<uuid:event_id>/',views.poll_view,name='polling'),
    path('event/', views.poll_view, name='poll'),
    path('change_passswd/',views.change_password,name='change_passwd'),
    # path('admin-page/',views.admin_view, name='admin-page'),
    path('profile/',views.profile_view,name='profile'),
    # path('poll/',views.poll_count_view,name='poll_count'),
    path('poll/<uuid:event_id>/',views.poll_count_view,name='poll_count'),
    path('poll/<uuid:event_id>/vote',views.poll_vote,name='poll_count_vote'),
    

    
]
