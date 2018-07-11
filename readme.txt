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
#       self.jxl_list = ["101","105"]                    		教学楼编号，目前考虑实际只提供理科楼（101），文科楼（105），图书馆将在另外的服务提供
#       Sel_XNXQ                                             	表单中规定的“学年学期”，目前为20171，开学后为20180
#       rad_gs                                                  表单中的格式要求：默认为1
#       txt_yzm/imgCode                                			表单中规定的验证码
#       Sel_XQ                                                 	表单中学区，默认为坞城校区
#       Sel_JXL                                                 表单中的教学楼
#       Sel_ROOM                                           	 	表单中的教室
#
