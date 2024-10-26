from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('acounts/', include('django.contrib.auth.urls')),
]
