from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration_page, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('storapp/upload_code', views.upload_code, name='upload-code'),
    path('storapp/unlock_code/<int:pk>', views.unlock_code, name='unlock-code'),
    path('storapp/upload_image', views.upload_image, name='upload-image'),
    path('storapp/unlock_image/<int:pk>', views.unlock_image, name='unlock-image'),
    path('storapp/code/<int:pk>', views.CodeDetailView.as_view(), name='code-detail'),
    path('storapp/image/<int:pk>', views.ImageDetailView.as_view(), name='image-detail'),
]
