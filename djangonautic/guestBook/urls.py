from .views import index, sign

from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('sign/', sign, name='sign')
]