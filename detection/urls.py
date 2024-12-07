from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Route for the home page
    path('stream/', views.stream_view, name='stream'),  # Route for the video stream
]
