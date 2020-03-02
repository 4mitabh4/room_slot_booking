from django.urls import path
from . import views

urlpatterns=[
  # different urls
  path('',views.home,name='home'),
  path('profile', views.profile, name='profile'),
  path('book/<int:room_no>/', views.book, name='user_book'),
  path('login', views.user_login, name='user_login'),
  path('register', views.register, name='register'),
  path('delete/<int:room_no>/', views.old_book, name='book_delete'),
  path('logout_user',views.user_logout,name='user_logout'),
]