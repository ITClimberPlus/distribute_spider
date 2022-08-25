#-*-coding:utf-8-*- 
# author lyl
from kazoo.exceptions import NoNodeError
import settings
import time
from kazoo.client import KazooClient
from loguru import logger
from cores.url_scheduler import get_out_ip




class ZookeeperMonitor:

    def __init__(self):
        self.zk = KazooClient(hosts=settings.ZOOKEEPER.get("hosts"))
        self.zk.start()

        self.zk_master_node = settings.ZOOKEEPER.get('master_node')
        self.zk_sub_node = settings.ZOOKEEPER.get("sub_node")

        try:
            self.zk.get(self.zk_master_node)
            logger.info("Zookeeper has node {}".format(self.zk_master_node))
        except NoNodeError as e:
            logger.info("Zookeeper create node {}".format(self.zk_master_node))
            self.zk.create(self.zk_master_node, makepath=True, value="master_node".encode())

    def register(self):

        self.zk.create(self.zk_master_node + "/" + self.zk_sub_node,
                       value=get_out_ip().encode(),
                       ephemeral=True,
                       sequence=True)



if __name__ == '__main__':

    cli = ZookeeperMonitor()
    cli.register()
    time.sleep(10)

