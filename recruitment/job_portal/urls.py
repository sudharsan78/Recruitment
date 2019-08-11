from django.urls import path

from . import views

urlpatterns = [
    path('', views.careers, name='index'),
    path('post/<slug:slug_data>/', views.job_post, name="job_post"),
]
