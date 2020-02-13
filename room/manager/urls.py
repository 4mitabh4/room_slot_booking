from django.urls import path
from . import views

urlpatterns=[
  path('',views.sign_in_up,name='manager_signin'),
  path('add',views.add_x,name='add'),
  path('rooms',views.rooms_data,name='room_data'),
  path('update/<int:room_no>/',views.update,name='update_data'),
  path('delete/<int:room_no>/',views.delete,name='delete_data'),
  path('login',views.manager_login,name='manager_login'),
  path('register',views.manager_register,name='manager_register'),
  path('logout',views.manager_logout,name='manager_logout'),
]