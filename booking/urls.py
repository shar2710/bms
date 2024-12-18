from django.urls import path
from . import views

urlpatterns = [
    path('showtimes/', views.showtimes, name='showtimes'),
]
