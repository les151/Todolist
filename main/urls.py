from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'main'

urlpatterns = [
    path('sign_up', views.sign_up, name = 'sign_up'),
    path('sign_in', views.sign_in, name = 'sign_in'),
    path('To_Do_List', views.To_Do_List_page, name = 'login'),
    path('add_task', views.add_task, name = 'add_task'),
    path('delete-task/<int:task_id>/', views.delete_task, name = 'delete_task'),
    path('edit-task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('update-task-status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]