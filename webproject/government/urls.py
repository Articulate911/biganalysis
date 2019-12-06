from django.urls import path
from . import views

app_name = 'government'

from django.urls import path
from government import views

urlpatterns = [
    path('test/', views.test),
    path('user/', views.user),
    path('jiedao/', views.jiedao),
    path('jieban/', views.jieban),
    path('minsheng/', views.minsheng),
    path('minsheng/', views.minsheng),
    path('login/', views.login)

]