# -*- coding: utf-8 -*- 
__author__ = 'Phil'
__date__ = '2019/6/10 0:41'

import re

import execjs
import requests

# 构建请求头
headers = {
    'Host': 'shaoq.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://shaoq.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

target_url = 'http://shaoq.com/wenshu'
response = requests.get(target_url, headers=headers)

# 获取参数
dynamicurl = re.search('dynamicurl="(.*?)"', response.text).group(1)
wzwsquestion = re.search('wzwsquestion="(.*?)"', response.text).group(1)
wzwsfactor = re.search('wzwsfactor="(.*?)"', response.text).group(1)
wzwsmethod = re.search('wzwsmethod="(.*?)"', response.text).group(1)
wzwsparams = re.search('wzwsparams="(.*?)"', response.text).group(1)

# 获取cookies
cookies = response.cookies.get_dict()

with open('wenshu.js', 'r', encoding='utf-8')      as f:
    para_part = '''var dynamicurl="{}";var wzwsquestion="{}";var wzwsfactor="{}";var wzwsmethod="{}";var wzwsparams="{}";
    '''.format(dynamicurl, wzwsquestion, wzwsfactor, wzwsmethod, wzwsparams)

    js_code = para_part + f.read()
    context = execjs.compile(js_code)
    challenge = context.call("get")

url = target_url+'?wzwschallenge='+challenge

headers['Referer'] = 'http://shaoq.com/wenshu'
headers['Cookie'] ='cookie=%s' % cookies['cookie']

response = requests.get(url, headers=headers)

print(response.text)


