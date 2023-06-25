from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('videos/', views.ListCreateVidMem.as_view()),
] 