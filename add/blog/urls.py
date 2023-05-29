from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('page/<int:id>', page),
    path('about', about),
    path('contact', contact)
]