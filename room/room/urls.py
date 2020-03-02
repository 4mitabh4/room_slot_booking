
from django.contrib import admin
from django.urls import path,include

admin.site.site_header='admin site'
admin.site.site_title='admin login'

urlpatterns = [
    # for admin site 
    path('admin/', admin.site.urls),

    # searches for urls file in home app 
    path('',include('user.urls')),

    path('manager/',include('manager.urls')),
]
