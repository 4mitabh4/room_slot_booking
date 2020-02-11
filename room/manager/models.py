from django.db import models

# Create your models here.
class add(models.Model):
  room_no=models.IntegerField(null=True)
  days=models.IntegerField(null=True)
  check_in_date=models.DateField(null=True)
  check_in_time=models.TimeField(null=True)
  check_out_date=models.DateField(null=True)
  check_out_time=models.TimeField(null=True)

  def __str__(self):
    return ('room no : '+str(self.room_no))


