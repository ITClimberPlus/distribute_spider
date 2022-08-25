#-*-coding:utf-8-*- 
# author lyl
import redis
import settings

redis_cli = redis.Redis(host=settings.REDIS.get("host"),
                        port=settings.REDIS.get("port"),
                        password=settings.REDIS.get("password"))

key = settings.REDIS.get("url_list_key")

url = "http://search.dangdang.com/?key={keyword}&act=input&page_index={page}"

keywords = ["python", "c++", "nlp", "cv", "大数据"]

for keyword in keywords:
    for page in range(1, 101):
        redis_cli.rpush(url.format(keyword=keyword, page=page))