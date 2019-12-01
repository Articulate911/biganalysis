from django.db.models import UserProfile
from django.http import JsonResponse

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            if UserProfile.objects.filter(username=username).exists():
                user = UserProfile.objects.get(username=username)
                if user.password == password:
                    if user.isadmin:
                        return JsonResponse({"status": 1, "msg": "登录成功", "isadmin":1})
                    else
                        return JsonResponse({"status": 1, "msg": "登录成功", "isadmin":0})
                else
                    return JsonResponse({"status": 0, "msg": "密码错误"})
            else
                return JsonResponse({"status": 0, "msg": "用户名不存在"})
        return JsonResponse({"status": 0, "msg": "请填写用户名和密码"})
