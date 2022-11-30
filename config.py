

g_none_word = "None"  # 为空的字段统一使用

# 微博请求头
g_weibo_headers = {
    "user-agent":'''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36''',
   #  "cookie": '''SINAGLOBAL=8442133158314.253.1626682443637; SCF=AiDDMWVizXow9Ozw-iGinLz5Ns36en_sRuc-t5Hf9SSxnYaO0RcT1fUFNfG7GYyYVgwJXNi64qpl7_RHyc6TRLE.; _s_tentry=weibo.com; Apache=6580780117091.589.1669368673389; ULV=1669368673393:5:1:1:6580780117091.589.1669368673389:1664510058554; UOR=login.sina.com.cn,weibo.com,github.com; SUB=_2A25Ohc2fDeRhGeRN71oW9C_Jwj6IHXVt8rhXrDV8PUNbmtANLUb5kW9NU7PGeHlSMJvsA5O1AZNoW6oRcmzWBEmC; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWqQKicwefG8NILG0Ep.eDf5JpX5KzhUgL.Foz0ShnNSh2f1Kz2dJLoIpjLxKqL1-BL1-eLxKnLB.-L1h.LxK.L1KBL12zt; ALF=1700983119; SSOLoginState=1669447119; PC_TOKEN=cfe4d160bd''',
    "cookie": '''SINAGLOBAL=8442133158314.253.1626682443637; SCF=AiDDMWVizXow9Ozw-iGinLz5Ns36en_sRuc-t5Hf9SSxnYaO0RcT1fUFNfG7GYyYVgwJXNi64qpl7_RHyc6TRLE.; _s_tentry=weibo.com; Apache=6580780117091.589.1669368673389; ULV=1669368673393:5:1:1:6580780117091.589.1669368673389:1664510058554; SSOLoginState=1669447119; UOR=login.sina.com.cn,weibo.com,www.google.com; login_sid_t=049c9099b05d79d348321b1cc1693d41; cross_origin_proto=SSL; PC_TOKEN=366d620510; SUB=_2A25Ogy39DeRhGeRN71oW9C_Jwj6IHXVt-Rg1rDV8PUNbmtANLRnukW9NU7PGeDHPtFzLD7Vv3Hl-gAIVUMxzBizL; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWqQKicwefG8NILG0Ep.eDf5JpX5KzhUgL.Foz0ShnNSh2f1Kz2dJLoIpjLxKqL1-BL1-eLxKnLB.-L1h.LxK.L1KBL12zt; ALF=1701351725''',
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding":"gzip, deflate, br", 
    "accept-language":"zh-CN,zh;q=0.9,ko;q=0.8,en;q=0.7",
    "cache-control":"max-age=0",
    "sec-ch-ua":'''"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"''',
    "sec-fetch-dest" :"document",
    "sec-fetch-site": "none",
    "sec-fetch-user":"?1",
    "upgrade-insecure-requests": "1",
    "sec-fetch-mode":"navigate",
}

# 微博Host
g_weibo_host = "https://s.weibo.com/weibo?"


class WeiboData():
    """需要记录的微博数据列表
    """
    def __init__(self):
        self.keyword = ""  # 关键词
        self.post_content = ""  # 帖子内容
        self.post_url = "" # 帖子链接
        self.post_liked = "" # 帖子点赞数
        self.post_transpond = "" # 帖子转发数
        self.post_comment = "" # 帖子评论数
        self.post_image_videos_link = "" # 图片视频链接
        self.post_release_time = "" # 发布时间
        self.post_user_id = "" # 发布人的id
        self.post_user_name = "" # 发帖人姓名
        self.post_account_type = "" # 发布人的账号类型
        self.post_fans_num = "" # 发布人的粉丝数
        self.post_author_brief = "" # 作者简介
        self.post_ip_pos = "" # ip归属地
        self.post_gender = "" # 性别
        self.post_all_weibo_nums = "" # 全部微博数量
