from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Device(models.Model):
  name = models.CharField(max_length=50)
  brand = models.CharField(max_length=40)
  technology = models.CharField(max_length=100)
  gprs = models.BooleanField()
  edge = models.BooleanField()
  announced = models.BooleanField()
  status = models.CharField(max_length=80)
  weight = models.CharField(max_length=20)
  sim = models.CharField(max_length=50)
  device_type = models.CharField(max_length=60)
  size = models.CharField(max_length=30)
  resolution = models.CharField(max_length=50)
  card_slot = models.BooleanField()
  loud_speaker = models.BooleanField()
  wlan = models.CharField(max_length=100)
  bluetooth = models.CharField(max_length=100)
  cpu = models.CharField(max_length=100)
  battery_c = models.CharField(max_length=100)
  sensor = models.CharField(max_length=100)
  cup = models.CharField(max_length=100)
  internal_memory = models.CharField(max_length=100)
  os = models.CharField(max_length=100)
  image = models.FileField(upload_to="device_images/",null=True,blank=True)

class Comment(models.Model):
  description = models.CharField(max_length=160)

  user = models.ForeignKey(
    User,
    on_delete = models.CASCADE
  )

  device = models.ForeignKey(
    Device,
    on_delete = models.CASCADE
  )
class Rate(models.Model):
  user_rate_type = models.IntegerField()
  rating = models.IntegerField()

  user = models.ForeignKey(
    User,
    on_delete = models.CASCADE
  )

  device = models.ForeignKey(
    Device,
    on_delete = models.CASCADE
  )
