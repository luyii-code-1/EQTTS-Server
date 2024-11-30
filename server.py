import requests
import websocket
import json

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
def jiexi():
    no1 = json_CENC["No1"]
    print(no1)
    location_newest = no1["location"]
    magnitude_newest = no1["magnitude"]
    intensity_newest = no1["intensity"]
    type_newest = no1["type"]

print("EQTTS - SERVER v0.0.1_Pre-1 by Luyii")

url_CENC = "https://api.wolfx.jp/cenc_eqlist.json"

rec_cenc = requests.get(url_CENC)
json_CENC = rec_cenc.json() 
jiexi()

