#-*-coding:utf-8-*- 
# author lyl
import settings
import redis
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
from multiprocessing import Process
from loguru import logger

redis_cli = redis.Redis(host=settings.REDIS.get("host"),
                        port=settings.REDIS.get("port"),
                        password=settings.REDIS.get("password"))

def register():
    if redis_cli.llen(settings.REDIS.get("url_list_key")) != 0:
        url = redis_cli.rpop(settings.REDIS.get("url_list_key"))
    else:
        url = ""
    return url


def start_server():
    server = SimpleXMLRPCServer(("0.0.0.0", 8000))
    print("Listening on port 8000...")
    server.register_function(register, "register")
    server.serve_forever()


def get_one_url():
    try:
        with xmlrpc.client.ServerProxy("http://{}:8000/".format(settings.DIST_CONF["master"])) as proxy:
            return str(proxy.register())
    except:
        return ""


class Rpc:

    def start_server(self):
        p = Process(target=start_server)
        p.start()
        logger.info("rpc服务已启动....")

    def get_url(self):
        return get_one_url()

