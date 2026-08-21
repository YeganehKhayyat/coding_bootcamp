from django.urls import path

from checkins.views import home

urlpatterns = [
    path('home/', home)
]
