from django.contrib import admin

from .models import PeopleRequest

# 注册PeopleRequest到admin中
admin.site.register(PeopleRequest)