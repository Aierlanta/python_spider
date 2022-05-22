# 时间:2022.5.21 本爬虫可用

import requests

class TieBa(object):

    def __init__(self,name,pn):
        #准备起始url地址和请求头信息
        self.name = name
        self.pn = pn
        self.url = f'https://tieba.baidu.com/f?kw={self.name}&ie=utf-8&pn='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
        }
        #生成不同页数的url信息
        self.url_list = [self.url + str(x * 50) for x in range(self.pn)]

    def gat_data(self):
        #发送请求、获取响应
        response = requests.get(self.url, headers=self.headers)
        return response.content.decode()

    def save_data(self, data, index):
        #保存数据
        file_name = name + '吧第' + str(index + 1) + '页' + '.html'
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(data)

    def run(self):
        #入口函数,在类的内部，实现各个函数之间的协调调用
        #遍历url列表，把每页url传给请求的函数
        for url in self.url_list:
            data = self.gat_data()
            index = self.url_list.index(url)
            self.save_data(data, index)

if __name__ == '__main__':
    # #获取程序外输入
    # import sys
    # name = sys.argv[1]
    # pn = int(sys.argv[2])
    name = input('请输入吧名:')
    pn = int(input('请输入需要爬取的页码数（1~n）:'))
    tieba = TieBa(name,pn)
    tieba.run()
