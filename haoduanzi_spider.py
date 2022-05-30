# 测试时间2022.5.30，本爬虫可用
# 因为后面的页面都炸了，所以本爬虫直接变为弱智爬虫
# 用来练习xpath
'''
有个很有意思的事，这网站除了第一页以外的段子都炸了
然后我发现这玩意也连没有useragent
http://www.haoduanzi.com/wen/
GET
xpath
//*[@id="LR"]/div/div[2]/ul/li[not(@class='ad')]
标题：
//*[@id="LR"]/div/div[2]/ul/li/div[1]/h2
内容：
//*[@id="LR"]/div/div[2]/ul/li/div[2]/a

如果说，这其他的页面没有问题的话，可以用format（）将数据传进去
'''

import requests, json
from lxml import etree

class HaoDuanZi(object):

    def __init__(self):
        # 初始url
        self.url = 'http://www.haoduanzi.com/wen/'
        self.file = open('41-haoduanzi.json', 'w', encoding='utf-8')

    def get_url(self):
        # 获取数据
        response = requests.get(self.url)
        # print(response.content.decode())
        return response.content.decode()

    def parse_data(self, data):
        # 解析数据，提取段子的标题和内容
        heml = etree.HTML(data)
        # 获取Element对象
        node_list = heml.xpath("//*[@id='LR']/div/div[2]/ul/li[not(@class='ad')]")
        # print(node_list)
        # 遍历节点列表，提取数据
        data_list = []
        for node in node_list:
            temp = {}
            temp['title'] = node.xpath("./div[1]/h2/text()")
            temp['content'] = node.xpath("./div[2]/a/text() | ./div[2]/a/p/text()")## “|”是xpath里的语法，所以要放在一个字符串里使用
            # print(temp)
            data_list.append(temp)
        # print(data_list)
        return data_list

    def save_data(self, data_list):
        # 遍历data_list，将其转为json格式
        for data in data_list:
            json_str = json.dumps(data, ensure_ascii=False) + '\n'
            self.file.write(json_str)

    def __del__(self):
        # 关闭文件
        self.file.close()

    def run(self):
        # 运行
        data = self.get_url()
        data_list = self.parse_data(data)
        self.save_data(data_list)

if __name__ == '__main__':
    dz = HaoDuanZi()
    dz.run()
