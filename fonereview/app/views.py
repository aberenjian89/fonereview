from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
import requests

def home(request):
    return render(request,'base.html',{'user': request.user})


def get_device_info(request):
    data = requests.get('https://fonoapi.freshpixl.com/v1/getlatest?token=75e16f79f00c963f2427b8651b176e70261baa6dac478d78')
    devices = data.json()


    return render(request,'pages/all_device.html',{'devices': devices})
