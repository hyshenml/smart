# -*- coding: utf-8 -*-

__author__ = 'sml'
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '10758323'
API_KEY = 'q0zI5K7I51EDKNlr0RR0dD1L'
SECRET_KEY = '0HQy36VkQsen7Pmhqg3RRikG1nZyDqmA'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
""" 带参数调用通用文字识别, 图片参数为本地图片 """
res=client.basicGeneral(image, options)
for word in res['words_result']:
    print word['words']