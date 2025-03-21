from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main'),
    path('sign_in', views.sign_in_page, name = 'sign_in')
]
