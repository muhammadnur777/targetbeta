# from django.contrib.auth.admin import UserAdmin 
# from django.contrib.admin import register
# from .models import User,UserReview
# from django.contrib import admin


# admin.site.register(UserReview)
# admin.site.register(User)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import UserReview, User


admin.site.register(UserReview)


# User = get_user_model()

# Регистрируем кастомного User
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # можно сконфигурировать поля, как мы делали ранее
    pass

# # Регистрируем модель отзывов
# @admin.register(UserReview)
# class UserReviewAdmin(admin.ModelAdmin):
#     list_display = ('user', 'rating', 'posted')
#     list_filter  = ('rating', 'posted')
#     search_fields = ('user__username', 'comment')
