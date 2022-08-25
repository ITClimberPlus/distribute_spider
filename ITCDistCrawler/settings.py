#-*-coding:utf-8-*- 
# author lyl

# ; 失败重试次数
MAX_REQUEST_NUM = 3

# 本节点名称
NODE_NAME = 'node_1'


# ; 爬虫headers设置
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",    "cookie": 'agent_id=1ff83a03-a2fc-4769-9174-ba640c7c39d5; session_id=1209d5a1-9d8d-48c5-9fdd-c11e60e7a031; session_key=d6c691f2e746712990a5fdf5ac06398b968e6634; gatehouse_id=1a73a2be-e69f-4c5e-8612-60c49c552bfe; geo_info={"countryCode":"FR","country":"FR","field_d":"c-dedie.net","field_n":"cp","trackingRegion":"Europe","cacheExpiredTime":1647589765536,"region":"Europe","fieldN":"cp","fieldD":"c-dedie.net"}|1647589765536; _sp_v1_uid=1:525:2a225c84-f9a2-44e6-9588-396517f0fa95; _sp_v1_csv=null; _sp_v1_lt=1:; ccpaUUID=c32a6f33-1231-4bb9-815d-84e0fa86c884; dnsDisplayed=true; ccpaApplies=true; signedLspa=false; _reg-csrf=s:-mp8sUbR4akPmZi-zJf_thtL.r6EGVi4HDmZ7Wutx14GqtFu6rxP5IFxoXefbbywVWP4; _user-status=anonymous; pxcts=cb02568e-a10f-11ec-9b81-574c4b4a6d76; _pxvid=cb024bc3-a10f-11ec-9b81-574c4b4a6d76; _sp_krux=true; consentUUID=52c3a722-4780-41bd-903e-a5d676fc2927_5; euconsent-v2=CPVrfb_PVrfb_AGABCENCGCgAP_AAGPAAAqIH9oB9CpGCTFDKGh4AIsAEAQXwBAEAOAAAAABAAAAAAgQAIwCAEASAACAAAACAAAAIAIAAAAAEAAAAEAAQAAAAAFAAAAEAAAAAAAAAAAAAAAAAAAAAIEAAAAAAUAAABAAgEAAABIAQAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgYtARAAcACEAHIAPwAvgCOAIHAQcBCACIgEWALqAYEA14B1AFlALzAYsAUMgCABMAEcARwBeYSAqAAsACoAGQAOAAgABkADSAIgAigBMACeAH4AQgAjgBSgDKAHeAPYAjgBKQDiAMkFQBQAmACOAI4ApsBeY6AyAAsACoAGQAOAAgABcADIAGkARABFACYAE8AMQAfgBHACYAFGAKUAZQA7wB7AEcAJSAcQA6gDJBwAEAC5CAUAAsADIALgAmABiAEcAO8AjgBKQDqEoBgACwAMgAcACIAEwAMQAjgBRgClAHeARwA6hIACABcpATAAWABUADIAHAAQAAyABpAEQARQAmABPADEAH4AUYApQBlADvAI4ASkBkhQACABc.YAAAAAAAAAAA; _sp_v1_opt=1:login|true:last_id|11:; bbgconsentstring=req1fun1pad1; bdfpc=004.9520457485.1646984986040; _gcl_au=1.1.588929971.1646984986; consentUUID=52c3a722-4780-41bd-903e-a5d676fc2927_5; __gads=ID=8d005339cf4cedad:T=1646984987:S=ALNI_Mbu438ghoat8O0aQzJjdiJszbnDjw; _ga=GA1.2.1907031709.1646984987; _gid=GA1.2.2006757276.1646984988; _cc_id=6fb28b279c88af9b4e952eb6b8fd351e; _rdt_uuid=1646984999426.9666e7f1-49fb-40e1-9620-73b00a53d909; _li_dcdm_c=.bloomberg.com; _lc2_fpi=b1166d620485--01fxvz9rw8wfak2rv2jbxp7qgf; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbLKK83J0YlRSkVil4AlqmtrlXRIVRZNJCMPxDCojcVlJD0ksDkbnzdHDaLEoFgAzRDu9nMCAAA=; _sp_v1_consent=1!1:1:1:0:0:0; optimizelyEndUserId=oeu1646985018026r0.4445593921187527; _scid=766fd56b-8060-4051-a307-d96ad0fff9b6; _parsely_session={"sid":1,"surl":"https://www.bloomberg.com/europe","sref":"","sts":1646985024866,"slts":0}; _parsely_visitor={"id":"pid=256c4892666dfe1a2c622bbdee11591e","session_count":1,"last_session_ts":1646985024866}; _fbp=fb.1.1646985026036.980128035; __sppvid=40f9064b-cce9-4ce2-b6da-9a2f1339f6ba; _tb_sess_r=https://www.bloomberg.com/europe; _sp_v1_data=2:439307:1646984967:0:6:0:6:0:0:_:-1; panoramaId_expiry=1647072056716; _tb_t_ppg=https://www.bloomberg.com/news/articles/2022-03-10/russia-ukraine-war-key-developments-in-the-ongoing-conflict; _reg-csrf-token=Gx3kxqkO-BuHpSGtV0J6aDa9Na2t_q-qtpq0; _last-refresh=2022-3-11 8:3; _uetsid=d5f9e920a10f11eca10cc191b2fee319; _uetvid=d5fbbe20a10f11ecbe29539c9c026427; trc_cookie_storage=taboola%20global%3Auser-id=fabf096f-05b1-4bad-ac0f-b9c2a10e30cc-tuct81ce3f4; _px3=dd358baf062534a5f8bacf63b9c0e1a47d0f699b68a652930564c9797e063847:7+4uskvI9AC7Py5fhRXTrFAGQg3PNTg7wC2eWU7D0IImDwfGJL86BhZj9w70AY1QDQtCGnyV9k4AJL5CHY24+Q==:1000:G5l3aWfvQitH7mElBidbefzLuRCLY5Akgdte19KffWh60GkKhnD8Oy+UVtCSP2wK6JBG/QJ5tiIr7Q3sGsmtT/xFoCb5BbG/apIG2aGcCG2g9tkMiBZISCar9L01+jrBP9zTfOVtTwC1RZ50YlaLEkEoYpwpyQsiQSUA7qIKlXvVlRI+mgaAm8CAsI4LsInaBV8e5sJgeR/6nMosUYqT6A==; _px2=eyJ1IjoiZjMyZWJhNzAtYTEwZi0xMWVjLWE5YzgtNDkyNjRiYTY1ODM1IiwidiI6ImNiMDI0YmMzLWExMGYtMTFlYy05YjgxLTU3NGM0YjRhNmQ3NiIsInQiOjE2NDY5ODY3NzU3ODAsImgiOiI3NGQyODQ2MDFlN2YxNjRiZDA0ZGIwNDM1NGQyMmNjMTQ2YjZkZWM2NjhmNGFhMTRiOTg5OWUwMjhhMTU2MTZiIn0=; _pxde=0dd202c12c0efc87be51e59b825c2fa6dd8af4a6a2f679505b7b9c8c0a91cb62:eyJ0aW1lc3RhbXAiOjE2NDY5ODY0NzU3ODAsImZfa2IiOjAsImlwY19pZCI6W119; _gat_UA-11413116-1=1'
}


#l; redis配置
REDIS = {
    "host": "",
    "port": 0,
    "password": None,
    "url_list_key": "spider_url"
}

# ; mongodb数据库配置
DATABASE = {
    "backend": "database.mongodb",
    "info":{
        "HOST": "",
        "PORT": 0,
        "USER": "",
        "PASSWORD": "",
        "DB_NAME": "",
        "ENABLE": False
    }
}

# ; 代理IP配置
IpProxy = {
    "PROXY_IP_SOURCE": "KuaidailiIpProxyPool",
    "ENABLE": False
}

#; 集群配置

DIST_CONF = {
    "master": "",
    "slaves": ["127.0.0.1"]
}


# ; Zookeeper 监控
ZOOKEEPER = {
    "hosts": "ip:2181",
    "master_node": "/spider",
    "sub_node": "spider_node_",
    "email_receivers": [""]
}

# hdfs配置

HDFS = {
    "url": "",
    "proxy": "",
    "data_path": '/spider',
    "filename": 'dangdang_{}.jsonl'
}
