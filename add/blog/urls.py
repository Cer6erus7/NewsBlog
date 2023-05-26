from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('page', page),
    path('about', about),
    path('contact', contact)
]