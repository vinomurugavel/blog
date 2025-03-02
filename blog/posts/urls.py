from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from . import views
urlpatterns=[
    path('',views.index, name='index'),
    path('post/<str:pk>',views.post, name='post')
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)