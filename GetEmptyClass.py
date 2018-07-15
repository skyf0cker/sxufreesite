
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
<<<<<<< HEAD
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
#
#更新：
#		成绩查询功能
#		输入学号和密码就好
#		
#		现在参数设计仍为2017-2018学年第一学期
#		下学期需要手动修改参数，具体为post_score中的url,和data
#		
#		
#		
=======
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
>>>>>>> c348e0332df71cf01975514991684bca154627bc
#
#
import threading
from urllib import request as rq
import re
from bs4 import BeautifulSoup
import urllib.parse
import sys
from http import cookiejar
import imgcodeidentify
from PIL import Image
from aip import AipOcr
import hashlib
from selenium import webdriver
import time
import datetime


class sxufreesite:
<<<<<<< HEAD
	index_url = ""
	class_url = ""
	score_url = ""
	usrname = ""
	password = ""
	header = ""
	table = ""
	cookie = ""
	handler = ""
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
		self.score_url = "http://bkjw.sxu.edu.cn/_data/login.aspx"
		self.cookie = cookiejar.CookieJar()
		self.handler = rq.HTTPCookieProcessor(self.cookie)
		self.opener = rq.build_opener(self.handler)
		self.header = {
		"Host":"bkjw.sxu.edu.cn",
		"Origin":"http://bkjw.sxu.edu.cn",
		"Content-Type":"application/x-www-form-urlencoded",
		"Referer":"http://bkjw.sxu.edu.cn/_data/login.aspx",
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

		}
		self.header2 = {
		"Host":"bkjw.sxu.edu.cn",
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Language":"zh-CN,zh;q=0.8",
		"Accept-Encoding":"gzip, deflate",
		"Referer":"http://bkjw.sxu.edu.cn/xscj/Stu_MyScore.aspx",
		"Content-Type":"application/x-www-form-urlencoded",
		"Content-Length":"76",
		"Cookie":"",
		"Connection":"keep-alive",
		"Upgrade-Insecure-Requests":"1"
		}
		self.jxl_list = ["101","105"]
		self.js_list_101 = ["1010101","1010102","1010103","1010104","1010105","1010106","1010107","1010108","1010109","1010110","1010111","1010112","1010113","1010114","1010115","1010201","1010202","1010203","1010204","1010205","1010206","1010207","1010208","1010301","1010302","1010303","1010304","1010305","1010306","1010307","1010308","1010401","1010402","1010501","1010502","1010503","1010504","1010505","1010506","1010507","1010508","1010509","1010510","1010511"]
		self.jxl_list_105 = ['1050101', '1050102', '1050103', '1050104', '1050105', '1050106', '1050107', '1050108', '1050109', '1050110', '1050111', '1050112', '1050113', '1050114', '1050115', '1050116','1050201', '1050202', '1050203', '1050204', '1050205', '1050206', '1050207', '1050208', '1050209','1050211', '1050212', '1050213', '1050214', '1050215', '1050216', '1050217', '1050218','1050301', '1050302', '1050303', '1050304', '1050305', '1050306', '1050307', '1050308', '1050309','1050310','1050311', '1050312', '1050313', '1050314', '1050315', '1050316', '1050317','1050401', '1050402', '1050403', '1050404', '1050405', '1050406', '1050407', '1050408', '1050409','1050501','1050502','1050503','1050504','1050505']
		self.client = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY)

	def get_img_code(self):
		req = rq.Request("http://bkjw.sxu.edu.cn/sys/ValidateCode.aspx",headers=self.header)
		with self.opener.open(req) as gec:
        # print(cookie)
			name = "imgCode.jpg"
			img_res = gec.read()
		with open(name,"wb") as ic:
			ic.write(img_res)
			print(self.cookie)



	# def get_score(self):
	# 	username = "201701003091"
	# 	password = "326824"
		# cookies = {}
		# for item in self.cookies:
		# 	cookies["name"] = item.name
		# 	cookies["value"] = item.value
		# cookies["domain"] = ".bkjw.sxu.edu.cn"
		# cookies["path"] = "/"
		# cookies["expires"] = None
		# browser2 = webdriver.PhantomJS()
		# # browser2.get("http://bkjw.sxu.edu.cn/sys/ValidateCode.aspx")
		# # ck2 = browser2.get_cookies()
		# # print(ck2)
		# browser = webdriver.PhantomJS()
		# browser.get("http://bkjw.sxu.edu.cn")
		# browser.delete_all_cookies()
		# browser.add_cookie(cookies)
		# browser.refresh()
		# browser.switch_to.frame(0)
		# browser.find_element_by_id("txt_asmcdefsddsd").send_keys(username)
		# browser.find_element_by_id("txt_pewerwedsdfsdff").send_keys(password)
		# browser.find_element_by_id("txt_sdertfgsadscxcadsads").click()
		# a = browser.get_screenshot_as_file("1.jpg")
		# im = Image.open("1.jpg")

		# box = (145,278,224,298)
		# region = im.crop(box)
		# region2 = region.convert("RGB")
		# region2.save("imgCode.jpg")
		# browser.add_cookie(cookies)

		# for j in range(20):
		# 	imgcodeidentify.deal_img("imgCode.jpg")
		# 	imgcodeidentify.interference_line(imgcodeidentify.deal_img("imgCode.jpg"),"imgCode.jpg")
		# 	imgcodeidentify.interference_point(imgcodeidentify.interference_line(imgcodeidentify.deal_img("imgCode.jpg"),"imgCode.jpg"),"imgCode.jpg")
		# code = self.client.basicGeneral(self.get_file_content("imgCode.jpg"))["words_result"][0]["words"]
		# browser.find_element_by_id("txt_sdertfgsadscxcadsads").send_keys(code)
		# ck = browser.get_cookies()

		# print(ck)
		# time.sleep(5)
		# browser.get_screenshot_as_file("1.jpg")




	def get_score(self,opener,username,password,yzm):

		h1 = hashlib.md5()

		h1.update(password.encode(encoding='utf-8'))

		hex_password = h1.hexdigest()

		temp_pwd = username+hex_password[:30].upper()+"10108"

		h2 = hashlib.md5()

		h2.update(temp_pwd.encode(encoding='utf-8'))

		hex_temp = h2.hexdigest()

		dsdsdsdsdxcxdfgfg = hex_temp[:30].upper()   #密码

		txt_asmcdefsddsd = username                 #用户名

		h3 = hashlib.md5()

		h3.update(yzm.upper().encode(encoding='utf-8'))

		hex_temp_yzm = h3.hexdigest()[:30].upper()+'10108'

		h4 = hashlib.md5()

		h4.update(hex_temp_yzm.encode(encoding='utf-8'))

		fgfggfdgtyuuyyuuckjg = h4.hexdigest()[:30].upper()  #验证码

		__VIEWSTATE = "dDwyMTIyOTQxMzM0Ozs+AI2AQlMGeOYvPjA1fJfST57PPCk="

		pcInfo = "Mozilla/5.0+(Windows+NT+10.0;+Win64;+x64;+rv:61.0)+Gecko/20100101+Firefox/61.0Windows+NT+10.0;+Win64;+x645.0+(Windows)+SN:NULL"

		Sel_Type = "STU"

		typeName = "学生"
		values = {}
		values["__VIEWSTATE"] = __VIEWSTATE
		values["dsdsdsdsdxcxdfgfg"] = dsdsdsdsdxcxdfgfg
		values["fgfggfdgtyuuyyuuckjg"] = fgfggfdgtyuuyyuuckjg
		values["pcInfo"] = pcInfo
		values["Sel_Type"] = Sel_Type
		values["txt_asmcdefsddsd"] = txt_asmcdefsddsd
		values["txt_pewerwedsdfsdff"] = ""
		values["txt_sdertfgsadscxcadsads"] = ""
		values["typeName"] = typeName
		
		data = urllib.parse.urlencode(values).encode('gb2312')            #GB18030

		req = rq.Request(self.score_url,data,headers=self.header)
		
		html = self.opener.open(req).read().decode('gb2312')

		print(data)
		print(html)

		# http://bkjw.sxu.edu.cn/xscj/Stu_MyScore_rpt.aspx
		# http://bkjw.sxu.edu.cn/xscj/Stu_MyScore_Drawimg.aspx?x=1&h=2&w=782&xnxq=20171&xn=2017&xq=1&rpt=1&rad=2&zfx=0&xh=201700004159
	def post_score(self,opener):
		# sel_xn=2017&sel_xq=1&SJ=1&btn_search=%BC%EC%CB%F7&SelXNXQ=2&zfx_flag=0&zxf=0
		data = "sel_xn=2017&sel_xq=1&SJ=1&btn_search=%BC%EC%CB%F7&SelXNXQ=2&zfx_flag=0&zxf=0".encode('GB18030')
		for item in self.cookie:
			self.header2["Cookie"] = item.name+'='+item.value
		print(self.header2)
		head2 = urllib.parse.urlencode(self.header2).encode('utf-8')
		request = rq.Request("http://bkjw.sxu.edu.cn/xscj/Stu_MyScore_Drawimg.aspx?x=1&h=2&w=782&xnxq=20171&xn=2017&xq=1&rpt=1&rad=2&zfx=0&xh=201700004159",head2)#,data   self.header2
		html = self.opener.open(request).read()
		with open("score.jpg","wb") as jpg:
			jpg.write(html)
		print(html)
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
		html = self.opener.open(request).read().decode('GB18030')
		reg = re.compile("<tr.*>.*</tr>")
		self.table = reg.findall(html)[0]
		return html
	def recommend_class(self):
		EmptyClassList = []
		for i in range(5):
			for j in range(7):
				if self.tr_list[i][j] == "":
					t = (j+1,i+1)
					EmptyClassList.append(t)
					print("¸Ã½ÌÊÒÐÇÆÚ"+str(j+1)+"µÚ"+str(i+1)+"½Ú¿ÎÎª¿Õ½ÌÊÒ")
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

		                # input("ÇëÊäÈëÑéÖ¤Âë\n")
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
						# print("Àí¿ÆÂ¥"+str(i)+"½ÌÊÒ²éÑ¯Íê±Ï")
						count = count + 1
						break




sfs = sxufreesite()
sfs.get_img_code()
for j in range(30):
	imgcodeidentify.deal_img("imgCode.jpg")
	imgcodeidentify.interference_line(imgcodeidentify.deal_img("imgCode.jpg"),"imgCode.jpg")
	imgcodeidentify.interference_point(imgcodeidentify.interference_line(imgcodeidentify.deal_img("imgCode.jpg"),"imgCode.jpg"),"imgCode.jpg")
code = input("code:")
# code = sfs.client.basicGeneral(sfs.get_file_content("imgCode.jpg"))["words_result"][0]["words"]
#self.client.basicGeneral(self.get_file_content("imgCode.jpg"))["words_result"][0]["words"]
# code = code.replace(" ","")
print(code)
opener = sfs.get_score(sfs.opener,"201701003091","326824",code)
print(sfs.cookie)
sfs.post_score(sfs.opener)




# sfs.get_score()
# sfs.main()
# print(sfs.final_list)

