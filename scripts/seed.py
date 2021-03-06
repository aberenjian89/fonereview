import requests
from app.models import (
    Device,
    Rate
)
import random
from  django.contrib.auth.models import User




def run():
    User.objects.all().delete()
    Device.objects.all().delete()
    regular_user = User.objects.create(
        username = "Doe89",
        password = "Admin123",
    )
    admin_user = User.objects.create(
        username = "Salem89",
        password = "123Admin",
        is_superuser = True
    )    
    devices = requests.get(
          'https://fonoapi.freshpixl.com/v1/getlatest?token=75e16f79f00c963f2427b8651b176e70261baa6dac478d78')
    for device in devices.json():
        # device.setdefault('DeviceName', 'Not Available')
        name = device.get('DeviceName', 'Not Available')
        brand = device.get('Brand', 'Not Available')
        technology = device.get('technology', 'Not Available')
        gprs = device.get('gprs', 'Not Available')
        edge = device.get('edge', 'Not Available')
        announced = device.get('announced', 'Not Available')
        status = device.get('status', 'Not Available')
        weight = device.get('weight', 'Not Available')
        sim = device.get('sim', 'Not Available')
        device_type = device.get('type', 'Not Available')
        size = device.get('size', 'Not Available')
        resolution = device.get('resolution', 'Not Available')
        card_slot = device.get('card_slot', 'Not Available')
        loud_speaker = device.get('loud_speaker', 'Not Available')
        wlan = device.get('wlan', 'Not Available')
        bluetooth = device.get('bluetooth', 'Not Available')
        cpu = device.get('cpu', 'Not Available')
        battery_c = device.get('battery_c', 'Not Available')
        sensor = device.get('sensors', 'Not Available')
        gpu = device.get('gpu', 'Not Available')
        internal_memory = device.get('internal', 'Not Available')
        os = device.get('os', 'Not Available')
   
        # defaults = {
        #     'DeviceName': 'Not Available',
        #     'Brand': 'Not Available',
        #     'technology': 'Not Available',
        #     'gprs': 'Not Available',
        #     'edge': 'Not Available',
        #     'announced': 'Not Available',
        #     'status': 'Not Available',
        #     'weight': 'Not Available',
        #     'sim': 'Not Available',
        #     'type': 'Not Available',
        #     'size': 'Not Available',
        #     'resolution': 'Not Available',
        #     'card_slot': 'Not Available',
        #     'loud_speaker': 'Not Available',
        #     'wlan': 'Not Available',
        #     'bluetooth': 'Not Available',
        #     'cpu': 'Not Available',
        #     'battery_c': 'Not Available',
        #     'sensors': 'Not Available',
        #     'gpu': 'Not Available',
        #     'internal': 'Not Available',
        #     'os': 'Not Available',

        #     # ...
        # }
        # defaults.update(device)
        # Device.objects.create(
        #     **defaults
        # )

        # if 'DeviceName' in device:
        #     name = device['DeviceName']
        # else:
        #     name = 'Not Avaliable'

        # if 'Brand' in device:
        #     brand = device['Brand']
        # else:
        #     brand = 'Not Avaliable'
        
        # if 'technology' in device:
        #     technology = device['technology']
        # else:
        #     technology = 'Not Avaliable'

        # if 'gprs' in device:
        #     gprs = device['gprs']
        # else:
        #     gprs = 'Not Avaliable'
        
        # if 'edge' in device:
        #     edge = device['edge']
        # else:
        #     edge = 'Not Avaliable'
        
        # if 'announced' in device:
        #     announced = device['announced']
        # else:
        #     announced = 'Not Avaliable'
        
        # if 'status' in device:
        #     status = device['status']
        # else:
        #     status = 'Not Avaliable'
        
        # if 'weight' in device:
        #     weight = device['weight']
        # else:
        #     weight = 'Not Avaliable'
        
        # if 'sim' in device:
        #     sim = device['sim']
        # else:
        #     sim = 'Not Avaliable'
        
        # if 'type' in device:
        #     device_type = device['type']
        # else:
        #     device_type = 'Not Avaliable'
        
        # if 'size' in device:
        #     size = device['size']
        # else:
        #     size = 'Not Avaliable'
        
        # if 'resolution' in device:
        #     resolution = device['resolution']
        # else:
        #     resolution = 'Not Avaliable'
        
        # if 'card_slot' in device:
        #     card_slot = device['card_slot']
        # else:
        #     card_slot = 'Not Avaliable'
        
        # if 'loudspeaker_' in device:
        #     loud_speaker = device['loudspeaker_']
        # else:
        #     loud_speaker = 'Not Avaliable'
        
        # if 'wlan' in device:
        #     wlan = device['wlan']
        # else:
        #     wlan = 'Not Avaliable'

        # if 'bluetooth' in device:
        #     bluetooth = device['bluetooth']
        # else:
        #     bluetooth = 'Not Avaliable'

        # if 'cpu' in device:
        #     cpu = device['cpu']
        # else:
        #     cpu = 'Not Avaliable'

        # if 'battery_c' in device:
        #     battery_c = device['battery_c']
        # else:
        #     battery_c = 'Not Avaliable'

        # if 'sensors' in device:
        #     sensor = device['sensors']
        # else:
        #     sensor = 'Not Avaliable'

        # if 'gpu' in device:
        #     gpu = device['gpu']
        # else:
        #     gpu = 'Not Avaliable'

        # if 'internal' in device:
        #     internal_memory = device['internal']
        # else:
        #     internal_memory = 'Not Avaliable'

        # if 'os' in device:
        #     os = device['os']
        # else:
        #     os = 'Not Avaliable'


        rate = (random.randrange(10,50))/10
        dev=Device.objects.create(
            name = name,
            brand = brand,
            technology = technology,
            gprs = gprs,
            edge = edge,
            announced = announced,
            status = status,
            weight = weight,
            sim = sim, 
            device_type = device_type, 
            size = size,
            resolution = resolution,
            card_slot = card_slot,
            loud_speaker = loud_speaker,
            wlan = wlan, 
            bluetooth = bluetooth,
            cpu = cpu, 
            battery_c = battery_c,
            sensor = sensor,
            gpu = gpu,
            internal_memory = internal_memory,
            os = os, 
            total_rating = rate,
        )   
        Rate.objects.create(
            device = dev,
            user = admin_user,
            rating = int(rate),
            user_rate_type = 2
        )



        
        

    print("Done Seeding!....")
