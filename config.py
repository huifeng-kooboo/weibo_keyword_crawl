

g_none_word = "None"  # 为空的字段统一使用

# 微博请求头
g_weibo_headers = {
    "user-agent":'''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36''',
    "cookie": '''SINAGLOBAL=8442133158314.253.1626682443637; UOR=login.sina.com.cn,weibo.com,www.google.com.hk; SCF=Aogk9bIUTRGH0-90pf0cHgo6aTBNG1Ja9dzC7fr27WMOo9vspUc-M4gLlCiXJFDfCSAW6kKIbevF6JTUu6dy3qk.; ALF=1718948954; SUB=_2A25LSfcLDeRhGeRN71oW9C_Jwj6IHXVoJ3bDrDV8PUJbkNAGLXb3kW1NU7PGeHXAsQFUlpwb7qqQrEmb2jxeVpGH; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWqQKicwefG8NILG0Ep.eDf5JpX5KMhUgL.Foz0ShnNSh2f1Kz2dJLoIpjLxKqL1-BL1-eLxKnLB.-L1h.LxK.L1KBL12zt; _s_tentry=-; Apache=8781883208.852648.1716356956647; ULV=1716356956655:29:2:1:8781883208.852648.1716356956647:1714660326941; XSRF-TOKEN=UtIXy8Df-3vteZ8hPUWAby0R; WBPSESS=5wJyffL-CzuDMohJ6cqKmF941RsEE4ggDzsxBzyjKB4_qTigjjb5npyvd4hzq1ZJo3QE0GH0Fxr_aQOjFZ7VvJCWK7KpFQsKFY1BtTlAg6RqdUBJRwEF1X7O8BruXQff''',
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

import platform

def is_mac_os():
    """判断是否为mac系统

    Returns:
        _type_: _description_
    """
    sys_platform = platform.platform().lower()
    if sys_platform.count("macos") > 0:
        return True
    return False

class WeiboData():
    """需要记录的微博数据列表
    """
    def __init__(self):
        self.keyword = ""  # 关键词  ☑️  【保留】
        self.post_content = ""  # 帖子内容 ☑️ 【保留】
        self.post_url = "" # 帖子链接 ☑️ 【保留】
        self.post_liked = "" # 帖子点赞数
        self.post_transpond = "" # 帖子转发数
        self.post_comment = "" # 帖子评论数
        self.post_image_videos_link = "" # 图片视频链接
        self.post_release_time = "" # 发布时间 【保留】
        self.post_user_id = "" # 发布人的id 【保留】
        self.post_user_name = "" # 发帖人姓名  ☑️
        self.post_account_type = "" # 发布人的账号类型
        self.post_fans_num = "" # 发布人的粉丝数 【保留】
        self.post_concerns_num = "none" # 发布人的关注数【保留】
        self.post_author_brief = "" # 作者简介
        self.post_ip_pos = "" # ip归属地
        self.post_gender = "" # 性别
        self.post_all_weibo_nums = "" # 全部微博数量
        self.post_all_weibo_tags = ""  # 标签
        self.post_all_image_video_type = "1" # 图片或者视频类型
        self.post_blogger_type = "无" # 博主分类
        self.post_company = "company" # 公司
        self.post_university = "university" #大学
        self.post_add_time_to_weibo = "weibo-time" # 加入微博时间
        self.post_incredit = "信用" # 信用极好
        self.post_scrapy_time = "time" # 爬取时间
        self.post_release_terminal = "手机" # 发布终端