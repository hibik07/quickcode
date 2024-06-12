from urllib.request import urlopen,quote
import json
import time
import math

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方

AddressAll=[]
AddressError=[]
#AddressResult=[]
with open("C:\\Users\\lenovo\\Desktop\\addressover.txt", encoding='utf-8') as f: 
    for line in f.readlines():
        AddressAll.append(line)
data=open("C:\\Users\\lenovo\\Desktop\\addressresult.txt",'w+') 
dataerror=open("C:\\Users\\lenovo\\Desktop\\addressERROR.txt",'w+') 
#所有文件地址需要依据需求进行修改

def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret

def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度·
    :return:
    """
    #if out_of_china(lng, lat):
        #return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


for address in AddressAll:
    ak='D4cxteM0Ke1bkKlq9ri6oIByefDYApvV'
    url='http://api.map.baidu.com/geocoding/v3/?address='
    output = 'json'
    add = quote(address) #本文城市变量为中文，为防止乱码，先用quote进行编码
    url2 = url+add+'&output='+output+'&ak='+ak+'&ret_coordtype=gcj02ll'
    req = urlopen(url2)
    res  = req.read().decode()
    temp = json.loads(res)
    print(temp)
    if temp['status']==0:
        lng = temp['result']['location']['lng']  # 获取经度
        lat = temp['result']['location']['lat']  # 获取纬度
        list1=[lng,lat]
        listwgs84=gcj02_to_wgs84(list1[0],list1[1])
        #print(address,'坐标：',list1)    
        strNums=[str(x) for x in listwgs84]
        #AddressResult.append(list1)
        print(listwgs84,file=data)
    else:
        AddressError.append(address)
        print('N/A',file=data)
        print(address,file=dataerror)
    #time.sleep(0.1)

print(AddressError)
data.close()
dataerror.close()   

