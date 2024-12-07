import requests
import os
import time

# 定义常量
URL_CENC = "https://api.wolfx.jp/cenc_eqlist.json"
LANGUAGE_KEY = 'No1'

# 打印信息
def print_welcome():
    print("EQTTS - SERVER v0.0.1_Pre-1 by Luyii")
    print("GitHub: luyii-code-1")
    print("WebSite: https://luyii.cn")
    print("BiliBili: luyii-code")
    print("Mail: root@luyii.cn")
    print("Please use GitHub Issues to report bugs. The exception to the Mountain code!")

# 获取API数据
def get_cenc():
    print("请求API...")
    try:
        response = requests.get(URL_CENC)
        response.raise_for_status()  # 如果请求失败，会抛出异常
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

# 解析地震信息
def parse_data(json_data):
    if json_data is None:
        return None
    
    no1 = json_data.get(LANGUAGE_KEY, {})
    location = no1.get("location", "未知位置")
    magnitude = no1.get("magnitude", "未知")
    intensity = no1.get("intensity", "未知")
    type_newest = no1.get("type", "未知")
    
    if type_newest == "reviewed":
        say_type = "正式测定"
    else:
        say_type = "自动测定"
    
    return f'中国地震台网{say_type},震中在{location},规模{magnitude}级,预估最大烈度{intensity}度.'

# 获取并生成TTS
def get_tts(text):
    print("获取朗读音频...")
    command = f"edge-tts --voice zh-CN-YunyangNeural --text \"{text}\" --write-media tts.mp3"
    print(command)
    os.system(command)

# 检查历史缓存
def check_old_data():
    try:
        with open('lastest.ini', 'r') as file:
            lastest = file.read()
        return lastest
    except FileNotFoundError:
        print("No Such File, Creating New File.")
        return None

# 更新历史缓存
def update_old_data(data):
    with open('lastest.ini', 'w') as file:
        file.write(str(data))

# 主功能
def main_loop():
    print_welcome()
    
    prev_data = None
    while True:
        json_data = get_cenc()
        parsed_data = parse_data(json_data)
        
        if parsed_data != prev_data:
            print("新数据获取成功！")
            get_tts(parsed_data)
            prev_data = parsed_data
            update_old_data(parsed_data)
        else:
            print("无新数据，等待1秒...")
        
        time.sleep(2)  # 每隔2秒检查一次

if __name__ == "__main__":
    main_loop()
