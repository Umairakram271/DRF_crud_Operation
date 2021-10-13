from django.contrib import admin
from django.urls import path, include
from crudapp import views

urlpatterns=[
    path('register/', views.Student_create, name="register/"),
    path('register/<int:pk>/', views.Student_create),
    path('subject/', views.Subject_create, name="subject/"),
    path('subject/<int:pk>/', views.Subject_create),

]