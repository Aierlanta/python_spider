import re
import requests

'''
1、获取数据
2、将数据配对
3、保存数据
'''


class NovelSpider(object):

    def __init__(self):
        # n = [i + 1 for i in range(1,10)]
        n = 2
        self.url1 = 'http://trxs.cc/tongren/index.html/'
        self.url2 = f'http://trxs.cc/tongren/index_{n}.html'

    def get_data(self):
        response1 = requests.get(self.url2)
        return response1.content

    @staticmethod
    def matching_data(data):
        url_number = re.findall('a href="/tongren/' + r'(\d+?)' + '.html', data)
        new_url = ['http://trxs.cc/tongren/' + url_number[i] + '.html' for i in range(len(url_number))]
        print(url_number)
        print(new_url)

    def save_data(self):
        pass

    def run(self):
        data = str(self.get_data())
        find_all(data)


def find_all(data):
    url_number = re.findall('a href="/tongren/' + r'(\d+?)' + '.html', data)
    new_url = ['http://trxs.cc/tongren/' + url_number[i] + '.html' for i in range(len(url_number))]
    print(url_number)
    print(new_url)


if __name__ == '__main__':
    ns = NovelSpider()
    ns.run()