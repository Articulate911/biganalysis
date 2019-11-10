# 导入 HttpResponse 模块
from django.http import HttpResponse
from .models import PeopleRequest
from django.shortcuts import render

# 视图函数
def request_list(request):
    requests = PeopleRequest.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'requests': requests }
    # render函数：载入模板，并返回context对象
    return render(request, 'government/list.html', context)