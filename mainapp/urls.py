from django.urls import path
from .import views
urlpatterns =[
    path("", views.main, ),
    path('signup', views.signup),
    path('login', views.login),
    path('myaccount', views.myaccount),
    path('home', views.home),
    path('employees', views.employees),
    path('register', views.register),
    path('aboutus', views.aboutus),
    path('emp_home', views.emp_home),
    path('newrequest', views.newrequest),
    path('done', views.done),
    path('cancel', views.cancel)
]