

# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls.i18n import i18n_patterns
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
    
   
#     path('i18n/', include('django.conf.urls.i18n')),
# ]

# # 2) Все остальные -- через i18n_patterns
# urlpatterns += i18n_patterns(
#     # Если хотите, чтобы /admin/ тоже «интернационализировалось», 
#     # перенесите admin внутрь этого блока. Но обычно админ оставляют без /<lang>/ 
#     path('admin/', admin.site.urls),
    
#     # Ваши приложения
#     path('', include('targetapp.urls')),      # /   и /en/, /ru/
#     path('accounts/', include('accounts.urls')),

#     # Не ставит префикс /ru/ для русского (дефолтного) языка
#     prefix_default_language=False,
# )

# # 3) Статические файлы (только в DEBUG)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
   
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('targetapp.urls')),
    path('accounts/', include('accounts.urls')),
    # по умолчанию prefix_default_language=True — /ru/, /en/ и т.д.
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
