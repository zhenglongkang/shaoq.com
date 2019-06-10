# -*- coding: utf-8 -*- 
__author__ = 'Phil'
__date__ = '2019/5/31 19:16'

import re

response = '''
eval(function(p,a,c,k,e,r){e=String;if('0'.replace(0,e)==0){while(c--)r[e(c)]=k[c];k=[function(e){return r[e]||e}];e=function(){return'[0]'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('0 dynamicurl="/wenshu";0 wzwsquestion="?&lt;Mut";0 wzwsfactor="8189";0 wzwsmethod="WZWS_METHOD";0 wzwsparams="WZWS_PARAMS";',[],1,'var'.split('|'),0,{}))
'''

regex = '(?P<param>\'0 dynamicurl.*";\')'

print(re.search(regex, response).groupdict()['param'])