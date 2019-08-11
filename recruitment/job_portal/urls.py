from django.urls import path

from .views import careers

urlpatterns = [
    path('careers/', careers, name='careers')
]
