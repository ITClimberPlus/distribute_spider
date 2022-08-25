#-*-coding:utf-8-*- 
# author lyl
# !coding:utf-8
import sys
import os
from hdfs.client import Client
# 关于python操作hdfs的API可以查看官网:
# https://hdfscli.readthedocs.io/en/latest/api.html
# http://120.53.228.150:9870



class HdfsHandler:

    def __init__(self, url, root=None, proxy=None, timeout=None, session=None):
        self.client = Client(url, root=root, proxy=proxy, timeout=timeout, session=session)

    def mkdirs(self, path, permission=None):
        self.client.makedirs(path, permission=permission)

    # 创建文件
    def touch(self, hdfs_path, filename):
        self.client.write(hdfs_path+filename, "")

    # 删除文件
    def delete_file(self, filename):
        self.client.delete(filename)

    # 将本地文件上传到hdfs
    def put(self, local_path, hdfs_path):
        self.client.upload(hdfs_path, local_path, cleanup=True)

    # 将hdfs文件下载到本地
    def get(self, hdfs_path, local_path, overwrite=False):
        self.client.download(hdfs_path, local_path, overwrite=overwrite)

    #向hdfs追加数据
    def append(self, hdfs_path, data):
        self.client.write(hdfs_path, data,
                          overwrite=False,
                          append=True,
                          encoding="utf-8")

    # 覆盖数据写到hdfs文件
    def write(self, hdfs_path, data):
        self.client.write(hdfs_path, data,
                          overwrite=True,
                          append=False,
                          encoding="utf-8")

    # 移动或者修改文件
    def move(self, hdfs_src_path, hdfs_dst_path):
        self.client.rename(hdfs_src_path, hdfs_dst_path)

    # 返回目录下的文件
    def list(self, hdfs_path):
        return self.client.list(hdfs_path, status=False)

    # 判断某个文件在某个路径下是否存在
    def exists(self, hdfs_path, filename):
        files = self.list(hdfs_path)
        return filename in files

    # 读取hdfs文件内容,将每行存入数组返回
    def read_hdfs_file(self, filename):
        lines = []
        with self.client.read(filename, encoding='utf-8', delimiter='\n') as reader:
            for line in reader:
                lines.append(line.strip())
        return lines





