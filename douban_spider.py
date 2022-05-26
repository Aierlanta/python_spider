# 豆瓣高分电影爬虫（前50条），2022.5.26可用

import requests, json

'''
通过浏览器测试，豆瓣高分电url地址：
https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0

实现步骤：
1、准备初始的url和响应头
2、发送请求，获取响应
3、解析响应，提取数据
4、保存数据
5、程序运行入口
'''

class DouBan(object):
    def __init__(self):
        # 准备初始的url和响应头
        self.url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
        }
        # 打开文件
        self.file = open('2.28-douban.json', 'w', encoding='utf-8')

    def get_data(self):
        # 发送请求，获取响应
        response = requests.get(self.url,headers=self.headers)
        return response.content.decode()

    def parse_data(self, data):
        # 解析响应，提取数据
        # 解析json，将其转化为字典类型
        result = json.loads(data)
        result_list = result['subjects']
        # 定义列表，提取json数据
        data_list = []
        # 遍历result_list获取名称、评分、url等内容
        for item in result_list:
            temp = {}
            temp['title'] = item['title']
            temp['rate'] = item['rate']
            temp['url'] = item['url']
            data_list.append(temp)
        # data_list中的列表形式：[{1},{2},{3}]
        return data_list

    def save_data(self, data_list):
        # 保存数据
        # 首先，要遍历data_list，将其转换成json，并加入逗号和换行符
        for data in data_list:
            show_list = data['title'] + ':' + data['rate'] + "分; 链接：" + data['url']
            json_data = json.dumps(show_list, ensure_ascii=False) + ',\n'
            self.file.write(json_data)

    def __del__(self):
        # 桥构方法，最后执行
        # 关闭文档
        self.file.close()

    def run(self):
        data = self.get_data()
        data_list = self.parse_data(data)
        self.save_data(data_list)


if __name__ == '__main__':
    douban = DouBan()
    douban.run()
