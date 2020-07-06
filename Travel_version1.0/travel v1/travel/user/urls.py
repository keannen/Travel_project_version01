from django.urls import path
from user import views

urlpatterns = [
    path('/test', views.test),
    path('/test_register', views.test_register),
    path('/test_uplodepic', views.test_uploadpic)
]
