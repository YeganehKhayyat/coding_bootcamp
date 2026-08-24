from django.urls import path

from checkins.views import home, get_form

app_name = 'checkins'

urlpatterns = [
    path('home/', home , name='home'),
    path('add/', get_form, name='add')
]
