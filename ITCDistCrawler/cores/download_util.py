#-*-coding:utf-8-*- 
# author lyl
import requests
from loguru import logger
import time
from selenium import webdriver
import settings
from typing import Union
from .proxy_util import ProxyManager


class HtmlDownloader:

    proxy_manager = ProxyManager()  if settings.IpProxy.get('ENABLE') else None

    @classmethod
    def request(cls, url: str,
                params=None,
                proxies=None,
                method="get",
                request_num=0,
                return_json=False,
                **kwargs) -> Union[requests.Response, None]:
        assert method in ['get', 'post'], f"method must be one of [post, get]"
        try:
            if proxies is None and cls.proxy_manager is not None:
                proxies = cls.proxy_manager.get_proxy()
            if method == "get":
                res = requests.get(url, params=params, headers=settings.HEADERS, proxies=proxies, **kwargs)
            else:
                res = requests.post(url, json=params, headers=settings.HEADERS, proxies=proxies, **kwargs)
        except Exception as e:
            logger.error(e)
            if request_num < settings.MAX_REQUEST_NUM:
                time.sleep(0.5)
                return cls.request(url, params, proxies, method, request_num+1)
            else:
                return None
        return res if res.status_code == 200 else None


class SeleniumDownloader:

    @classmethod
    def request(cls, url):
        browser = webdriver.Chrome('D:\\chromedriver.exe')
        browser.get(url)
        time.sleep(2)
        page = browser.page_source
        browser.close()
        return page
