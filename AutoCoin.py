import urllib.request
import urllib.parse
import json
import time

# 在这里填你的csrt效验码
csrf=''
# 在这里填上你的b站cookie
cookie=""

def SeadAdd(Avcode,cookie,csrf):
    url = 'https://api.bilibili.com/x/web-interface/coin/add'
    formdata={'aid':Avcode,'multiply':'1','select_like':'1','cross_domain':'true','csrf':csrf}
    header={
    "Host": "api.bilibili.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Connection": "keep-alive",
    "Origin": "https://www.bilibili.com",
    "Referer": "https://www.bilibili.com/video/"+ str(Avcode),
    "Cookie": cookie,
    "Pragma": "no-cache",
    "Cache-Control":"no-cache"
    }
    request=urllib.request.Request(url=url,headers=header)
    formdata=urllib.parse.urlencode(formdata).encode()
    response=urllib.request.urlopen(request,formdata)

    massage=json.loads(response.read().decode())

    return massage['code']

def Get_todayExp():
    api='https://api.bilibili.com/x/web-interface/coin/today/exp'
    header={
     "Host": "api.bilibili.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cookie":cookie,
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control":"max-age=0"
    }
    response = urllib.request.Request(url=api,headers=header)
    response = urllib.request.urlopen(response)
    response = json.loads(response.read().decode('utf-8'))
    return response

def Get_bangumi():
    bangumiApi="https://api.bilibili.com/x/web-interface/newlist?rid=33"
    response=urllib.request.urlopen(bangumiApi)
    response=json.loads(response.read().decode('utf-8'))
    data=response['data']
    avlist=[]
    for i in data['archives']:
        avlist.append(i['aid'])
    return avlist

if __name__ == '__main__':
    f=open("log.txt",'a+')
    localtime = time.asctime(time.localtime(time.time()))
    time=(50-Get_todayExp()['data'])/10
    Avlist=Get_bangumi()
    i=0
    while time!=0:
        if SeadAdd(Avlist[i], cookie, csrf) != 0:
            print('已经投过币了！')
            f.write(str(localtime)+' 已经投过币了！\n')
            i+=1
        else:
            print(str(Avlist[i])+'投币成功')
            f.write(str(localtime) + ' 投币成功'+str(Avlist[i])+"\n")
            i+=1
            time-=1
    print("你今天的投币经验机会已经使用完毕")
    f.write(str(localtime) + ":你今天的投币经验机会已经使用完毕\n")
