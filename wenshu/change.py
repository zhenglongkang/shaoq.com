# -*- coding: utf-8 -*- 
__author__ = 'Phil'
__date__ = '2019/6/10 11:56'

import re

import execjs

"""
处理裁判文书网的简化后的js代码
调用_0x213d函数的地方替换为函数的结果
"""

with open('wenshu_source.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    # 正则表达式匹配函数参数
    regex = r"_0x213d\('(?P<param_1>\w+?)', '(?P<param_2>\w+?)'\)"
    args_list = re.findall(regex, js_code)
    with open('_0x213d.js', 'r', encoding='utf-8') as j:
        # 传入js代码
        context = execjs.compile(j.read())
        for args in args_list:
            formula = "0x213d('{}', '{}')".format(*args)
            # 调用函数，获得结果
            result = context.call("_0x213d", *args)
            # 对js代码进行替换
            js_code.replace(formula, "'{}'".format(result))
        print(js_code)
