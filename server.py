import requests
import os
import websocket#<-----懒得写了
import json




##                            _ooOoo_
##                           o8888888o
##                           88" . "88
##                           (| -_- |)
##                            O\ = /O
##                        ____/`---'\____
##                      .   ' \\| |// `.
##                       / \\||| : |||// \
##                     / _||||| -:- |||||- \
##                       | | \\\ - /// | |
##                     | \_| ''\---/'' | |
##                      \ .-\__ `-` ___/-. /
##                   ___`. .' /--.--\ `. . __
##                ."" '< `.___\_<|>_/___.' >'"".
##               | | : `- \`.;`\ _ /`;.`/ - ` : | |
##                 \ \ `-. \_ __\ /__ _/ .-` / /
##         ======`-.____`-.___\_____/___.-`____.-'======
##                            `=---='
##
##         .............................................
##                  佛祖镇楼                  
##          佛曰:
##                  写字楼里写字间，写字间里程序员；
##                  程序人员写程序，又拿程序换酒钱。
##                酒醒只在网上坐，酒醉还来网下眠；
##                  酒醉酒醒日复日，网上网下年复年。
##                  但愿老死电脑间，不愿鞠躬老板前；
##                  奔驰宝马贵者趣，公交自行程序员。
##                  别人笑我忒疯癫，我笑自己命太贱；
##                  不见满街漂亮妹，哪个归得程序员？



#    def on_open(ws):
 #       print("Connection opened")
  ## 
    ## 定义接收到服务器消息时的回调函数 
    #def on_message(ws_cenc, message):
    #    receive_cenc = {message}
    #    if receive_cenc['type'] == "cenc_eqlist":
    #        print("有效内容")
    #    else:
    #        print(receive_cenc['type'])
   #
    # 定义连接关闭时的回调函数 
    #def on_close(ws_cenc):
    #    print("Connection closed")
    
    # 定义遇到错误时的回调函数 
    #def on_error(ws_cenc, error):
    #    print(f"Error occurred: {error}")
    
    # 创建WebSocket连接 
    #ws_cenc = websocket.WebSocketApp("wss://ws-api.wolfx.jp/cenc_eqlist", 
     #                           on_open=on_open,
      #                          on_message=on_message,
       #                        on_error=on_error)
    
    # 消息：{message}

#    print("EQTTS - SERVER v0.0.1_Pre-1 by Luyii")
 #  ws_cenc.run_forever()
  #  while(ture):
   #     ws_cenc.send = "query_cenceqlist"
    #    sleep(200)

def get_cenc():

    url_CENC = "https://api.wolfx.jp/cenc_eqlist.json"
    print("请求API...")
    try:#屎山02
        rec_cenc = requests.get(url_CENC)#屎山02
    except rec_cenc.status_code != 200:#屎山02
        print("请求失败:{response.status_code}")#屎山02
    except requests.exceptions.ConnectionError:#屎山02
        print("无网络连接?")#屎山02

    json_CENC = rec_cenc.json() 

def jiexi():
    no1 = json_CENC["No1"]
    location_newest = no1["location"]
    magnitude_newest = no1["magnitude"]
    intensity_newest = no1["intensity"]
    type_newest = no1["type"]
    if type_newest == "reviewed":
        saytype_newest = "正式测定"
    else:
        saytype_newest = "自动测定"    
    语言组织 = "中国地震台网",saytype_newest,",震中在",location_newest,",规模",magnitude_newest,",预估最大烈度",intensity_newest,"度."
    print(语言组织)

def getTTS():
    print("获取朗读音频...")
    com_t1 = "edge-tts --voice zh-CN-YunyangNeural --text  ",语言组织,"  --write-media tts.mp3"
    os.system(str(com_t1))

def checkold():#屎山03
    print("检查历史缓存")#屎山03
    try:#屎山03
        with open('lastest.ini',  'r') as file:#屎山03
            lastest = file.read()#屎山03
    except FileNotFoundError:#屎山03
        print("No Such File,Creative")#屎山03
        file.write(str(no1))#屎山03

print("EQTTS - SERVER v0.0.1_Pre-1 by Luyii")
print("GitHub:luyii-code-1")
print("WebSite:https://luyii.cn")
print("BiliBili:luyii-code")
print("Mail:root@luyii.cn")
print("Please use GitHub Issuse to report bugs. The exception to the Mountain code!")

#初始化
#屎山#01
print("初始化...")
url_CENC = "https://api.wolfx.jp/cenc_eqlist.json"
try:
    rec_cenc = requests.get(url_CENC)
except rec_cenc.status_code != 200:#屎山02
    print("请求失败:{response.status_code}")#屎山02
except requests.exceptions.ConnectionError:#屎山02
        print("无网络连接?")#屎山02
json_CENC = rec_cenc.json() 
no1 = json_CENC["No1"]
location_newest = no1["location"]
magnitude_newest = no1["magnitude"]
intensity_newest = no1["intensity"]
type_newest = no1["type"]
#屎山#01
#print("检查历史缓存")#屎山03
#try:#屎山03
#    with open('lastest.ini',  'r') as file:#屎山03
#        lastest = file.read()#屎山03
#except FileNotFoundError:#屎山03
#    print("No Such File,Creative")#屎山03
#    # file.write(str(no1))#屎山03
#if lastest != no1:#屎山03
#    newstatus = 0#屎山03
#else:#屎山03
#    newstatus = 1#屎山03
#    # file.write(str(no1))#屎山03 ?没有实现效果，懒得删了~
no1 = json_CENC["No1"]
location_newest = no1["location"]
magnitude_newest = no1["magnitude"]
intensity_newest = no1["intensity"]
type_newest = no1["type"]
if type_newest == "reviewed":
    saytype_newest = "正式测定"
else:
    saytype_newest = "自动测定"    
语言组织 = "中国地震台网",saytype_newest,",震中在",location_newest,",规模",magnitude_newest,",预估最大烈度",intensity_newest,"度."
print(语言组织)

######这里才是程序开始######
print("启动服务")
get_cenc()
jiexi()
getTTS()