from .models import PeopleRequest
from django.http import JsonResponse
import heapq
from datetime import datetime

def minsheng(request):
    if request.method == 'GET':
        startDate = int(request.GET.get('startDate'))
        endDate = int(request.GET.get('endDate'))
        if startDate and endDate:
            startYear = startDate/10000
            startMonth = (startDate%10000)/100
            startDay = startDate%100
            endYear = endDate/10000
            endMonth = (endDate/10000)%100
            endDay = endDate%100
            date_from = datetime(startYear, startMonth, startDay, 0, 0)
            date_to = datetime(endYear, endMonth, endDay, 0, 0)
            request_list = PeopleRequest.objects.filter(create_time__range=(date_from, date_to))
            tousu = [i for i in request_list if i.event_property_name == "投诉"]
            ganxie = [i for i in request_list if i.event_property_name == "感谢"]
            zixun = [i for i in request_list if i.event_property_name == "咨询"]
            qiujue = [i for i in request_list if i.event_property_name == "求决"]
            qita = [i for i in request_list if i.event_property_name == "其他"]
            jianyi = [i for i in request_list if i.event_property_name == "建议"]
            return JsonResponse({"status": 1, 
                                 "data": "[{value:"+str(len(tousu))+", name:'投诉'},\
                                           {value:"+str(len(ganxie))+", name:'感谢'},\
                                           {value:"+str(len(zixun))+", name:'咨询'},\
                                           {value:"+str(len(qiujue))+", name:'求决'},\
                                           {value:"+str(len(qita))+", name:'其他'},\
                                           {value:"+str(len(jinayi))+", name:'建议'}]"})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入起止日期"})

def jieban(request):
    if request.method == 'GET':
        startDate = int(request.GET.get('startDate'))
        endDate = int(request.GET.get('endDate'))
        if startDate and endDate:
            startYear = startDate/10000
            startMonth = (startDate%10000)/100
            startDay = startDate%100
            endYear = endDate/10000
            endMonth = (endDate/10000)%100
            endDay = endDate%100
            date_from = datetime(startYear, startMonth, startDay, 0, 0)
            date_to = datetime(endYear, endMonth, endDay, 0, 0)
            request_list = PeopleRequest.objects.filter(create_time__range=(date_from, date_to))
            chuzhizhong = [i for i in request_list if i.intime_achieve_num == 1]
            anqijieban = [i for i in request_list if i.intime_to_achieve_num == 1]
            chaoqijieban = [i for i in request_list if i.overtime_achieve_num == 1]
            type_list = ['市�?�城�?',
                        '事件数目',
                        '市政/�?共�?�施',
                        '教育体制',
                        '服务行业废气扰民',
                        '宣传广告违法行为',
                        '占道经营',
                        '车辆乱停�?',
                        '废弃物堆�?',
                        '垃圾�?�?',
                        '工业�?�?',
                        '刑�?�侦�?',
                        '�?用部�?',
                        '�?共�?�施保洁',
                        '绿化养护',
                        '其他市�?�违法�?�为或影响市容�?�件',
                        '住房保障和房地产',
                        '城市�?共资源�?�理',
                        '�?共交通�?�理',
                        '宣传舆�??',
                        '建筑施工�?�?',
                        '社会生活�?�?',
                        '集体土地上房屋拆迁与补偿',
                        '道路交通安�?',
                        '人力资源',
                        '禽畜养殖污染',
                        '物业服务管理监督',
                        '地质安全',
                        '商业经营�?�?',
                        '市政、公共�?�施设置及维�?',
                        '�?�?设施设置及维�?',
                        '行政能效',
                        '医政监�??',
                        '表达情感',
                        '供、排水及水质�?�?',
                        '消费维权',
                        '线路消防安全',
                        '警务监督',
                        '水污�?',
                        '社会组织',
                        '劳动就业',
                        '互联网与通�??',
                        '军转安置',
                        '双拥优抚',
                        '住宅区（�?区）或建筑物内安全、环�?�?�?',
                        '�?尘污�?',
                        '无证无照经营']
            len_list = []
            for x in type_list:
                temp = [i for i in request_list if i.MAIN_TYPE_NAME == x]
                len_list.append(len(temp))
            top_5 = list(map(len_list.index, heapq.nlargest(5, len_list)))
            sum_5 = 0
            for i in range(5):
                sum_5 = sum_5 + len_list[top_5[i]]
            sum_other = 10000 - sum_5

            return JsonResponse({"status": 1, 
                                "inData": "[{value:"+str(len(chuzhizhong))+", name:'处置�?'},\
                                            {value:"+str(len(anqijieban))+", name:'按期结办'},\
                                            {value:"+str(len(chaoqijieban))+", name:'超期结办'}]", 
                                "outData": "[{value:"+str(len_list[top_5[0]])+", name:'"+type_list[top_5[0]]+"'},\
                                            {value:"+str(len_list[top_5[1]])+", name:'"+type_list[top_5[1]]+"'},\
                                            {value:"+str(len_list[top_5[2]])+", name:'"+type_list[top_5[2]]+"'},\
                                            {value:"+str(len_list[top_5[3]])+", name:'"+type_list[top_5[3]]+"'},\
                                            {value:"+str(len_list[top_5[4]])+", name:'"+type_list[top_5[4]]+"'},\
                                            {value:"+str(sum_other)+", name:'其他'},\
                                            ]"})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入起止日�?"})

def load(request):
    if request.method == 'GET':
        ID = request.GET.get('id')
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

        if ID and
           report_num and
           event_property_name and
           event_type_id and
           event_type_name and
           event_src_name and
           district_id and
           intime_archive_num and
           sub_type_id and
           district_name and
           community_id and
           rec_id and
           street_id and
           overtime_archive_num and
           operate_num and
           dispose_unit_id and
           street_name and
           create_time and
           event_src_id and
           intime_to_archive_num and
           sub_type_name and
           event_property_id and
           occur_place and
           community_name and
           dispose_unit_name and
           main_type_name and
           main_type_id:
            PeopleRequest.objects.create(id=ID,
                                         report_num=report_num,
                                         event_property_name=event_property_name,
                                         event_type_id=event_type_id,
                                         event_type_name=event_type_name,
                                         event_src_name=event_src_name,
                                         district_id=district_id,
                                         intime_archive_num=intime_archive_num,
                                         sub_type_id=sub_type_id,
                                         district_name=district_name,
                                         community_id=community_id,
                                         rec_id=rec_id,
                                         street_id=street_id,
                                         overtime_archive_num=overtime_archive_num,
                                         operate_num=operate_num,
                                         dispose_unit_id=dispose_unit_id,
                                         street_name=street_name,
                                         create_time=create_time,
                                         event_src_id=event_src_id,
                                         intime_to_archive_num=intime_to_archive_num,
                                         sub_type_name=sub_type_name,
                                         event_property_id=event_property_id,
                                         occur_place=occur_place,
                                         community_name=community_name,
                                         dispose_unit_name=dispose_unit_name,
                                         main_type_name=main_type_name,
                                         main_type_id=main_type_id)
            return JsonResponse({"status": 1, 
                                 "msg": "添加记录成功"})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入字段信�?"})

def jiedao(request):
    if request.method == 'GET':
        startDate = int(request.GET.get('startDate'))
        endDate = int(request.GET.get('endDate'))
        if startDate and endDate:
            startYear = startDate/10000
            startMonth = (startDate%10000)/100
            startDay = startDate%100
            endYear = endDate/10000
            endMonth = (endDate/10000)%100
            endDay = endDate%100
            date_from = datetime(startYear, startMonth, startDay, 0, 0)
            date_to = datetime(endYear, endMonth, endDay, 0, 0)
            request_list = PeopleRequest.objects.filter(create_time__range=(date_from, date_to))
            longtian = [i for i in request_list if i.community_name == "龙田街道"]
            pingshan = [i for i in request_list if i.community_name == "�?山�?�道"]
            biling = [i for i in request_list if i.community_name == "碧岭街道"]
            kengzi = [i for i in request_list if i.community_name == "坑�?��?�道"]
            maluan = [i for i in request_list if i.community_name == "�?峦�?�道"]
            shijing = [i for i in request_list if i.community_name == "石井街道"]
            return JsonResponse({"status": 1, 
                                 "data": "[{value:"+str(len(longtian))+", name:'龙田街道'},\
                                           {value:"+str(len(pingshan))+", name:'�?山�?�道'},\
                                           {value:"+str(len(biling))+", name:'碧岭街道'},\
                                           {value:"+str(len(kengzi))+", name:'坑�?��?�道'},\
                                           {value:"+str(len(maluan))+", name:'�?峦�?�道'},\
                                           {value:"+str(len(shijing))+", name:'石井街道'}]"})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入起止日�?"})

def jiedaominshengshijian(request):
    if request.method == 'GET':
        startDate = int(request.GET.get('startDate'))
        endDate = int(request.GET.get('endDate'))
        if startDate and endDate:
            startYear = startDate/10000
            startMonth = (startDate%10000)/100
            startDay = startDate%100
            endYear = endDate/10000
            endMonth = (endDate/10000)%100
            endDay = endDate%100
            date_from = datetime(startYear, startMonth, startDay, 0, 0)
            date_to = datetime(endYear, endMonth, endDay, 0, 0)
            request_list = PeopleRequest.objects.filter(create_time__range=(date_from, date_to))
            return JsonResponse({"status":1,"data":"[{\
                name:'市�?�城�?',\
                type:'bar',\
                stack:'事件数目',\
                data:" + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 1159]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '教育体制',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 1019]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '服务行业废气扰民',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 140]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '宣传广告违法行为',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 180 ]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '占道经营',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 178]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '车辆乱停�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 179]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '废弃物堆�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 177]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '垃圾�?�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 172]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '工业�?�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 132]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '刑�?�侦�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 130]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '�?用部�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 185]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '�?共�?�施保洁',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 175]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '绿化养护',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 176]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '其他市�?�违法�?�为或影响市容�?�件',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 181]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '住房保障和房地产',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 162]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '城市�?共资源�?�理',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 187]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '�?共交通�?�理',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 193]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '宣传舆�??',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 1002]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '建筑施工�?�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 133]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '社会生活�?�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 137]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '集体土地上房屋拆迁与补偿',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 966]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '道路交通安�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 27]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '人力资源',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 1047]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '禽畜养殖污染',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 138]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '物业服务管理监督',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 117]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '地质安全',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 60]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '商业经营�?�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 134]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '市政、公共�?�施设置及维�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 186]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '�?�?设施设置及维�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 182]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '行政能效',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 100]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '医政监�??',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 1007]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '表达情感',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 938]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '供、排水及水质�?�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 152]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '消费维权',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 61]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '线路消防安全',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 23]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '警务监督',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 129]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '水污�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 141]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '社会组织',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 107]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '劳动就业',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 34]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '互联网与通�??',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 59]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '军转安置',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 89]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '双拥优抚',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 795]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '住宅区（�?区）或建筑物内安全、环�?�?�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 120]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '�?尘污�?',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 142]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "},{\
                name: '无证无照经营',\
                type: 'bar',\
                stack: '事件数目',\
                data: " + str([len([i for i in request_list if i.community_id == x and i.main_type_id == 46]) for x in [1500,1801,1772,8532,1920,1536]]) + 
                "}]"})
        else:
            return JsonResponse({"status": 0,
                                 "msg": "请输入起止日�?"})

# def yuceshuju(request):
#     if request.method == 'GET':
#         month_index = []
#         tousu = []
#         ganxie = []
#         zixun = []
#         qiujue = []
#         qita = []
#         jianyi = []
#         for month in range(6,11):
#             month_index.append(month)
#             date_from = datetime(2018, month, 1, 0, 0)
#             date_to = datetime(2018, month+1, 1, 0, 0)
#             request_list = PeopleRequest.objects.filter(create_time__range=(date_from, date_to))
#             tousu.append(len([i for i in request_list if i.event_property_name == "投诉"]))
#             ganxie.append(len([i for i in request_list if i.event_property_name == "感谢"]))
#             zixun.append(len([i for i in request_list if i.event_property_name == "咨询"]))
#             qiujue.append(len([i for i in request_list if i.event_property_name == "求决"]))
#             qita.append(len([i for i in request_list if i.event_property_name == "其他"]))
#             jianyi.append(len([i for i in request_list if i.event_property_name == "建议"]))
#         return JsonResponse({"status": 1, 
#                              "index":str(month_index),
#                              "data": "[{value:"+str(tousu)+", name:'投诉'},\
#                                        {value:"+str(ganxie)+", name:'感谢'},\
#                                        {value:"+str(zixun)+", name:'咨询'},\
#                                        {value:"+str(qiujue)+", name:'求决'},\
#                                        {value:"+str(qita)+", name:'其他'},\
#                                        {value:"+str(jinayi)+", name:'建议'}]"})

def weijieban(request):
    if request.method == 'GET':
        date_from = datetime(2018, 10, 30, 0, 0)
        date_to = datetime(218, 10, 31, 0, 0)
        request_list = PeopleRequest.objects.filter(create_time__range=(date_from, date_to))
        weijieban = [i for i in request_list if i.intime_to_achieve_num == 0]
        return JsonResponse({"status": 1, 
                             "data": "str(weijieban)"})

def nextday(tuple):
    if tuple[1] == 31 or (tuple[1] == 30 and (tuple[0] == 6 or tuple[0] == 9)):
        return (tuple[0]+1, 1)
    else:
        return (tuple[0], tuple[1]+1)

def nextweek(tuple):
    return nextday(nextday(nextday(nextday(nextday(nextday(nextday(tuple)))))))

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
        month = 2
        day = 8
        while(month != 10 or day != 30):
            nmonth = nextday((month, day))[0]
            nextday = nextday((month, day))[1]
            date_from = datetime(2018, month, day, 0, 0)
            date_to = datetime(2018, nmonth, nday, 0, 0)
            request_list = PeopleRequest.objects.filter(create_time__range=(date_from, date_to))
            for community in communities:
                if len([i for i in request_list if i.community_name == community]) >= 10:
                    abnormals.append({"create_time": str(2018)+str(month)+str(day),
                                      "community_name": community})

        return JsonResponse({"status": 1, 
                             "msg": "当天该社区事件数目超出阈值",
                             "data": str(abnormals)})

from pro import pro
def yuce(request):
    if request.method == 'GET':
        begin_date = (9, 25)
        tousu = []
        ganxie = []
        zixun = []
        qiujue = []
        qita = []
        jianyi = []
        for x in range(5):
            date_from = datetime(2018, begin_date[0], begin_date[1], 0, 0)
            date_to = datetime(2018, nextweek(begin_date)[0], nextweek(begin_date)[1], 0, 0)
            request_list = PeopleRequest.objects.filter(create_time__range=(date_from, date_to))
            tousu[x] = len([i for i in request_list if i.event_property_name == "投诉"])
            ganxie[x] = len([i for i in request_list if i.event_property_name == "感谢"])
            zixun[x] = len([i for i in request_list if i.event_property_name == "咨询"])
            qiujue[x] = len([i for i in request_list if i.event_property_name == "求决"])
            qita[x] = len([i for i in request_list if i.event_property_name == "其他"])
            jianyi[x] = len([i for i in request_list if i.event_property_name == "建议"])
            return JsonResponse({"status": 1, 
                                 "data": str(pro(ganxie, zixun, jianyi, qiujue, tousu, qita))})