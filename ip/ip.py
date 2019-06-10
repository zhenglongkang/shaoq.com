# -*- coding: utf-8 -*- 
__author__ = 'Phil'
__date__ = '2019/5/31 15:20'

'''
css反爬-隐藏标签
'''

import re

import requests
from bs4 import BeautifulSoup


target_url = 'http://shaoq.com/ip'

response = requests.get(target_url)
response = response.text

soup = BeautifulSoup(response, "lxml")
style = soup.find('style')
regex =  r'(?P<style>.*)\{display\:none\}'

style_list = re.findall(regex, str(style))

# 将display的标签去掉
regex = r'<[a-zA-Z]*? style="display:none">.*?</[a-zA-Z]*?>'
# a = re.findall(regex, response)
response = re.sub(regex, '', response)
for style in style_list:
    regex = r'<[a-zA-Z]*? class="{}">.*?</[a-zA-Z]*?>'.format(style[1:])
    response = re.sub(regex, '', response)
response = re.sub(r'\s', '', response)

ip_list = list()
for element in response.split('<br>'):
    _element = BeautifulSoup(element, "lxml")
    ip = ''
    for s in list(_element.strings):
        regex = '^[0-9\.]+$'
        if re.match(regex, s) is not None:
            ip += s
    if ip:
        ip_list.append(ip)

print(ip_list)





