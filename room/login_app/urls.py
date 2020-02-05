from django.urls import path
from . import views

urlpatterns=[
  # searches for login function in views 
  path('login',views.login,name='login'),

  # searches for register function in views 
  path('register',views.register,name='register'),

  # searches for logout function in views 
  path('logout',views.logout,name='logout'),
]