from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class add(models.Model):
  room_no=models.IntegerField(null=True,unique=True)
  days=models.IntegerField(null=True)
  date=models.DateField(auto_now=True)
  check_in_time=models.TimeField(null=True)
  check_out_time = models.TimeField(null=True)
  booked=models.BooleanField(default=False)

  def __str__(self):
    return ('room no : ' + str(self.room_no))



# new bookings 
class new_booking(models.Model):
  new = models.ForeignKey(add, on_delete=models.CASCADE, null=True)
  customer = models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)
  booking_time=models.DateTimeField(auto_now_add=True,null=True)
  def __str__(self):
    return (str(self.new))


class old_booking(models.Model):
  old = models.ForeignKey(add, on_delete=models.CASCADE, null=True)
  customer = models.ForeignKey(User,null=True, blank=True, on_delete=models.SET_NULL)
  time=models.DateTimeField(null=True)
  def __str__(self):
    return (str(self.new))