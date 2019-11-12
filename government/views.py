# 导入 HttpResponse 模块
from django.http import HttpResponse
from .models import PeopleRequest
from django.shortcuts import render
from django.http import JsonResponse

# 视图函数
# def request_list(request):
#     requests = PeopleRequest.objects.all()
#     # 需要传递给模板（templates）的对象
#     context = { 'requests': requests }
#     # render函数：载入模板，并返回context对象
#     return render(request, 'government/list.html', context)


def time_filter(request):
    if request.method == 'GET':
        # print(request.GET.get('name'))
        print('request is ')
        print(request.GET.get('time_start'))
        print(request.GET.get('time_end'))
        return JsonResponse({'status': 0, 'data': '[1, 2, 3, 4]'})
    else:
        print('not GET')
        print(request.GET.get('name'))
        return JsonResponse({'status': 0, 'data': [5, 6, 7, 8]})
