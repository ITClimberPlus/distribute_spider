#-*-coding:utf-8-*- 
# author lyl
import time
import socket
import settings
import requests
from loguru import logger
from multiprocessing import Process, Queue, Lock
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import Thread, Lock


def get_host_ip():
    ip = ""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as e:
        logger.error(e)
    return ip

def get_out_ip():
    ip = ""
    try:
        res = requests.get('http://ifconfig.me/ip', timeout=10)
        if res.status_code != 200:
            raise ValueError('status code is {}'.format(res.status_code))
        ip = res.text.strip()
    except Exception as e:
        logger.error(e)
    return ip



class UrlScheduler:

    def __init__(self, downloader, parser, dataPipline, rpc):
        self.downloader = downloader
        self.parser = parser
        self.dataPipline = dataPipline
        self.rpc = rpc

        # 开启多线程
        self.q = Queue()
        self.mutex = Lock() # 互斥锁

        # 如果是master，启动server
        if settings.DIST_CONF["master"] == get_out_ip():
            self.rpc.start_server()


    def download_exec(self):
        while True:
            url = self.rpc.get_url()
            logger.info(url)
            if not isinstance(url, str) or url.strip() == "":
                continue
            html = self.downloader.request(url).text
            self.q.put(html)
            time.sleep(0.5)

    def parse_save_exec(self):
        while True:
            html = self.q.get()
            item = self.parser.parse(html)
            if len(item) != 0:
                self.dataPipline.save(item)


    def loop_twothread(self):
        thread_pool = ThreadPoolExecutor(max_workers=5)
        thread_pool.submit(self.download_exec)
        thread_pool.submit(self.parse_save_exec)
        thread_pool.shutdown(wait=True)

    def one_loop(self):
        url = self.rpc.get_url()
        logger.info(url)
        if not isinstance(url, str) or url.strip() == "":
            return
        html = self.downloader.request(url).text
        item = self.parser.parse(html)
        if len(item) != 0:
            self.dataPipline.save(item)

    def run(self):
        self.loop_twothread()
        # while True:
        #     self.one_loop()
        #     time.sleep(0.5)








