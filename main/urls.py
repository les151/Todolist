from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'main'

urlpatterns = [
    path('sign_up', views.sign_up, name = 'sign_up'),
    path('sign_in', views.sign_in, name = 'sign_in'),
    path('To_Do_List', views.To_Do_List_page, name = 'login')
]