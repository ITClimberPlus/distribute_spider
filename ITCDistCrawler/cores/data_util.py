#-*-coding:utf-8-*- 
# author lyl
from utils.hdfs_util import HdfsHandler
import settings
from cores.parser_util import DangdangItem
from loguru import logger
from typing import Union, List

class DataPipline:

    def __init__(self):
        self.hdfsClient = HdfsHandler(settings.HDFS.get('url'),
                                      proxy=settings.HDFS.get('proxy'))

        self.data_path = settings.HDFS.get("data_path")
        self.filename = settings.HDFS.get('filename').format(
            settings.NODE_NAME
        )

    def save(self, item: Union[DangdangItem, List[DangdangItem]]) -> None:
        if isinstance(item, DangdangItem):
            item = [item]
        for it in item:
            data = it.to_json()
            if not self.hdfsClient.exists('/spider', self.filename):
                self.hdfsClient.touch('/spider/', self.filename)
            self.hdfsClient.append('/spider/{}'.format(self.filename), data + "\n")
            print(data)
