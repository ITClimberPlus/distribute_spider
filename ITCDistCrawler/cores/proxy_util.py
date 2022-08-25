#-*-coding:utf-8-*- 
# author lyl
import settings
from loguru import logger
from utils.IpProxyPool import KuaidailiIpProxyPool, ZhimaIpProxyPool


proxy_map = {
    'KuaidailiIpProxyPool': KuaidailiIpProxyPool,
    'ZhimaIpProxyPool': ZhimaIpProxyPool
}


class ProxyManager:

    def __init__(self):
        proxy_src = settings.IpProxy.get('PROXY_IP_SOURCE')
        assert proxy_src in ["ZhimaIpProxyPool", "ZhimaIpProxyPool"]
        self.proxy_generator = proxy_map[proxy_src]()

    def get_proxy(self):
        try:
            proxy = self.proxy_generator.getproxies()
        except Exception as e:
            logger.warning(e)
            proxy = None
        return proxy