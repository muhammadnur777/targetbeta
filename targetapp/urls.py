from django.urls import path
from .views import index, map, save_contact



urlpatterns = [
    path('', index, name='home'),
    path('save_contact/', save_contact, name='save_contact'),
    path('map/', map, name='map')

    
]
