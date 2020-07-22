import requests
import time
import hashlib

def get_md5(line):
    m = hashlib.md5()
    m.update(line.encode())
    return m.hexdigest()

udid = 'IMEI354013070175612-IMSI460010901112928'
str_time = round(time.time())
print(str_time)
params = 'f1190aca-d08e-4041-8666-29931cd89dde'
line = '%s&&%s&&%s' % (udid, str_time, params)
signature = get_md5(line)
print(signature)

url = 'https://app.suzhou-news.cn/api/v1/appNews/getBannerNewsList7?page=1&bannerID=12'
headers = {
    "timestamp": "%s" % str_time,
    "authority": "app.suzhou-news.cn",
    "udid": "IMEI354013070175612-IMSI460010901112928",
    "signature": "%s" % signature
}
data = requests.get(url, headers=headers)
print(data.content.decode('utf-8'))
