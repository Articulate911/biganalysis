from django.shortcuts import render
from django.http import JsonResponse
from government.models import PeopleRequest
from django.http import JsonResponse
from userprofile.models import UsrProfile
import datetime
import heapq
from math import pow


def minsheng(request):
    if request.method == 'GET':
        startDate = datetime.datetime.strptime(request.GET.get('startDate'), "%Y%m%d")
        temp = datetime.datetime.strptime(request.GET.get('endDate'), "%Y%m%d")
        endDate = temp + datetime.timedelta(days=1)
        if startDate and endDate:
            request_list = PeopleRequest.objects.filter(create_time__range=(startDate, endDate))
            tousu = [i for i in request_list if i.event_property_name == "投诉"]
            ganxie = [i for i in request_list if i.event_property_name == "感谢"]
            zixun = [i for i in request_list if i.event_property_name == "咨询"]
            qiujue = [i for i in request_list if i.event_property_name == "求决"]
            qita = [i for i in request_list if i.event_property_name == "其他"]
            jianyi = [i for i in request_list if i.event_property_name == "建议"]
            return JsonResponse({"status": 1,
                                 "data": "[{value:" + str(len(tousu)) + ", name:'投诉'},\
                                           {value:" + str(len(ganxie)) + ", name:'感谢'},\
                                           {value:" + str(len(zixun)) + ", name:'咨询'},\
                                           {value:" + str(len(qiujue)) + ", name:'求决'},\
                                           {value:" + str(len(qita)) + ", name:'其他'},\
                                           {value:" + str(len(jianyi)) + ", name:'建议'}]"})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入起止日期"})


def jiedao(request):
    if request.method == 'GET':
        startDate = datetime.datetime.strptime(request.GET.get('startDate'), "%Y%m%d")
        temp = datetime.datetime.strptime(request.GET.get('endDate'), "%Y%m%d")
        endDate = temp + datetime.timedelta(days=1)
        if startDate and endDate:
            request_list = PeopleRequest.objects.filter(create_time__range=(startDate, endDate))
            return JsonResponse({"status": 0, "data": "[{\
                        name:'市容城管',\
                        type:'bar',\
                        stack:'事件数目',\
                        data:" + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 1159]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '教育体制',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 1019]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '服务行业废气扰民',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 140]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '宣传广告违法行为',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 180]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '占道经营',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 178]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '车辆乱停放',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 179]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '废弃物堆放',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 177]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '垃圾问题',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 172]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '工业噪声',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 132]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '刑案侦破',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 130]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '公用部件',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 185]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '公共设施保洁',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 175]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '绿化养护',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 176]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '其他市容违法行为或影响市容案件',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 181]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '住房保障和房地产',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 162]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '城市公共资源管理',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 187]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '公共交通管理',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 193]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '宣传舆论',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 1002]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '建筑施工噪声',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 133]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '社会生活噪声',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 137]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '集体土地上房屋拆迁与补偿',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 966]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '道路交通安全',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 27]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '人力资源',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 1047]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '禽畜养殖污染',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 138]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '物业服务管理监督',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 117]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '地质安全',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 60]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '商业经营噪声',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 134]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '市政、公共设施设置及维护',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 186]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '环卫设施设置及维护',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 182]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '行政能效',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 100]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '医政监管',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 1007]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '表达情感',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 938]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '供、排水及水质问题',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 152]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '消费维权',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 61]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '线路消防安全',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 23]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '警务监督',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 129]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '水污染',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 141]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '社会组织',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 107]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '劳动就业',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 34]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '互联网与通讯',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 59]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '军转安置',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 89]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '双拥优抚',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 795]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '住宅区（园区）或建筑物内安全、环卫问题',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 120]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '扬尘污染',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 142]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "},{\
                                                   name: '无证无照经营',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 46]) for x in
                 [101, 104, 100, 105, 102, 103]]) +
                                                      "}]"})


def jieban(request):
    if request.method == 'GET':
        startDate = datetime.datetime.strptime(request.GET.get('startDate'), "%Y%m%d")
        temp = datetime.datetime.strptime(request.GET.get('endDate'), "%Y%m%d")
        endDate = temp + datetime.timedelta(days=1)
        if startDate and endDate:
            request_list = PeopleRequest.objects.filter(create_time__range=(startDate, endDate))
            chuzhizhong = [i for i in request_list if i.intime_archive_num == 1]
            anqijieban = [i for i in request_list if i.intime_to_archive_num == 1]
            chaoqijieban = [i for i in request_list if i.overtime_archive_num == 1]
            type_list = ['市容城管',
                         '事件数目',
                         '市政/公共设施',
                         '教育体制',
                         '服务行业废气扰民',
                         '宣传广告违法行为',
                         '占道经营',
                         '车辆乱停放',
                         '废弃物堆放',
                         '垃圾问题',
                         '工业噪声',
                         '刑案侦破',
                         '公用部件',
                         '公共设施保洁',
                         '绿化养护',
                         '其他市容违法行为或影响市容案件',
                         '住房保障和房地产',
                         '城市公共资源管理',
                         '公共交通管理',
                         '宣传舆论',
                         '建筑施工噪声',
                         '社会生活噪声',
                         '集体土地上房屋拆迁与补偿',
                         '道路交通安全',
                         '人力资源',
                         '禽畜养殖污染',
                         '物业服务管理监督',
                         '地质安全',
                         '商业经营噪声',
                         '市政、公共设施设置及维护',
                         '环卫设施设置及维护',
                         '行政能效',
                         '医政监管',
                         '表达情感',
                         '供、排水及水质问题',
                         '消费维权',
                         '线路消防安全',
                         '警务监督',
                         '水污染',
                         '社会组织',
                         '劳动就业',
                         '互联网与通讯',
                         '军转安置',
                         '双拥优抚',
                         '住宅区（园区）或建筑物内安全、环卫问题',
                         '扬尘污染',
                         '无证无照经营']
            len_list = []
            for x in type_list:
                temp = [i for i in request_list if i.main_type_name == x]
                len_list.append(len(temp))
            top_5 = list(set(map(len_list.index, heapq.nlargest(5, len_list))))
            sum_5 = 0
            outData = []
            for i in range(len(top_5)):
                temp = {}
                temp['value'] = len_list[top_5[i]]
                temp['name'] = str(type_list[top_5[i]])
                outData.append(temp)
                sum_5 = sum_5 + len_list[top_5[i]]
            sum_other = len(request_list) - sum_5
            temp = {}
            temp['name'] = '其它'
            temp['value'] = sum_other
            outData.append(temp)
            return JsonResponse({"status": 1,
                                 "inData": "[{value:" + str(len(chuzhizhong)) + ", name:'处置中'},\
                                            {value:" + str(len(anqijieban)) + ", name:'按期结办'},\
                                            {value:" + str(len(chaoqijieban)) + ", name:'超期结办'}]",
                                 "outData": str(outData)})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入起止日期"})


def shequ(request):
    if request.method == 'GET':
        startDate = datetime.datetime.strptime(request.GET.get('startDate'), "%Y%m%d")
        temp = datetime.datetime.strptime(request.GET.get('endDate'), "%Y%m%d")
        endDate = temp + datetime.timedelta(days=1)
        if startDate and endDate:
            request_list = PeopleRequest.objects.filter(create_time__range=(startDate, endDate))
            shequ_list = [
                '和平社区', \
                '坪山社区', \
                '汤坑社区', \
                '金沙社区', \
                '江岭社区', \
                '石井社区', \
                '六和社区', \
                '沙湖社区', \
                '老坑社区', \
                '竹坑社区', \
                '秀新社区', \
                '沙田社区', \
                '六联社区', \
                '坪环社区', \
                '龙田社区', \
                '坑梓社区', \
                '沙坣社区', \
                '田头社区', \
                '碧岭社区', \
                '金龟社区', \
                '马峦社区' \
                ]
            data = []
            for x in range(len(shequ_list)):
                y = [i for i in request_list if i.community_name == shequ_list[x]]
                tempvalue = len(y)
                tempname = shequ_list[x]
                temp = {}
                temp['name'] = tempname
                temp['value'] = tempvalue
                data.append(temp)
            return JsonResponse({"status": 1,
                                 "data": str(data)})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入起止日期"})


def login(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        password = request.GET.get('password')
        if username and password:
            if UsrProfile.objects.filter(username=username).exists():
                user = UsrProfile.objects.get(username=username)
                if user.password == password:
                    if user.isadmin:
                        return JsonResponse({"status": 1, "msg": "登录成功", "isadmin":1})
                    else:
                        return JsonResponse({"status": 1, "msg": "登录成功", "isadmin":0})
                else:
                    return JsonResponse({"status": 0, "msg": "密码错误"})
            else:
                return JsonResponse({"status": 0, "msg": "用户名不存在"})
        return JsonResponse({"status": 0, "msg": "请填写用户名和密码"})


def submit(request):
    if request.method == 'GET':
        report_num = request.GET.get('report_num')
        event_property_name = request.GET.get('event_property_name')
        event_type_id = request.GET.get('event_type_id')
        event_type_name = request.GET.get('event_type_name')
        event_src_name = request.GET.get('event_src_name')
        district_id = request.GET.get('district_id')
        intime_archive_num = request.GET.get('intime_archive_num')
        sub_type_id = request.GET.get('sub_type_id')
        district_name = request.GET.get('district_name')
        community_id = request.GET.get('community_id')
        rec_id = request.GET.get('rec_id')
        street_id = request.GET.get('street_id')
        overtime_archive_num = request.GET.get('overtime_archive_num')
        operate_num = request.GET.get('operate_num')
        dispose_unit_id = request.GET.get('dispose_unit_id')
        street_name = request.GET.get('street_name')
        create_time = request.GET.get('create_time')
        event_src_id = request.GET.get('event_src_id')
        intime_to_archive_num = request.GET.get('intime_to_archive_num')
        sub_type_name = request.GET.get('sub_type_name')
        event_property_id = request.GET.get('event_property_id')
        occur_place = request.GET.get('occur_place')
        community_name = request.GET.get('community_name')
        dispose_unit_name = request.GET.get('dispose_unit_name')
        main_type_name = request.GET.get('main_type_name')
        main_type_id = request.GET.get('main_type_id')

        if      report_num and \
                event_property_name and \
                event_type_id and \
                event_type_name and \
                event_src_name and \
                district_id and \
                intime_archive_num and \
                sub_type_id and \
                district_name and \
                community_id and \
                rec_id and \
                street_id and \
                overtime_archive_num and \
                operate_num and \
                dispose_unit_id and \
                street_name and \
                create_time and \
                event_src_id and \
                intime_to_archive_num and \
                sub_type_name and \
                event_property_id and \
                occur_place and \
                community_name and \
                dispose_unit_name and \
                main_type_name and \
                main_type_id:
            PeopleRequest.objects.create(
                                         report_num=report_num, \
                                         event_property_name=event_property_name, \
                                         event_type_id=event_type_id, \
                                         event_type_name=event_type_name, \
                                         event_src_name=event_src_name, \
                                         district_id=district_id, \
                                         intime_archive_num=intime_archive_num, \
                                         sub_type_id=sub_type_id, \
                                         district_name=district_name, \
                                         community_id=community_id, \
                                         rec_id=rec_id, \
                                         street_id=street_id, \
                                         overtime_archive_num=overtime_archive_num, \
                                         operate_num=operate_num, \
                                         dispose_unit_id=dispose_unit_id, \
                                         street_name=street_name, \
                                         create_time=create_time, \
                                         event_src_id=event_src_id, \
                                         intime_to_archive_num=intime_to_archive_num, \
                                         sub_type_name=sub_type_name, \
                                         event_property_id=event_property_id, \
                                         occur_place=occur_place, \
                                         community_name=community_name, \
                                         dispose_unit_name=dispose_unit_name, \
                                         main_type_name=main_type_name, \
                                         main_type_id=main_type_id)
            return JsonResponse({"status": 1,
                                 "msg": "添加记录成功"})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入字段信息"})


def weijieban(request):
    if request.method == 'GET':
        date_from = datetime.datetime(2018, 10, 30)
        date_to = datetime.datetime(2018, 10, 31)
        request_list = PeopleRequest.objects.filter(create_time__range=(date_from, date_to))
        weijieban = [i for i in request_list if i.intime_to_archive_num == 0]
        category = []
        rank=["12319", "12345", "固话投诉", "政府信箱", "@坪山", "美丽深圳"]
        for item in rank:
            category.append([i for i in weijieban if i.event_src_name == item])
        data=[]
        for y in category:
            for x in y:
                data.append({"create_time":datetime.datetime.strftime(x.create_time, "%Y-%m-%d %H:%M:%S"),
                            "street":x.street_name,
                            "community":x.community_name,
                            "title":x.sub_type_name,
                            "source":x.event_src_name,
                            "department":x.dispose_unit_name,
                            "property":x.event_property_name,
                            "status":1})
        return JsonResponse({"status": 1,
                             "data": str(data)})



def abnormal(request):
    communities = ["南布社区",
                   "和平社区",
                   "坪山社区",
                   "汤坑社区",
                   "金沙社区",
                   "江岭社区",
                   "石井社区",
                   "六和社区",
                   "沙湖社区",
                   "老坑社区",
                   "竹坑社区",
                   "秀新社区",
                   "沙田社区",
                   "六联社区",
                   "坪环社区",
                   "龙田社区",
                   "坑梓社区",
                   "沙坣社区",
                   "田头社区",
                   "田心社区",
                   "碧岭社区",
                   "金龟社区",
                   "马峦社区"]
    abnormals = []
    if request.method == 'GET':
        day_from = datetime.datetime(2018, 2, 9)
        day_to = datetime.datetime(2018, 10, 30)
        dayp = day_from
        while(dayp != day_to):
            nextday =  dayp + datetime.timedelta(days=1)
            request_list = PeopleRequest.objects.filter(create_time__range=(dayp, nextday))
            for community in communities:
                if len([i for i in request_list if i.community_name == community]) >= 10:
                    abnormals.append({"title": str(datetime.datetime.strftime(dayp, "%Y%m%d")),
                                   "message": community})
            dayp = nextday
        return JsonResponse({"status": 1,
                             "msg": "当天该社区事件数目超出阈值",
                             "data": str(abnormals)})


def yuce(request):
    if request.method == 'GET':
        print(request.GET.get('date'))
        # print(request.GET)
        # if(request.GET.get('date')):
        date = int(request.GET.get('date'))
        year = int(date / 10000)
        month = int((date / 100) % 100)
        day = int(date % 100)
        # print(year)
        # print(month)
        # print(day)
        day_from = datetime.datetime(year, month, day) + datetime.timedelta(days=-35)

        # day_from = datetime.datetime(2018, 10, 30) + datetime.timedelta(days=-35)
        dayp = day_from
        tousu = []
        ganxie = []
        zixun = []
        qiujue = []
        qita = []
        jianyi = []
        for x in range(5):
            nextweek = dayp + datetime.timedelta(days=7)
            request_list = PeopleRequest.objects.filter(create_time__range=(dayp, nextweek))
            tousu.append(len([i for i in request_list if i.event_property_name == "投诉"]))
            ganxie.append(len([i for i in request_list if i.event_property_name == "感谢"]))
            zixun.append(len([i for i in request_list if i.event_property_name == "咨询"]))
            qiujue.append(len([i for i in request_list if i.event_property_name == "求决"]))
            qita.append(len([i for i in request_list if i.event_property_name == "其他"]))
            jianyi.append(len([i for i in request_list if i.event_property_name == "建议"]))
            dayp = nextweek
        return JsonResponse({"status": 1,
                             "data": str(pro(ganxie, zixun, jianyi, qiujue, tousu, qita))})


def predict(data, alpha):
    beta = 1-alpha
    ave = 1/5*(data[0]+data[1]+data[2]+data[3]+data[4])
    return alpha*data[4]+alpha*beta*data[3]+alpha*pow(beta, 2)*data[2]+alpha*pow(beta, 3)*data[1]+alpha*pow(beta, 4)*data[0]+pow(beta, 5)*ave


def pro(ganxie, zixun, jianyi, qiujue, tousu, qita):
    alpha = 0.7
    i = 0
    sum_count = [0.0, 0.0, 0.0, 0.0, 0.0]
    g = [0.0, 0.0, 0.0, 0.0, 0.0]
    z = [0.0, 0.0, 0.0, 0.0, 0.0]
    j = [0.0, 0.0, 0.0, 0.0, 0.0]
    q1 = [0.0, 0.0, 0.0, 0.0, 0.0]
    t = [0.0, 0.0, 0.0, 0.0, 0.0]
    q2 = [0.0, 0.0, 0.0, 0.0, 0.0]
    ganxie_prd = [0.0, 0.0, 0.0, 0.0, 0.0]
    zixun_prd = [0.0, 0.0, 0.0, 0.0, 0.0]
    jianyi_prd = [0.0, 0.0, 0.0, 0.0, 0.0]
    qiujue_prd = [0.0, 0.0, 0.0, 0.0, 0.0]
    tousu_prd = [0.0, 0.0, 0.0, 0.0, 0.0]
    qita_prd = [0.0, 0.0, 0.0, 0.0, 0.0]
    sum_num = 0

    for i in range(0, 5, 1):
        sum_count[i] = ganxie[i] + zixun[i] + jianyi[i] + qiujue[i] + tousu[i] + qita[i] + 0.0
    if(sum_count == [0.0, 0.0, 0.0, 0.0, 0.0]):
        return [0, 0, 0, 0, 0]
    for i in range(0, 5, 1):
        g[i] = 1.0 * ganxie[i] / sum_count[i]
        z[i] = 1.0 * zixun[i] / sum_count[i]
        j[i] = 1.0 * jianyi[i] / sum_count[i]
        q1[i] = 1.0 * qiujue[i] / sum_count[i]
        t[i] = 1.0 * tousu[i] / sum_count[i]
        q2[i] = 1.0 * qita[i] / sum_count[i]

    ganxie_prd = predict(g, alpha)
    zixun_prd = predict(z, alpha)
    jianyi_prd = predict(j, alpha)
    qiujue_prd = predict(q1, alpha)
    tousu_prd = predict(t, alpha)
    qita_prd = predict(q2, alpha)

    sum_num = ganxie_prd + zixun_prd + jianyi_prd + qiujue_prd + tousu_prd + qita_prd
    if sum_num == 0:
        return [0, 0, 0, 0, 0]
    else:
        ganxie_prd = ganxie_prd / sum_num
        zixun_prd = zixun_prd / sum_num
        jianyi_prd = jianyi_prd / sum_num
        qiujue_prd = qiujue_prd / sum_num
        tousu_prd = tousu_prd / sum_num
        qita_prd = qita_prd / sum_num
        ans = [ganxie_prd, zixun_prd, jianyi_prd, qiujue_prd, tousu_prd, qita_prd]
        return ans


