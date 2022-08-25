# -*-coding:utf-8-*-
# author lyl
from kazoo.exceptions import NoNodeError
import settings
from loguru import logger
import time
from kazoo.client import KazooClient

import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


class EmailSender:

    def __init__(self):

        self.__passwd_code = ""

        # 发送地址
        self.__from_addr = ""
        # 收件人地址:
        self.__to_addrs = settings.ZOOKEEPER.get('email_receivers')
        # 输入SMTP服务器地址:
        self.smtp_server = 'smtp.163.com'

        self.server = smtplib.SMTP() # SMTP协议默认端口是25
        self.server.set_debuglevel(0)

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def set_to_addrs(self, addr):
        self.__to_addrs = addr if isinstance(addr, list) else [addr]
        return self

    def send(self, msg):
        msg = MIMEText(msg, 'plain', 'utf-8')

        msg["From"] = self._format_addr("爬虫系统监控系统 <%s>".format(self.__from_addr))
        msg["To"] = self._format_addr(",".join(["管理员 <%s>".format(addr) for addr in self.__to_addrs]))
        msg["Subject"] = Header('爬虫节点变化通知', 'utf-8').encode()

        self.server.connect(self.smtp_server, 25)
        self.server.login(self.__from_addr, self.__passwd_code)
        self.server.sendmail(self.__from_addr, self.__to_addrs, msg.as_string())
        self.server.quit()


class ZookeeperMonitor:

    def __init__(self):
        self.zk = KazooClient(hosts=settings.ZOOKEEPER.get("hosts"))
        self.zk.start()

        self.zk_master_node = settings.ZOOKEEPER.get('master_node')
        self.zk_sub_node = settings.ZOOKEEPER.get("sub_node")

        self.childs = self.zk.get_children(self.zk_master_node)

        # node -> value
        self.childs_map = {}

        logger.info("zookeeper启动监控...")
        logger.info(self.childs)

        # 邮件发送
        self.mail_sender = EmailSender()

    def add_prompt(self, childs=None):
        try:
            if childs and len(childs) > 0:
                node = childs.pop()
                ip = self.zk.get(self.zk_master_node + "/" + node)[0].decode()
                self.childs_map[node] = ip
                info = "新增一个节点，节点信息为：{}" .format(ip)
            else:
                info = "新增一个节点"
            logger.info(info)
            self.mail_sender.send(info)
        except Exception as e:
            logger.warning(e)

    def delete_prompt(self, childs=None):
        try:
            if childs and len(childs) > 0:
                node = childs.pop()
                ip = self.childs_map.get(node, node)
                info = "有爬虫节点挂掉了，请人工查看爬虫节点的情况，节点信息为：{}".format(ip)
            else:
                info = "删除一个节点"
            logger.info(info)
            self.mail_sender.send(info)
        except Exception as e:
            logger.warning(e)

    def call_back(self, event):
        childs = self.zk.get_children(self.zk_master_node)
        # 新增
        if set(childs) - set(self.childs):
            self.add_prompt(set(childs)-set(self.childs))
        # 删除
        elif set(self.childs) - set(childs):
            self.delete_prompt(set(self.childs) - set(childs))
        self.childs = childs
        self.start_monitor()

    def start_monitor(self):
        self.zk.get_children(self.zk_master_node, watch=self.call_back)


if __name__ == '__main__':
    ZookeeperMonitor().start_monitor()
    time.sleep(100000)