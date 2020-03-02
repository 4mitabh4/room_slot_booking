from django.shortcuts import render,redirect
from manager.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import timedelta,datetime
from django.contrib.auth.models import User,auth,Group

def home(request):
  count=add.objects.filter(booked=False).count()
  room=add.objects.filter(booked=False).order_by('room_no')
  context={'count':count,'room':room}
  for x in room:
    x.date=datetime.now().date()+timedelta(days=x.days)

  return render(request,"home.html",context)


@login_required(login_url='user_login')
def profile(request):
    new_bookings = new_booking.objects.filter(customer=request.user)
    old_bookings = old_booking.objects.filter(customer=request.user)
    user = User.objects.get(id=request.user.id)
    username=user.username
    first_name = user.first_name
    last_name = user.last_name
    email = user.email
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
      
    return render(request, 'profile.html', context)

@login_required(login_url='user_login')  
def book(request, room_no):
  if request.method == 'POST':
    x = add.objects.get(room_no=room_no)
    y = new_booking.objects.create(new=x, customer=request.user)
    y.save()
    x.booked = True
    x.save()
    return redirect('profile')
  else:
    
    context={'room_no':room_no}
    return render(request, 'booking_confirm.html',context)

@login_required(login_url='user_login')  
def old_book(request, room_no):
  print(room_no)
  if request.method == 'POST':
    x = add.objects.get(room_no=room_no)
    z = new_booking.objects.get(new=x, customer=request.user)
    y = old_booking.objects.create(old=x, customer=request.user,time=z.booking_time)
    
    y.save()
    x.booked = False
    x.save()
    z.delete()
    return redirect('profile')
  else:
    
    context={'room_no':room_no}
    return render(request, 'delete_booking.html',context)

# function to grant access to manager only

def user_login(request):
    
    if request.user.is_authenticated:
      return redirect('home')
      
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
        return redirect('home')
      
      # if invalid credentials is given show message and redirect to the same page 
      else:
        messages.info(request,'invalid credentials')
        return redirect('user_login')

    else:
      return render(request, "login.html", {'act': user_login})
      
# register 
def register(request):
  if request.user.is_authenticated:
    return redirect('/')
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
        return redirect('register')

      # checks if the email is already taken 
      elif User.objects.filter(email=email).exists():
        messages.info(request,'email taken')
        return redirect('register')

      # create an account and redirect to login page 
      else:
        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
        user.save()
        group=Group.objects.get(name='customer')
        group.user_set.add(user)
        return redirect('user_login')
        
    else:
      messages.info(request,'password not matching')
      return redirect('register')
  
  
  else:
    return render(request,"register.html")

# logout 
def user_logout(request):
  auth.logout(request)
  return redirect('home')


