#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-
#
#
#author: Vophan Lee
#date:18/7/11
#
#
#环境：python3.6
#依赖库：urllib,re,bs4,sys,http,imgcodeidentify,PIL,aip
#调用sxufreesite类的main方法,即可
#类的final_list成员为最终结果，该list中包含许多dictionary，每个dictionary的key为教室代号，value值为一个list，list中有所有空教室信息
#
#注意：该程序需要在连接vpn的情况使用，如果没有连接vpn，会出现无法响应的情况
#      该程序验证码自动识别使用了百度ai的api,每天500次查询机会，需要安装aip库获得支持
#      空教室查询每十次查询会换sessionid，需要重新验证验证码
#      该程序将降噪脚本运行了30次，来提高识别准确率，但同时降低了程序的速度，如果要提高速度，可以减少降噪算法的运行次数
#      降噪方法在imgidentity.py中，如需调用记得import
#      返回的list的最终结果是（星期，课程），具体应用是可以在前端对用户的时间进行获取判断，从而得到空教室的个数
#相应参数解释：
#       self.jxl_list = ["101","105"]                  教学楼编号，目前考虑实际只提供理科楼（101），文科楼（105），图书馆将在另外的服务提供
#       Sel_XNXQ                                       表单中规定的“学年学期”，目前为20171，开学后为20180
#       rad_gs                                         表单中的格式要求：默认为1
#       txt_yzm/imgCode                                表单中规定的验证码
#       Sel_XQ                                         表单中学区，默认为坞城校区
#       Sel_JXL                                        表单中的教学楼
#       Sel_ROOM                                       表单中的教室
#
from urllib import request as rq
import re
from bs4 import BeautifulSoup
import urllib.parse
import sys
from http import cookiejar
import imgcodeidentify
from PIL import Image
from aip import AipOcr

class sxufreesite:
    index_url = ""
    class_url = ""
    usrname = ""
    password = ""
    header = ""
    table = ""
    values = {}
    tr_list = []
    td_list = []
    class_list = []
    js_list = []
    jxl_list_101 = []
    jxl_list_102 = []
    final_list = []
    APP_ID = '11519354'
    API_KEY = 'tLlZhgC4kwx8ArqEhBXzCvRw'
    SECRET_KEY = 'GnpZ0XXBFgZXz8v0aYTGIMhHRMmlRKSd'
    def __init__(self):
        self.index_url = "http://bkjw.sxu.edu.cn/"
        self.class_url = "http://bkjw.sxu.edu.cn/ZNPK/KBFB_RoomSel.aspx"
        self.header = {
        "Host":"bkjw.sxu.edu.cn",
        "Origin":"http://bkjw.sxu.edu.cn",
        "Referer":"http://bkjw.sxu.edu.cn/ZNPK/KBFB_RoomSel.aspx",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

        }
        self.jxl_list = ["101","105"]
        self.js_list_101 = ["1010101","1010102","1010103","1010104","1010105","1010106","1010107","1010108","1010109","1010110","1010111","1010112","1010113","1010114","1010115","1010201","1010202","1010203","1010204","1010205","1010206","1010207","1010208","1010301","1010302","1010303","1010304","1010305","1010306","1010307","1010308","1010401","1010402","1010501","1010502","1010503","1010504","1010505","1010506","1010507","1010508","1010509","1010510","1010511"]
        self.jxl_list_105 = ['1050101', '1050102', '1050103', '1050104', '1050105', '1050106', '1050107', '1050108', '1050109', '1050110', '1050111', '1050112', '1050113', '1050114', '1050115', '1050116','1050201', '1050202', '1050203', '1050204', '1050205', '1050206', '1050207', '1050208', '1050209','1050211', '1050212', '1050213', '1050214', '1050215', '1050216', '1050217', '1050218','1050301', '1050302', '1050303', '1050304', '1050305', '1050306', '1050307', '1050308', '1050309','1050310','1050311', '1050312', '1050313', '1050314', '1050315', '1050316', '1050317','1050401', '1050402', '1050403', '1050404', '1050405', '1050406', '1050407', '1050408', '1050409','1050501','1050502','1050503','1050504','1050505']
        self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def get_img_code(self):
        cookie = cookiejar.CookieJar()
        handler=rq.HTTPCookieProcessor(cookie)
        opener = rq.build_opener(handler)
        req = rq.Request("http://bkjw.sxu.edu.cn/sys/ValidateCode.aspx",headers=self.header)
        with opener.open(req) as gec:
            # print(cookie)
            name = "imgCode.jpg"
            img_res = gec.read()
            with open(name,"wb") as ic:
                ic.write(img_res)

        return opener
    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            result = fp.read()
            return result
    def post_data(self,opener,Sel_XNXQ,rad_gs,imgcode,Sel_XQ,Sel_JXL,Sel_ROOM):
        self.values["Sel_XNXQ"] = Sel_XNXQ 
        self.values["rad_gs"] = rad_gs     
        self.values["txt_yzm"] = imgcode   
        self.values["Sel_XQ"] = Sel_XQ     
        self.values["Sel_JXL"] = Sel_JXL   
        self.values["Sel_ROOM"] = Sel_ROOM 
        data = urllib.parse.urlencode(self.values).encode('GB18030')
        request = rq.Request("http://bkjw.sxu.edu.cn/ZNPK/KBFB_RoomSel_rpt.aspx", data, self.header)
        html = opener.open(request).read().decode('GB18030')
        reg = re.compile("<tr.*>.*</tr>")
        self.table = reg.findall(html)[0]
        # print(self.table)

        # with open("1.html","w") as ht:
        #     ht.write(html)
        # print(html)
        return html
    def recommend_class(self):
        EmptyClassList = []
        for i in range(5):
            for j in range(7):
                if self.tr_list[i][j] == "":
                    t = (j+1,i+1)
                    EmptyClassList.append(t)
                    print("该教室星期"+str(j+1)+"第"+str(i+1)+"节课为空教室")
        return EmptyClassList

    def deal_table(self,html):
        soup = BeautifulSoup(html,"html5lib")
        td_list = soup.findAll(valign = "top")
        tr_list1 = []
        tr_list2 = []
        tr_list3 = []
        tr_list4 = []
        tr_list5 = []
        count = 1
        for i in td_list:
            if count <= 7:
                tr_list1.append(i.text)
            elif count <=14 and count >=8:
                tr_list2.append(i.text)
            elif count <=21 and count >=15:
                tr_list3.append(i.text)
            elif count <=28 and count >=22:
                tr_list4.append(i.text)
            elif count <=35 and count >=29:
                tr_list5.append(i.text)
            else:
                pass
            count = count + 1
        self.tr_list.append(tr_list1)
        self.tr_list.append(tr_list2)
        self.tr_list.append(tr_list3)
        self.tr_list.append(tr_list4)
        self.tr_list.append(tr_list5)
    def main(self):#,xq,time
        count = 0
        for i in self.js_list_101: 
            while True:         
                if count%10 == 0:
                    opener = self.get_img_code()
                    for j in range(30):
                        imgcodeidentify.deal_img("imgCode.jpg")
                        imgcodeidentify.interference_line(imgcodeidentify.deal_img("imgCode.jpg"),"imgCode.jpg")
                        imgcodeidentify.interference_point(imgcodeidentify.interference_line(imgcodeidentify.deal_img("imgCode.jpg"),"imgCode.jpg"),"imgCode.jpg")
                    try:
                        code = self.client.basicGeneral(self.get_file_content("imgCode.jpg"))["words_result"][0]["words"]
                    except IndexError:
                        continue
                    #self.client.basicGeneral(self.get_file_content("imgCode.jpg"))["words_result"][0]["words"]
                    code = code.replace(" ","")
                    print(code)

                    # input("请输入验证码\n")
                try:
                    html = self.post_data(opener,"20171","1",code,"1","101",i)
                except IndexError:
                    continue
                else:
                    self.deal_table(html)
                    temp_list = self.recommend_class()
                    temp_dict = {}
                    temp_dict[str(i)] = temp_list
                    self.final_list.append(temp_dict)
                    # print("理科楼"+str(i)+"教室查询完毕")
                    count = count + 1
                    break
                
sfs = sxufreesite()
sfs.main()
print(sfs.final_list)

