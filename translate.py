# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 09:22:23 2023

@author: Danny Huang

need to access Baidu Fanyi to apply a developer account.
http://api.fanyi.baidu.com/doc/21

"""
def translate_text(q):
    
    # coding=utf-8
    
    import http.client
    import hashlib
    import urllib
    import random
    import json
    
    appid = 'xxxxx'  # input your app ID here
    secretKey = 'xxxx'   # input your key here
    
    httpClient = None
    myurl = '/api/trans/vip/translate'
    
    fromLang = 'zh'   #原文语种
    toLang = 'en'   #译文语种
    salt = random.randint(32768, 65536)
    action = '1'
    
#    q= ''
    a=''
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign + '&action=' + action
    
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
    
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        
    #    print (result)
    #    print(result.get('trans_result'))
    #    'print(trans_result.get('dst'))
        trans_result_final = result.get('trans_result')
        
        a = trans_result_final[0].get('dst')
    #    print(a)
    
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()
    return a

#q= '建立CRG003项目基因组滴度（ddPCR法）检测方法与操作，确保检测过程符合规定，从而保证检测结果准确可靠。铺板操作如下'
#print(translate_text(q))
