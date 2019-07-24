from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
import requests
from django.contrib.auth.decorators import login_required
from .models import Device
from .models import Comment
from .models import Rate
from django import forms
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


@login_required(login_url='/sign-in/')
def fonereview_device_single(request,device_id):
    if request.method == 'POST' and  request.user.is_authenticated :
        description = request.POST['description']
        print(request.POST['rate'])
        rate = int(request.POST['rate'])
        device = Device.objects.get(id=device_id)
        user = request.user
        if user.is_superuser:
            user_type = 1
        else:
            user_type = 2
        Rate.objects.create(
            user_rate_type = user_type,
            rating = int(rate),
            device = device,
            user = user,
        )

        Comment.objects.create(
            description = description,
            device = device,
            user = user
        )
        get_over_all_rate(device)

        ctx = {
            'device': device,
            'comment': Comment.objects.filter(device=device).order_by('-created'),
        }

        return render(request, 'pages/single.html', ctx)
    else:
        device = Device.objects.get(id=device_id)
        device_comment = Comment.objects.filter(device=device)
        ctx = {
            'device': device,
            'comment': Comment.objects.filter(device=device).order_by('-created'),
        }
        return render(request,'pages/single.html',ctx)

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


def get_over_all_rate(device):
    device_rates = Rate.objects.filter(device=device)
    sum = 0
    for rate in device_rates:
        sum += rate.rating
    device.total_rating = sum/len(device_rates)
    device.save()

