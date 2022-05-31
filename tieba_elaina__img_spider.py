'''
需求：
1、完成某个百度贴吧的某个帖子
2、使用xpath进行定位
3、完成翻页功能
4、下载详情页都图片
---
第一次get请求，伊雷娜吧的url：
http://c.tieba.baidu.com/f?kw=%E4%BC%8A%E8%95%BE%E5%A8%9C
进入每个帖子的url：
‘http://c.tieba.baidu.com' + //*[@id="thread_list"]/li/div/div[2]/div[1]/div[1]/a/@href

第二次url请求：全部图片的url：
//*[@id]/img/@src
# 但注意，这里面包含有表情包
正则：
http://tiebapic.baidu.com/.+

下一页链接：
'http:' + //*[@id="frs_list_pager"]/a[contains(text(), '下一页')]/@href
在每页帖子图片爬完以后，翻页
'''

import requests, re
from lxml import etree

class TieBa(object):

    def __init__(self):
        pass

    def get_data(self):
        pass

    def parse_data(self):
        pass

    def parse_detal(self):
        pass

    def save_img(self):
        pass

    def run(self):
        pass

if __name__ == '__main__':
    tieba = TieBa()
    tieba.run()
