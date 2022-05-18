from django.contrib import admin
from django.urls import path
#import myapp.views
from myapp import views

urlpatterns = [
    path("", views.home, name="hello word"),
    path("test/", views.test)
]
