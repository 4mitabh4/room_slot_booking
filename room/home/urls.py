from django.urls import path
from . import views

urlpatterns=[
  # searches for home function in views 
  path('',views.home,name='home')
]