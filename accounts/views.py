

# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User, UserReview
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username','').strip()
        password = request.POST.get('password','')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Вы вошли как {user.username}')
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя или пароль.')

    return render(request, 'login.html')

@login_required
def add_review(request):
    if request.method == 'POST':
        comment = request.POST.get('comment','').strip()
        rating  = int(request.POST.get('rating',5))
        if comment:
            UserReview.objects.create(
                user=request.user,
                comment=comment,
                rating=rating
            )
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')





# accounts/views.py


User = get_user_model()
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name','').strip()
        last_name  = request.POST.get('last_name','').strip()
        pwd1       = request.POST.get('password1','')
        pwd2       = request.POST.get('password2','')

        if not first_name or not last_name or not pwd1:
            messages.error(request, 'Введите имя, фамилию и пароль.')
        elif pwd1 != pwd2:
            messages.error(request, 'Пароли не совпадают.')
        elif User.objects.filter(username__iexact=f"{first_name}{last_name}").exists():
            messages.error(request, 'Пользователь с таким именем уже существует.')
        else:
            user = User.objects.create_user(
                username=f"{first_name.lower()}{last_name.lower()}",
                password=pwd1,
                first_name=first_name,
                last_name=last_name,
            )
            avatar = request.FILES.get('avatar')
            if avatar:
                user.avatar = avatar
                user.save()

            login(request, user)
            return redirect('home')

    return render(request, 'signup.html')