import urllib.request
import urllib.parse
import json
import time

# 在这里填你的csrt效验码
csrf='b0734b1f38e2f3ab276e57f2d18b14fd'
# 在这里填上你的b站cookie
cookie=" _uuid=898B91F2-E50A-6843-3EE7-6BAA9AFC14BE97078infoc; buvid3=195C653B-23E7-461E-A2C1-83EA28D91417190959infoc; LIVE_BUVID=AUTO5615751130990552; CURRENT_FNVAL=16; stardustvideo=1; laboratory=1-1; rpdid=|(u)Yk)|))lY0J'ul~luYl)uY; CURRENT_QUALITY=112; bp_t_offset_11611487=379760321125681316; im_notify_type_11611487=0; INTVER=-1; sid=aceyho8d; DedeUserID=11611487; DedeUserID__ckMd5=862e7439cf3c2534; SESSDATA=bbb6608b%2C1599789662%2C6f221*31; bili_jct=b0734b1f38e2f3ab276e57f2d18b14fd; PVID=7; bsource=seo_baidu"

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
