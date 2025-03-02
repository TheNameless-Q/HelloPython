import requests
url='https://www.weather.com.cn/weather1d/101010100.shtml'#将后缀的#search删除
resp=requests.get(url)#打开浏览器并打开网址，得到一个响应
#设置编码格式
resp.encoding='utf-8'
print(resp.text)

###本程序未完成，详见P137
