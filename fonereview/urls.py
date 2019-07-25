"""fonereview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from users import views as User_views
from app import views as App_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', App_views.fonereview_homepage, name="home"),
    path('sign-up/', User_views.register, name='sign-up'),
    path('sign-in/', User_views.login_in, name='login'),
    path('sign-out/', User_views.log_out, name='logout'),
    path('edit-profile/',User_views.edit_profile),
    path('getlatest/',App_views.get_device_info),
    path('device/<device_id>/',App_views.fonereview_device_single),
    path('popular_phone/',App_views.fonereview_popular,name='popular'),
    path('about/',App_views.fonereview_about, name='about'),
    path('contact/',App_views.fonereview_contact, name='contact'),    
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
