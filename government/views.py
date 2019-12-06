from django.shortcuts import render
from django.http import JsonResponse
from government.models import PeopleRequest
from django.http import JsonResponse
import datetime
import heapq
from pro import pro

def minsheng(request):
    if request.method == 'GET':
        startDate = datetime.datetime.strptime(request.GET.get('startDate'), "%Y%m%d")
        temp = datetime.datetime.strptime(request.GET.get('endDate'), "%Y%m%d")
        endDate = temp + datetime.timedelta(days=1)
        if startDate and endDate:
            request_list = PeopleRequest.objects.filter(create_time__range=(startDate, endDate))
            print(request_list)
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


# def minsheng(request):
#     print('request is ')
#     print(request.GET.get('startDate'))
#     print(request.GET.get('endDate'))
#     if request.GET.get('startDate') == '20191114':
#         print("this is 20191114")
#         return JsonResponse({"status": 0, "data": "[{value:200, name:'投诉'},\
#                 {'value':200, name:'感谢'},\
#                 {value:200, name:'咨询'},\
#                 {value:200, name:'求决'},\
#                 {value:200, name:'其它'},\
#                 {value:200, name:'建议'}]"})
#     elif request.GET.get('startDate') == '20181130':
#         print("this is 20181130")
#         return JsonResponse({"status": 0, "data": "[{value:200, name:'投诉'},\
#                 {'value':100, 'name':'感谢'},\
#                 {value:200, name:'咨询'},\
#                 {value:100, name:'求决'},\
#                 {value:200, name:'其它'},\
#                 {value:200, name:'建议'}]"})


def test(request):
    print("fuck")
    print(request.GET.get('age'))
    return JsonResponse({"status": 0, "message": "This is Django message"})


def user(request):
    if request.method == 'GET':
        print('request is ')
        print(request.GET.get('name'))
        return JsonResponse({'status': 0, 'data': '[1, 2, 3, 4]'})
    else:
        print('not GET')
        print(request.GET.get('name'))
        return JsonResponse({'status': 0, 'data': [5, 6, 7, 8]})


# def jiedao(request):
#     if request.method == 'GET':
#         print('request is ')
#         print(request.GET.get('startDate'))
#         print(request.GET.get('endDate'))
#         if request.GET.get('startDate') == '20191114':
#             print("this is 20191114")
#             return JsonResponse({"status": 0, "data": "[{\
#                   name: '市容城管',\
#                   type: 'bar',\
#                   stack:'事件数目',\
#                   data: [5, 5, 5, 5, 5, 5]\
#                   }, {\
#                   name: '禽畜养殖污染',\
#                   type: 'bar',\
#                   stack:'事件数目',\
#                   data: [5, 5, 5, 5, 5, 5]\
#                   }, {\
#                   name: '市政/公共设施',\
#                   type: 'bar',\
#                   stack:'事件数目',\
#                   data: [5, 5, 5, 5, 5, 5]\
#               }]"})
#         elif request.GET.get('startDate') == '20181130':
#             print("this is 20181130")
#             return JsonResponse({"status": 0, "data": "[{\
#                   name: '市容城管',\
#                   type: 'bar',\
#                   stack:'事件数目',\
#                   data: [5, 15, 25, 35, 45, 55]\
#                   }, {\
#                   name: '禽畜养殖污染',\
#                   type: 'bar',\
#                   stack:'事件数目',\
#                   data: [55, 45, 35, 25, 15, 5]\
#                   }, {\
#                   name: '市政/公共设施',\
#                   type: 'bar',\
#                   stack:'事件数目',\
#                   data: [5, 5, 5, 5, 5, 5]\
#                   }, {\
#                   name: 'ABCDE',\
#                   type: 'bar',\
#                   stack:'事件数目',\
#                   data: [1, 2, 3, 4, 5, 5]\
#               }]"})


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
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '教育体制',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 1019]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '服务行业废气扰民',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 140]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '宣传广告违法行为',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 180]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '占道经营',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 178]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '车辆乱停放',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 179]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '废弃物堆放',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 177]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '垃圾问题',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 172]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '工业噪声',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 132]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '刑案侦破',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 130]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '公用部件',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 185]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '公共设施保洁',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 175]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '绿化养护',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 176]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '其他市容违法行为或影响市容案件',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 181]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '住房保障和房地产',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 162]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '城市公共资源管理',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 187]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '公共交通管理',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 193]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '宣传舆论',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 1002]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '建筑施工噪声',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 133]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '社会生活噪声',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 137]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '集体土地上房屋拆迁与补偿',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 966]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '道路交通安全',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 27]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '人力资源',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 1047]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '禽畜养殖污染',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 138]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '物业服务管理监督',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 117]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '地质安全',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 60]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '商业经营噪声',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 134]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '市政、公共设施设置及维护',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 186]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '环卫设施设置及维护',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 182]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '行政能效',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 100]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '医政监管',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 1007]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '表达情感',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 938]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '供、排水及水质问题',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 152]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '消费维权',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 61]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '线路消防安全',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 23]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '警务监督',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 129]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '水污染',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 141]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '社会组织',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 107]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '劳动就业',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 34]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '互联网与通讯',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 59]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '军转安置',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 89]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '双拥优抚',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 795]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '住宅区（园区）或建筑物内安全、环卫问题',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 120]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '扬尘污染',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 142]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "},{\
                                                   name: '无证无照经营',\
                                                   type: 'bar',\
                                                   stack: '事件数目',\
                                                   data: " + str(
                [len([i for i in request_list if i.street_id == x and i.main_type_id == 46]) for x in
                 [101, 104, 100, 105, 102, 103]]) + \
                                                      "}]"})


# def jieban(request):
#     if request.method == 'GET':
#         # print('request is none')
#         if request.GET.get('startDate') == '20191114':
#             print("this is 20191114")
#             return JsonResponse({"status": 0, "inData": "[\
#                 {value:100, name:'处置中'},\
#                 {value:100, name:'按期结办'},\
#                 {value:100, name:'超期结办'}\
#                 ]", "outData": "[\
#                 {value:10, name:'市容环卫'},\
#                 {value:10, name:'环保水务'},\
#                 {value:10, name:'市政设施'},\
#                 {value:10, name:'规土城建'},\
#                 {value:10, name:'教育卫生'},\
#                 {value:10, name:'安全隐患'},\
#                 {value:10, name:'组织人事'},\
#                 {value:10, name:'党纪政纪'}\
#             ]"})
#         elif request.GET.get('startDate') == '20181130':
#             print("this is 20181130")
#             return JsonResponse({"status": 0, "inData": "[\
#                 {value:100, name:'处置中'},\
#                 {value:200, name:'按期结办'},\
#                 {value:300, name:'超期结办'}\
#                 ]", "outData": "[\
#                 {value:10, name:'市容环卫'},\
#                 {value:20, name:'环保水务'},\
#                 {value:30, name:'市政设施'},\
#                 {value:40, name:'规土城建'},\
#                 {value:50, name:'教育卫生'},\
#                 {value:60, name:'安全隐患'},\
#                 {value:70, name:'组织人事'},\
#                 {value:80, name:'党纪政纪'}\
#             ]"})


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
            print(top_5)

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
            # sum_other = PeopleRequest.objects.count() - sum_5
            print(outData)
            return JsonResponse({"status": 1,
                                 "inData": "[{value:" + str(len(chuzhizhong)) + ", name:'处置中'},\
                                            {value:" + str(len(anqijieban)) + ", name:'按期结办'},\
                                            {value:" + str(len(chaoqijieban)) + ", name:'超期结办'}]",
                                 "outData": str(outData)})
            # "outData": "[{value:" + str(len_list[top_5[0]]) + ", name:'" + type_list[top_5[0]] + "'},\
            #            {value:" + str(sum_other) + ", name:'其他'},\
            #            ]"})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入起止日期"})



# def shequ(request):
#     if request.method == 'GET':
#         # print('request is none')
#         if request.GET.get('startDate') == '20191114':
#             print("this is 20191114")
#             return JsonResponse({"status": 0, "data": "[\
#                  {name: '南布社区', value: 279},\
#                  {name: '和平社区', value: 279},\
#                  {name: '坪山社区', value: 279},\
#                  {name: '汤坑社区', value: 279},\
#                  {name: '金沙社区', value: 279},\
#                  {name: '江岭社区', value: 279},\
#                  {name: '石井社区', value: 279},\
#                  {name: '六和社区', value: 279},\
#                  {name: '沙湖社区', value: 279},\
#                  {name: '老坑社区', value: 279},\
#                  {name: '竹坑社区', value: 279},\
#                  {name: '秀新社区', value: 279},\
#                  {name: '沙田社区', value: 279},\
#                  {name: '六联社区', value: 279},\
#                  {name: '坪环社区', value: 279},\
#                  {name: '龙田社区', value: 279},\
#                  {name: '坑梓社区', value: 279},\
#                  {name: '沙坣社区', value: 279},\
#                  {name: '田头社区', value: 279},\
#                  {name: '碧岭社区', value: 279},\
#                  {name: '金龟社区', value: 279},\
#                  {name: '马峦社区', value: 279},\
#             ]"})
#         elif request.GET.get('startDate') == '20181130':
#             print("this is 20181130")
#             return JsonResponse({"status": 0, "data": "[\
#                  {name: '南布社区', value: 1},\
#                  {name: '和平社区', value: 1},\
#                  {name: '坪山社区', value: 1},\
#                  {name: '汤坑社区', value: 1},\
#                  {name: '金沙社区', value: 1},\
#                  {name: '江岭社区', value: 1},\
#                  {name: '石井社区', value: 1},\
#                  {name: '六和社区', value: 1},\
#                  {name: '沙湖社区', value: 1},\
#                  {name: '老坑社区', value: 1},\
#                  {name: '竹坑社区', value: 1},\
#                  {name: '秀新社区', value: 1},\
#                  {name: '沙田社区', value: 1},\
#                  {name: '六联社区', value: 1},\
#                  {name: '坪环社区', value: 1},\
#                  {name: '龙田社区', value: 1},\
#                  {name: '坑梓社区', value: 1},\
#                  {name: '沙坣社区', value: 1},\
#                  {name: '田头社区', value: 1},\
#                  {name: '碧岭社区', value: 279},\
#                  {name: '金龟社区', value: 279},\
#                  {name: '马峦社区', value: 279},\
#             ]"})


def shequ(request):
    if request.method == 'GET':
        startDate = datetime.datetime.strptime(request.GET.get('startDate'), "%Y%m%d")
        temp = datetime.datetime.strptime(request.GET.get('endDate'), "%Y%m%d")
        endDate = temp + datetime.timedelta(days=1)
        if startDate and endDate:
            request_list = PeopleRequest.objects.filter(create_time__range=(startDate, endDate))
            print(request_list)
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
            print(data)
            return JsonResponse({"status": 1,
                                 "data": str(data)})
            # tousu = [i for i in request_list if i.event_property_name == "投诉"]
            # ganxie = [i for i in request_list if i.event_property_name == "感谢"]
            # zixun = [i for i in request_list if i.event_property_name == "咨询"]
            # qiujue = [i for i in request_list if i.event_property_name == "求决"]
            # qita = [i for i in request_list if i.event_property_name == "其他"]
            # jianyi = [i for i in request_list if i.event_property_name == "建议"]
            # return JsonResponse({"status": 1,
            #                      "data": "[{value:"+str(len(tousu))+", name:'投诉'},\
            #                                {value:"+str(len(ganxie))+", name:'感谢'},\
            #                                {value:"+str(len(zixun))+", name:'咨询'},\
            #                                {value:"+str(len(qiujue))+", name:'求决'},\
            #                                {value:"+str(len(qita))+", name:'其他'},\
            #                                {value:"+str(len(jianyi))+", name:'建议'}]"})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入起止日期"})


def login(request):
    if request.method == 'GET':
        print('name and password are')
        print(request.GET.get('username'))
        print(request.GET.get('password'))
        if request.GET.get('username') == 'admin' and request.GET.get('password') == '111111':

        # print(request.GET.get('msg'))
            return JsonResponse({"status": 1, "msg": "This is Django message"})
        # return JsonResponse({'status': 0, 'msg': '登录成功'})


def submit(request):
    print('尝试添加记录')
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
        weijieban = [i for i in request_list if i.intime_to_achieve_num == 0]
        return JsonResponse({"status": 1, 
                             "data": "str(weijieban)"})

def yichang(request):
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
        day_from = datetime.datetime.(2018,2,9)
        day_to = datetime.datetime.(2018,10,30)
        dayp = day_from
        while(dayp != day_to):
            nextday =  dayp + datetime.timedelta(days=1)
            request_list = PeopleRequest.objects.filter(create_time__range=(dayp, nextday))
            for community in communities:
                if len([i for i in request_list if i.community_name == community]) >= 10:
                    abnormals.append({"create_time": str(2018)+str(month)+str(day),
                                      "community_name": community})
            dayp = nextday

        return JsonResponse({"status": 1, 
                             "msg": "当天该社区事件数目超出阈值",
                             "data": str(abnormals)})

def yuce(request):
    if request.method == 'GET':
        day_from = datetime.datetime(2018,10,30) + datetime.timedelta(days=-35)
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
            tousu[x] = len([i for i in request_list if i.event_property_name == "投诉"])
            ganxie[x] = len([i for i in request_list if i.event_property_name == "感谢"])
            zixun[x] = len([i for i in request_list if i.event_property_name == "咨询"])
            qiujue[x] = len([i for i in request_list if i.event_property_name == "求决"])
            qita[x] = len([i for i in request_list if i.event_property_name == "其他"])
            jianyi[x] = len([i for i in request_list if i.event_property_name == "建议"])
            dayp = nextweek
        return JsonResponse({"status": 1, 
                             "data": str(pro(ganxie, zixun, jianyi, qiujue, tousu, qita))})