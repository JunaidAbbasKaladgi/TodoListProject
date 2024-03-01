from django.contrib import admin
from django.urls import path
from TodoListApp import views

urlpatterns = [
    path('', views.TodoList,name="TodoList"),
    path('Tasks/', views.Tasks,name="Tasks"),
     path('update/<int:id>', views.update_Task,name="update_Task"),
    path('delete/<int:id>', views.delete_Task,name="delete_Task"),  
]