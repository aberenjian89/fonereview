from django.shortcuts import render
from django.http import HttpResponse

# List of phones for featured listing

featured_phones = [
    {
    'phone_id': '001',
    'type': 'Apple iphone',
    'model': 'Xs',
    'os': 'ios',
    'description': 'The iPhone XS display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 5.85 inches diagonally (actual viewable area is less). iPhone XS and iPhone XS Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529 (maximum depth of 2 meters up to 30 minutes).',
    'date_released': '2019',
    'rating': '4.8',
    'number_of_reviews': '10',
    'image': '/static/images/image_1.jpg'
    

    },
    {
    'phone_id': '002',
    'type': 'Samsung Galaxy 10',
    'model': 'S10',
    'os': 'Android',
    'description': 'The Samsung Galaxy S10 is a fantastic phone in almost every department: performance, design, camera capabilities, the features included, and so on. Even in the areas where it doesnt quite excel – battery life and software – its still a strong device. Its easy to recommend the S10 to anyone looking for a new phone.',
    'date_released': '2018',
    'rating': '4.6',
    'number_of_reviews': '7',
    'image': '/static/images/image_2.jpg'
    }
    ,
    {
    'phone_id': '003',
    'type': 'LG G3',
    'model': 'G3',
    'os': 'Android',
    'description': 'It seems as though LG is not about to stop putting its phone buttons on the rear anytime soon. The brand-new G3 flagship might be gorgeous from every angle, but this one design touch will affect how you use this phone, and might be the only thing that puts you off about it. Otherwise, the specs are phenomenal, with the insanely crisp 5.5-inch QHD 1440x2560-pixel screen taking centre stage. The Snapdragon 801 processor and laser auto-focus camera dont hurt either. Performance is great, and LG throws in loads of software features including ways to multi-task and make use of the screen.',
    'date_released': '2017',
    'rating': '4.3',
    'number_of_reviews': '5',
    'image': '/static/images/image_3.jpg'
    }
]


def fonereview_homepage(request):
    context = {
        
        'featured_phones': featured_phones,
        'title': 'Welcome to Fone Review Site',
        'logo': '/static/images/logo_bg.jpg'

    }
    return render(request, 'index.html', context)

def fonereview_register(request):
    context = {
        'title': 'Fone Review - Register - New User',
        'logo': '/static/images/logo_bg.jpg'

    }
    return render(request, 'register.html', context)

def fonereview_login(request):
    context = {
        'title': 'Fone Review - Login for Existing Users',
        'logo': '/static/images/logo_bg.jpg',
        'icon': '/static/images/usericon.svg'

    }
    return render(request, 'login.html', context)

def fonereview_logout(request):
    context = {
        'title': 'Fone Review - Thank you for visiting',
        'logo':'/static/images/logo_bg.jpg'

    }
    return render(request, 'logout.html', context)
def fonereview_about(request):
    context = {
        'title': 'Fone Review - About us',
        'header_text': 'About Us',
        'logo':'/static/images/logo_bg.jpg',
        'about_image': '/static/images/about.png',
        'team': 'Ali, Matin, Pradeep & Nick'
    }
    return render(request, 'about.html', context)
def fonereview_contact(request):
    context = {
        'title': 'Fone Review - Contact the Team',
        'logo':'/static/images/logo_bg.jpg',
        'header_text': 'Contact the Fone Review Team'

    }
    return render(request, 'contact.html', context)
def fonereview_phone(request):
    context = {
        'title': 'Phone Specs and Review',
        'logo':'/static/images/logo_bg.jpg',
        'header_text': 'Phone Review Page',
        'phone_id': '001',
        'type': 'Apple iphone',
        'model': 'Xs',
        'os': 'ios',
        'description': 'The iPhone XS display has rounded corners that follow a beautiful curved design, and these corners are within a standard rectangle. When measured as a standard rectangular shape, the screen is 5.85 inches diagonally (actual viewable area is less). iPhone XS and iPhone XS Max are splash, water, and dust resistant and were tested under controlled laboratory conditions with a rating of IP68 under IEC standard 60529 (maximum depth of 2 meters up to 30 minutes).',
        'date_released': '2019',
        'rating': '4.8',
        'number_of_reviews': '10',
        'image': '/static/images/image_1.jpg'

    }
    return render(request, 'phone.html', context)