from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


# login
def login(request):

  # if request is of post type 
  if request.method=='POST':

    # take username and password 
    username=request.POST['username']
    password=request.POST['password']

    # authenticate username and password 
    user=auth.authenticate(username=username,password=password)

    # if username and login is valid 
    if user is not None:
      auth.login(request,user)

      # redirect to home page
      return redirect('/')
    
    # if invalid credentials is given show message and redirect to the same page 
    else:
      messages.info(request,'invalid credentials')
      return redirect('login')

  else:
    return render(request,"login.html")




# register 
def register(request):

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
        return redirect('login')
        
    else:
      messages.info(request,'password not matching')
      return redirect('register')
  
  
  else:
    return render(request,"register.html")

# logout
def logout(request):
  auth.logout(request)
  return redirect('/')
