#-*-coding:utf-8-*- 
# author lyl
from cores.download_util import HtmlDownloader, SeleniumDownloader
from cores.parser_util import DangdangParser
from cores.data_util import DataPipline
from cores.rpc_util import Rpc
from cores.url_scheduler import UrlScheduler
from cores.monitor_util import ZookeeperMonitor
from loguru import logger


class JobManager:

    def __init__(self, scheduler, zk_monitor=None):
        self.scheduler = scheduler
        self.zk_monitor = zk_monitor

    def start(self):
        if self.zk_monitor is not None:
            # zookeeper注册
            logger.info("zookeeper register...")
            self.zk_monitor.register()
        self.scheduler.run()


if __name__ == '__main__':

    urlScheduler = UrlScheduler(
        HtmlDownloader(),
        DangdangParser(),
        DataPipline(),
        Rpc()
    )
    JobManager(urlScheduler, ZookeeperMonitor()).start()





