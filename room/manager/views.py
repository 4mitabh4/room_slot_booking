from django.shortcuts import render,redirect
from .forms import AddForm,UpdateForm
from .models import add
from django.contrib import messages


# Create your views here.
def add_x(request):
  
  form=AddForm()
  if request.method=='POST':
    form=AddForm(request.POST)
    if form.is_valid():
      room_no=request.POST['room_no']
      if add.objects.filter(room_no=room_no).exists():
        print('already exist')
        messages.info(request,'room no already allocated')
        # redirect('add')
      else:
        form.save()
        messages.info(request,'data saved')
        return redirect('room_data')
    else:
      print('form not valid')
  
  context={'form':form}
  return render(request,'add.html',context)



# rooms
def rooms_data(request):
  room=add.objects.all()
  context={'room':room}
  return render(request,'rooms_data.html',context)

# update 
def update(request,room_no):
  up=add.objects.get(room_no=room_no)
  form_before=UpdateForm(instance=up)
  if request.method=='POST':
    form_after=UpdateForm(request.POST,instance=up)
    if form_after.is_valid():
      if form_after.has_changed()==False:
        messages.info(request,'no change detected')
      else:
        form_after.save()
        messages.info(request,'Successfully Updated')
        return redirect('room_data')
  context={'form':form_before}

  return render(request,'update.html',context)


def delete(request,room_no):
  up=add.objects.get(room_no=room_no)
  if request.method=='POST':
    up.delete()
    messages.info(request,'Successfully deleted')
    return redirect('room_data')
  context={'up':up}
  return render(request,'delete.html',context)