from django.urls import path
from . import views

app_name = 'government'

urlpatterns = [
    path('request_list/', views.request_list, name='request_list'),
]