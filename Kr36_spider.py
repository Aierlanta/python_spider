# 爬取36kr新闻站的爬虫，复习正则使用
# 2022.5.28本爬虫可用

'''
url：https://36kr.com/
请求方法：GET

user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53

标签样式：<script>window.initialState=(.*?)</script>

实现步骤：
1、准备请求头和url
2、发送请求，获取相应
3、解析相应，获取数据，返回数据列表
4、保存数据
5、运行程序
'''

import re, requests, json

class Kr36(object):

    def __init__(self):
        self.url = 'https://36kr.com/'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
        }
        self.file = open('34-Kr36.json', 'w', encoding='utf-8')

    def get_url(self):
        response = requests.get(self.url, headers=self.headers)
        return response.content.decode()

    def parse_data(self, data):
        # re.findall会返回列表，所以用[]取其第一项
        result = re.findall('<script>window.initialState=(.*?)</script>', data)[0]
        # 将取得的列表转化为json
        dict_result = json.loads(result)
        # 提取新闻数据
        list_result = dict_result['homeData']['data']['homeFlow']['data']['itemList']
        # print(type(list_result))
        # 定义列表，保存新闻数据
        data_list = []
        for item in list_result:
            # itemType的值有10、60、5000，其中10为主
            # print(type(item))
            try:
                temp = {}
                if item['itemType'] == 10 or 60:
                    temp['title'] = item['templateMaterial']['widgetTitle']
                    temp['summary'] = item['templateMaterial']['summary']
                    temp['author'] = item['templateMaterial']['authorName']
                data_list.append(temp)

            except:
                pass
        return data_list

    def save_data(self, data_list):
        for data in data_list:
            json_str = json.dumps(data, ensure_ascii=False) + '\n'
            self.file.write(json_str)

    def __del__(self):
        self.file.close()

    def run(self):
        data = self.get_url()
        data_list = self.parse_data(data)
        self.save_data(data_list)

if __name__ == '__main__':
    kr = Kr36()
    kr.run()
