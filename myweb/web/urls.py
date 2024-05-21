from django.urls import path
from .views import Index_home


urlpatterns=[

    path('', Index_home),


]



