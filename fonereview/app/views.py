from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
import requests
from django.http import HttpResponse
from .models import Device
# List of phones for featured listing


def get_device_info(request):
    data = requests.get('https://fonoapi.freshpixl.com/v1/getlatest?token=75e16f79f00c963f2427b8651b176e70261baa6dac478d78')
    devices = data.json()
    return render(request,'pages/all_device.html',{'devices': devices})


def fonereview_homepage(request):
    featured_phones = Device.objects.all()[:15]
    
    context = {

        'featured_phones': featured_phones,
        'title': 'Welcome to Fone Review Site',
        'logo': 'static/app/images/logo_bg.jpg'

    }
    return render(request, 'pages/recent_phone.html', context)

def fonereview_device_single(request,device_id):
    if request.method == 'POST':
        pass
    else:
        device = Device.objects.get(id=device_id)
        return render(request,'pages/single.html',{'device': device})

def fonereview_about(request):
    context = {
        'title': 'Fone Review - About us',
        'logo': 'static/app/images/logo_bg.jpg'

    }
    return render(request, 'pages/logout.html', context)


def fonereview_contact(request):
    context = {
        'title': 'Fone Review - Contact the Team',
        'logo': 'static/app/images/logo_bg.jpg'

    }
    return render(request, 'pages/logout.html', context)
