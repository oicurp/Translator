# coding=utf-8

def translate_text(q):

    import http.client
    import hashlib
    import urllib
    import random
    import json
    
    appid = '20230818001784866'  # 填写你的appid
    secretKey = 'nnzqQih7ge1am5oi8QKc'  # 填写你的密钥
    
    httpClient = None
    myurl = '/api/trans/vip/fieldtranslate'
    a = ''
    fromLang = 'zh'   #原文语种
    toLang = 'en'   #译文语种
    salt = random.randint(32768, 65536)
    #q= '理论塔板数'
    domain = 'senimed'
    sign = appid + q + str(salt) + domain + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&domain=' + domain + '&sign=' + sign
    
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
    
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        
        trans_result_final = result.get('trans_result')
        a = trans_result_final[0].get('dst')
    
        #print (result)
    
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()
    
    return a