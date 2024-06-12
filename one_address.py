from urllib.request import urlopen,quote
import json

 
address="湖北省武汉市武汉大学"
ak='D4cxteM0Ke1bkKlq9ri6oIByefDYApvV'
url='http://api.map.baidu.com/geocoding/v3/?address='
output = 'json'
#http://api.map.baidu.com/geocoding/v3/?address=北京市海淀区上地十街10号&output=json&ak=您的ak&callback=showLocation
add = quote(address) #本文城市变量为中文，为防止乱码，先用quote进行编码
url2 = url+add+'&output='+output+'&ak='+ak+'&ret_coordtype=gcj02ll'
req = urlopen(url2)
res  = req.read().decode()
temp = json.loads(res)
print(temp)
lng = temp['result']['location']['lng']  # 获取经度
lat = temp['result']['location']['lat']  # 获取纬度
list1=[lng,lat]
print('百度坐标为：',list1)