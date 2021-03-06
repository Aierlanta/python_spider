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

import requests, re, os
from lxml import etree

class TieBa(object):

    def __init__(self):
        # 如果想要爬其他的吧，可以在初始化函数中加入吧名参数，然后作为变量引入要爬的吧，和作为要保存的文件夹名
        self.url = 'http://c.tieba.baidu.com/f?kw=%E4%BC%8A%E8%95%BE%E5%A8%9C'
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
        }

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        # with open('tieba.html', 'w', encoding='utf-8') as f:
        #     f.write(response.content.decode())
        return response.content

    def parse_data(self, results):
        # 解析获取到的网页数据，提取，返回帖子列表，和下一页链接
        html = etree.HTML(results)
        node_list = html.xpath('//*[@id="thread_list"]/li')
        # print(node_list)
        tieba_list = []
        # 遍历节点列表，提取数据
        for node in node_list:
            temp = {}
            if not node.xpath('./div/div[2]/div[1]/div[1]/a/@href'):
                pass
            else:
                # print(node.xpath('./div/div[2]/div[1]/div[1]/a/@href'))
                temp['url'] = 'http://c.tieba.baidu.com' + node.xpath('./div/div[2]/div[1]/div[1]/a/@href')[0]
            tieba_list.append(temp)
            # print(tieba_list)

        next_url = 'http:' + html.xpath('//*[@id="frs_list_pager"]/a[contains(text(), "下一页")]/@href')[0]
        # print(next_url)

        return tieba_list, next_url

    def parse_detail(self, detail_data):
        # 解析详情内容，返回图片列表
        html = etree.HTML(detail_data)
        img_list = html.xpath('//*[@id]/img/@src')
        # print(img_list)
        for img in img_list:
            # print(img)
            image_list = re.findall('http://tiebapic.baidu.com/.+', img,)
            # print(real)
            if not image_list:
                pass
            else:
                return image_list
                # print(imge_list)

    def save_img(self, image_list):
        try:
            # 创建文件夹
            if not os.path.exists('elaina_img'):
                os.mkdir('elaina_img')
            for img_url in image_list:
                image_bytes = self.get_data(img_url)
                image_name1 = img_url.split('?')[0]
                image_name2 = 'elaina_img' + os.sep +  image_name1.split('/')[-1]
                # print(image_name2)
                with open(image_name2, 'wb') as f:
                    f.write(image_bytes)
        except:
            pass

    def run(self):
        url = self.url
        while True:
            results = self.get_data(url)
            tieba_list, next_url = self.parse_data(results)
            # 遍历帖子，获取图片链接，然后进入下一页
            for tieba in tieba_list:
                # print(tieba)
                if tieba == {}:
                    pass
                else:
                    detail_data = self.get_data(tieba['url'])
                    image_list = self.parse_detail(detail_data)
                    self.save_img(image_list)
                    # print(detail_data)
            if not next_url:
                break
            else:
                url = next_url

if __name__ == '__main__':
    tieba = TieBa()
    tieba.run()
