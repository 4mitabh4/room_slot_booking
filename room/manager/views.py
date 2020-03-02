from django.shortcuts import render,redirect
from .forms import AddForm,UpdateForm
from .models import *
from django.contrib.auth.models import User,auth,Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import timedelta


# function for managerial accesss
def group_access(request):
  if request.user.groups.exists():
    if request.user.groups.filter(name='manager'):
      return True
    if request.user.groups.filter(name='customer'):
      return False
    
# function for error check
def error_check(request):
      # stores date in list format 
      # check_in_date=[int(x) for x in request.POST['check_in_date'].split('-')]
      # check_out_date=[int(x) for x in request.POST['check_out_date'].split('-')]
      
      # check_in_time=[int(x) for x in request.POST['check_in_time'].split(':')]
      # check_out_time=[int(x) for x in request.POST['check_out_time'].split(':')]

      # check if the days is less than 1 days 
      if int(request.POST['days'])<1:
        messages.info(request,'invalid days  given')
        return False

      # checks if the check_in_date(year) is greater than check_out_date(year)
      # elif check_in_date[0]>check_out_date[0]:
      #   messages.info(request,'invalid checkin and checkout years_field given')
      #   return False

      # checks if the check_in_date(month) is greater than check_out_date(month)
      # elif check_in_date[0]==check_out_date[0] and check_in_date[1]>check_out_date[1]:
      #   messages.info(request,'invalid checkin and checkout months_field given')
      #   return False
      
      # checks if the check_in_date(days) is greater than check_out_date(days)
      # elif check_in_date[0]==check_out_date[0] and check_in_date[1]==check_out_date[1] \
      # and check_in_date[2]>check_out_date[2]:
      #   messages.info(request,'invalid checkin and checkout days_field given')
      #   return False

      # checks if the check_in_time(hour) is greater than check_out_time(hour)
      # elif check_in_date[0]==check_out_date[0] and check_in_date[1]==check_out_date[1] \
      # and check_in_date[2]==check_out_date[2] and check_in_time[0]>check_out_time[0]:
      #   messages.info(request,'invalid checkin and checkout time(hour)_field given')
      #   return False

      # checks if the check_in_time(min) is greater than check_out_time(min)
      # elif check_in_date[0]==check_out_date[0] and check_in_date[1]==check_out_date[1] \
      # and check_in_date[2]==check_out_date[2] and check_in_time[0]==check_out_time[0] \
      # and  check_in_time[1]>check_out_time[1]:
      #   messages.info(request,'invalid checkin and checkout time(min)_field given')
      #   return False
      
      else:
        return True



#decorator to ensure that login is done
@login_required(login_url='manager_login')

# function to add new room 
def add_x(request):
  # to ensure only manager can add data
  if group_access(request)==True:
    # create form 
    form=AddForm()
    if request.method=='POST':
      form=AddForm(request.POST)
      if form.is_valid():

        # checks if room no is already allocated
        room_no=request.POST['room_no']
        if add.objects.filter(room_no=room_no).exists():
          messages.info(request,'room no already allocated')

          # checks the validity of room no 
        elif int(room_no)<1:
          messages.info(request,'invalid room no given')

          # if no error is found then add new room info 
        elif error_check(request):
          form.save()
          messages.info(request,'data saved')
          return redirect('room_data')
      else:
        print('form not valid')
    

    # if request is of get type 
    else:
      context={'form':form}
      return render(request,'add.html',context)
  
  else:
    return redirect('room_data')



#decorator to ensure that login is done
@login_required(login_url='manager_login')

# function to show the room info 
def rooms_data(request):
  # manager accesss
  if group_access(request) == True:
    room=add.objects.all().order_by('room_no')
    context={'room':room}
    return render(request,'rooms_data.html',context)
    
  else:
    messages.info(request,'login with manager account')
    return redirect('manager_logout')
  


@login_required(login_url='manager_login')

# function to update room info 
def update(request,room_no):
  # manager accesss
  if group_access(request)==True:
    up=add.objects.get(room_no=room_no)
    form_before=UpdateForm(instance=up)
    if request.method=='POST':
      form_after=UpdateForm(request.POST,instance=up)
      if form_after.is_valid():

        # to make sure change is made 
        if form_after.has_changed()==False:
          messages.info(request,'no change detected')

        # if no error is found then update 
        elif error_check(request):
          form_after.save()
          messages.info(request,'Successfully Updated')
          return redirect('room_data')


    context={'form':form_before}
    return render(request,'update.html',context)
  
  else:
    return redirect('room_data')

@login_required(login_url='manager_login')

# function to delete room info 
def delete(request,room_no):
  # manager accesss
  if group_access(request)==True:
    up=add.objects.get(room_no=room_no)
    if request.method=='POST':
      up.delete()
      messages.info(request,'Successfully deleted')
      return redirect('room_data')
    context={'up':up}
    return render(request,'delete.html',context)
  
  else:
    return redirect('/')


# function to render manager home page
def sign_in_up(request):
  return render(request,'manager.html')


# function to grant access to manager only 
def manager_login(request):
    
    if request.user.is_authenticated:
      return redirect('room_data')
      
    # if request is of post type 
    if request.method=='POST':
      
      username=request.POST['username']
      password=request.POST['password']

      # authenticate username and password 
      user=auth.authenticate(username=username,password=password)

      # if username and login is valid 
      
      if user is not None :
        auth.login(request,user)

        # redirect to admin dashboard
        return redirect('room_data')
      
      # if invalid credentials is given show message and redirect to the same page 
      else:
        messages.info(request,'invalid credentials')
        return redirect('manager_login')

    else:
      return render(request,"login.html",{'act':manager_login})


# to create new manager account 
def manager_register(request):
  if request.user.is_authenticated:
    return redirect('room_data')
  # if request is of post type
  if request.method=='POST':

    # take the necessay fiels in its respective variables 

    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    username=request.POST['username']
    email=request.POST['email']
    password1=request.POST['password1']
    password2=request.POST['password2']


    # if password and confirm password is equal 
    if password1==password2:
      # checks if username is already taken 
      if User.objects.filter(username=username).exists():
        messages.info(request,'username taken')
        return redirect('manager_register')

      # checks if the email is already taken 
      elif User.objects.filter(email=email).exists():
        messages.info(request,'email taken')
        return redirect('manager_register')

      # create an account and redirect to login page 
      else:
        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
        user.save()
        group=Group.objects.get(name='manager')
        group.user_set.add(user)
        return redirect('manager_login')
        
    else:
      messages.info(request,'password not matching')
      return redirect('manager_register')
  
  
  else:
    return render(request,"register.html")


# logout 
def manager_logout(request):
  auth.logout(request)
  return redirect('manager_signin')

# booked rooms
def booked_rooms(request):
  booking = new_booking.objects.all()
  context = {'booking': booking}
  return render(request, "booked_rooms.html", context)


@login_required(login_url='manager_login')  
def user_profile(request,id):
    new_bookings = new_booking.objects.filter(customer=id)
    old_bookings = old_booking.objects.filter(customer=id)
    user = User.objects.get(id=id)

    username=user.username
    first_name = user.first_name
    last_name = user.last_name
    email=user.email
    context = {'new_bookings': new_bookings,
    'old_bookings': old_bookings,
    'username': username,
    'first_name': first_name,
    'last_name': last_name,
    'email':email,
    }
    for x in new_bookings:
      x.new.date = x.booking_time.date() + timedelta(days=x.new.days)
    for y in old_bookings:
      y.old.date = y.time.date() + timedelta(days=y.old.days)
    return render(request, 'user_info.html', context)