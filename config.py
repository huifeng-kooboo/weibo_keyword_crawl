

g_none_word = "None"  # 为空的字段统一使用

# 微博请求头
g_weibo_headers = {
    "user-agent":'''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36''',
    "cookie": '''SINAGLOBAL=8442133158314.253.1626682443637; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWqQKicwefG8NILG0Ep.eDf5JpX5KMhUgL.Foz0ShnNSh2f1Kz2dJLoIpjLxKqL1-BL1-eLxKnLB.-L1h.LxK.L1KBL12zt; ALF=1672496228; SSOLoginState=1669904229; SCF=AiUCu1UuXqnKGG3UVTsT5Kw_g3FfTTBsdquxuXiL-npEPILq8RbvYE4dCxPZFiY9XLEE2ORpImGc_zivyIwI8lI.; SUB=_2A25OjMc2DeRhGeRN71oW9C_Jwj6IHXVt-7_-rDV8PUNbmtANLUT9kW9NU7PGeJ3DB13mANevZ0Uhf_krxki104GY; _s_tentry=login.sina.com.cn; UOR=login.sina.com.cn,weibo.com,login.sina.com.cn; Apache=6512818099088.22.1669904230629; ULV=1669904230645:7:1:2:6512818099088.22.1669904230629:1669817521492''',
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
        self.keyword = ""  # 关键词  ☑️
        self.post_content = ""  # 帖子内容 ☑️
        self.post_url = "" # 帖子链接 ☑️
        self.post_liked = "" # 帖子点赞数
        self.post_transpond = "" # 帖子转发数
        self.post_comment = "" # 帖子评论数
        self.post_image_videos_link = "" # 图片视频链接
        self.post_release_time = "" # 发布时间
        self.post_user_id = "" # 发布人的id
        self.post_user_name = "" # 发帖人姓名  ☑️
        self.post_account_type = "" # 发布人的账号类型
        self.post_fans_num = "" # 发布人的粉丝数
        self.post_author_brief = "" # 作者简介
        self.post_ip_pos = "" # ip归属地
        self.post_gender = "" # 性别
        self.post_all_weibo_nums = "" # 全部微博数量
