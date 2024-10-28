from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration_page, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('storapp/upload_code', views.upload_code, name='upload-code'),
]
