file = open("/data/misc/wifi/WifiConfigStore.xml")
wifi_str = file.readline()
while wifi_str:
    if ("PreSharedKey" in wifi_str) and (not("null" in wifi_str)):
        print("WIFI密码："+wifi_str[34:(wifi_str.rfind('&'
        ))])
        print("====================")
    elif ("ConfigKey" in wifi_str):
        admin = wifi_str[31:(wifi_str.rfind('<'))].split('&quot;')
        print("WIFI账号："+admin[0])
        print("WIFI类型："+admin[1])
    elif ("PreSharedKey" in wifi_str) and ("null" in wifi_str):
        print("该WIFI没有密码！")
        print("====================")
        
    wifi_str = file.readline()
file.close()
