from django.shortcuts import render, redirect
from accounts.models import UserReview

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import contact
# Create your views here.
# def index(request):
#     return render(request, 'index.html')



# targetapp/views.py

def index(request):
    """Главная страница + отзывы"""
    reviews = UserReview.objects.select_related('user').all()
    return render(request, 'index.html', {'reviews': reviews})


def map(request):
    return render(request, 'map.html')


@csrf_exempt
def save_contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '')
        phone = data.get('phone', '')

        if name and phone:
            contact.objects.create(name=name, phone=phone)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'error'}, status=400)
    return JsonResponse({'error': 'invalid request'}, status=400)