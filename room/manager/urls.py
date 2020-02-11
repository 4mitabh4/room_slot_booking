from django.urls import path
from . import views

urlpatterns=[

  path('add',views.add_x,name='add'),
  path('rooms',views.rooms_data,name='room_data'),
  path('update/<int:room_no>/',views.update,name='update_data'),
  path('delete/<int:room_no>/',views.delete,name='delete_data'),
]