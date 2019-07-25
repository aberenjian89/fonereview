from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Device(models.Model):
  name = models.CharField(max_length=255)
  brand = models.CharField(max_length=255)
  technology = models.CharField(max_length=255)
  gprs = models.CharField(max_length=255)
  edge = models.CharField(max_length=255)
  announced = models.CharField(max_length=255)
  status = models.CharField(max_length=255)
  weight = models.CharField(max_length=255)
  sim = models.CharField(max_length=255)
  device_type = models.CharField(max_length=255)
  size = models.CharField(max_length=255)
  resolution = models.CharField(max_length=255)
  card_slot = models.CharField(max_length=255)
  loud_speaker = models.CharField(max_length=255)
  wlan = models.CharField(max_length=255)
  bluetooth = models.CharField(max_length=255)
  cpu = models.CharField(max_length=255)
  battery_c = models.CharField(max_length=255)
  sensor = models.CharField(max_length=255)
  gpu = models.CharField(max_length=255)
  internal_memory = models.CharField(max_length=255)
  os = models.CharField(max_length=255)
  image = models.FileField(upload_to="device_images/",null=True,blank=True)
  total_rating = models.DecimalField(max_digits=2,decimal_places=1,null=True,blank=True)
  #change the var to 255

  def __str__(self):
    return self.name


class Rate(models.Model):
  # User Rate Type
    # 1 : Admin Or SuperAdmin
    # 2 : Regular User
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

  created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
  description = models.CharField(max_length=255)

  user = models.ForeignKey(
    User,
    on_delete = models.CASCADE
  )

  device = models.ForeignKey(
    Device,
    on_delete = models.CASCADE
  )

  created = models.DateTimeField(auto_now_add=True)


