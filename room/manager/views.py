from django.shortcuts import render,redirect
from .forms import AddForm,UpdateForm
from .models import add
from django.contrib.auth.models import User,auth,Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# function for admin accesss
def group_access(request):
  if request.user.groups.exists():
    if request.user.groups.filter(name='manager'):
      return True
    if request.user.groups.filter(name='customer'):
      return False
    
# function for error check
def error_check(request):
      check_in_date=[int(x) for x in request.POST['check_in_date'].split('-')]
      check_out_date=[int(x) for x in request.POST['check_out_date'].split('-')]
      
      check_in_time=[int(x) for x in request.POST['check_in_time'].split(':')]
      check_out_time=[int(x) for x in request.POST['check_out_time'].split(':')]

      if int(request.POST['days'])<1:
        messages.info(request,'invalid days  given')
        return False

      elif check_in_date[0]>check_out_date[0]:
        messages.info(request,'invalid checkin and checkout years_field given')
        return False

      elif check_in_date[0]==check_out_date[0] and check_in_date[1]>check_out_date[1]:
        messages.info(request,'invalid checkin and checkout months_field given')
        return False
      
      elif check_in_date[0]==check_out_date[0] and check_in_date[1]==check_out_date[1] \
      and check_in_date[2]>check_out_date[2]:
        messages.info(request,'invalid checkin and checkout days_field given')
        return False

      elif check_in_date[0]==check_out_date[0] and check_in_date[1]==check_out_date[1] \
      and check_in_date[2]==check_out_date[2] and check_in_time[0]>check_out_time[0]:
        messages.info(request,'invalid checkin and checkout time(hour)_field given')
        return False

      elif check_in_date[0]==check_out_date[0] and check_in_date[1]==check_out_date[1] \
      and check_in_date[2]==check_out_date[2] and check_in_time[0]==check_out_time[0] \
      and  check_in_time[1]>check_out_time[1]:
        messages.info(request,'invalid checkin and checkout time(min)_field given')
        return False
      
      else:
        return True


# Create your views here.
@login_required(login_url='manager_login')
def add_x(request):
  # manager accesss
  if group_access(request)==True:
    form=AddForm()
    if request.method=='POST':
      form=AddForm(request.POST)
      if form.is_valid():
        room_no=request.POST['room_no']
        if add.objects.filter(room_no=room_no).exists():
          messages.info(request,'room no already allocated')
        elif int(room_no)<1:
          messages.info(request,'invalid room no given')
        elif error_check(request):
          form.save()
          messages.info(request,'data saved')
          return redirect('room_data')
      else:
        print('form not valid')
    
    context={'form':form}
    return render(request,'add.html',context)
  
  else:
    return redirect('/')



# rooms
@login_required(login_url='manager_login')
def rooms_data(request):
  # manager accesss
  if group_access(request) == True:
    room=add.objects.all().order_by('room_no')
    context={'room':room}
    return render(request,'rooms_data.html',context)
    
  else:
    messages.info(request,'login with manager account')
    return redirect('manager_logout')
  

# update 
@login_required(login_url='manager_login')
def update(request,room_no):
  # manager accesss
  if group_access(request)==True:
    up=add.objects.get(room_no=room_no)
    form_before=UpdateForm(instance=up)
    if request.method=='POST':
      form_after=UpdateForm(request.POST,instance=up)
      if form_after.is_valid():
        if form_after.has_changed()==False:
          messages.info(request,'no change detected')
        elif error_check(request):
          form_after.save()
          messages.info(request,'Successfully Updated')
          return redirect('room_data')
    context={'form':form_before}

    return render(request,'update.html',context)
  
  else:
    return redirect('/')

@login_required(login_url='manager_login')
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


def sign_in_up(request):
  return render(request,'manager.html')


  
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