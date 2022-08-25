#-*-coding:utf-8-*- 
# author lyl
import lxml.etree as etree
from dataclasses import dataclass
from urllib.parse import urljoin
from typing import List
import json

@dataclass
class DangdangItem:
    '''
    当当网数据类
    '''
    title: str # 商品标题
    now_price: str = "" # 商品现价
    pre_price: str = "" # 商品原价
    discount: str = "" # 商品折扣
    author: str = "" # 作者
    pub_date: str = "" # 出版日期
    img_url: str = "" # 商品图片链接
    publisher: str = "" # 出版社
    url: str = "" # 商品链接
    comment_count: str = "" # 评论数

    def __repr__(self):
        return "{" + ", ".join(["{}: {}".format(k, v) for k, v in self.__dict__.items() if v]) + "}"

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

class DangdangParser:

    base_url = "http://product.dangdang.com/"
    rules = {
        "list": '//div[@id="search_nature_rg"]/ul/li',
        "url": './/p[@class="name"]/a/@href',
        "title": './/p[@name="title"]/a//text()',
        "now_price": './/p[@class="price"]/span[@class="search_now_price"]/text()',
        "pre_price": './/p[@class="price"]/span[@class="search_pre_price"]/text()',
        "author": './/p[@class="search_book_author"]/span[1]//text()',
        "discount": './/p[@class="price"]/span[@class="search_discount"]/text()',
        "date": './/p[@class="search_book_author"]/span[2]//text()',
        "publisher": './/p[@class="search_book_author"]/span[3]/a/text()',
        'img_url': './a[@class="pic"]/img/@data-original',
        "comment_count": './/p[@class="search_star_line"]/a[@dd_name="单品评论"]/text()'
    }
    dalone = lambda x: x[0] if x else ""

    @classmethod
    def parseList(cls, html) -> List[DangdangItem]:

        details = []
        item_list = etree.HTML(html).xpath(cls.rules['list'])
        for item in item_list:
            # 获取标题
            title = "".join([i for i in item.xpath(cls.rules["title"]) if i.strip()])
            # 获取原价
            pre_price = "".join([i for i in cls.dalone(item.xpath(cls.rules["pre_price"])) if i != '\n'])
            # 获取现价
            now_price = "".join([i for i in cls.dalone(item.xpath(cls.rules["now_price"])) if i != '\n'])
            # 获取折扣
            discount = "".join([i for i in item.xpath(cls.rules["discount"]) if i]).strip().strip('(').strip(')')
            # 获取作者
            author = "".join([i for i in item.xpath(cls.rules["author"]) if i.strip()])
            # 获取日期
            date = cls.dalone(item.xpath(cls.rules["date"])).strip().strip('/')
            # 获取出版社
            publisher = cls.dalone(item.xpath(cls.rules["publisher"])).strip()
            # 获取url
            url = urljoin(cls.base_url, cls.dalone(item.xpath(cls.rules['url'])))
            # 获取图片url
            img_url = cls.dalone(item.xpath(cls.rules['img_url'])).strip()
            if img_url == "":
                img_url = cls.dalone(item.xpath(cls.rules["img_url"].replace("data-original", "src"))).strip()
            img_url = urljoin("http://", img_url)
            # 获取评论数
            comment_count =  cls.dalone(item.xpath(cls.rules["comment_count"])).strip().strip("条评论")

            if title.strip() == "" or now_price.strip() == "":
                continue

            item = DangdangItem(
                title=title,
                now_price=now_price,
                pre_price=pre_price,
                author=author,
                url=url,
                pub_date=date,
                discount=discount,
                publisher=publisher,
                img_url=img_url,
                comment_count=comment_count
            )
            details.append(item)
        return details

    @classmethod
    def parse(cls, html: str) -> List[DangdangItem]:
        return cls.parseList(html)
