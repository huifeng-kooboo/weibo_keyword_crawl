from config import g_none_word, g_weibo_host, g_weibo_headers, WeiboData, is_mac_os
import requests
from bs4 import BeautifulSoup
import csv
import re
import json
import os
import dateutil.parser
import time


def get_time_stamp_str():
    """获取返回时间戳
    """
    current_time = time.time()
    local_time = time.localtime(current_time)
    time_stamp = time.strftime("%Y-%m-%d-%H-%M-%S",local_time)
    return time_stamp

def base62_decode(string):
    """
    base
    """
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = str(string)
    num = 0
    idx = 0
    for char in string:
        power = (len(string) - (idx + 1))
        num += alphabet.index(char) * (len(alphabet) ** power)
        idx += 1

    return num


def reverse_cut_to_length(content, code_func, cut_num=4, fill_num=7):
    """
    url to mid
    """
    content = str(content)
    cut_list = [content[i - cut_num if i >= cut_num else 0:i] for i in range(len(content), 0, (-1 * cut_num))]
    cut_list.reverse()
    result = []
    for i, item in enumerate(cut_list):
        s = str(code_func(item))
        if i > 0 and len(s) < fill_num:
            s = (fill_num - len(s)) * '0' + s
        result.append(s)
    return ''.join(result)


def url_to_mid(url: str):
    """>>> url_to_mid('z0JH2lOMb')
    3501756485200075
    """
    result = reverse_cut_to_length(url, base62_decode)
    return int(result)


def parse_time(s):
    """
    Wed Oct 19 23:44:36 +0800 2022 => 2022-10-19 23:44:36
    """
    # return "2022-10-19 23:44:36"
    return dateutil.parser.parse(s).strftime('%Y-%m-%d %H:%M:%S')


def parse_user_info(data):
    """
    解析用户信息
    """
    # 基础信息
    user = {
        "_id": str(data['id']),
        "avatar_hd": data['avatar_hd'],
        "nick_name": data['screen_name'],
        "verified": data['verified'],
    }
    # 额外的信息
    keys = ['description', 'followers_count', 'friends_count', 'statuses_count',
            'gender', 'location', 'mbrank', 'mbtype', 'credit_score']
    for key in keys:
        if key in data:
            user[key] = data[key]
    if 'created_at' in data:
        user['created_at'] = parse_time(data.get('created_at'))
    if user['verified']:
        user['verified_type'] = data['verified_type']
        if 'verified_reason' in data:
            user['verified_reason'] = data['verified_reason']
    return user


class WeiboCrawler(object):
    """爬虫主入口

    Args:
        object (_type_): _description_
    """
    def __init__(self, search_config: dict):
        self.__search_config = search_config
        self.__search_result = False
        self.__key_word = search_config.get("keyword",g_none_word)
    
    
    def start_search(self, is_need_multithreading: bool = False):
        """_summary_

        Args:
            is_need_multithreading (bool, optional): 是否需要开启多线程. Defaults to False.

        Returns:
            bool: 是否搜索成功
        """
        keyword = self.__search_config.get("keyword",g_none_word)
        if keyword == g_none_word:
            print("..........未提供关键词，搜索失败............")
            return False
        print(f"搜索开始，关键词为:{keyword}")
        is_search_by_time = True
        begin_time = self.__search_config.get("begin_time",g_none_word)
        end_time = self.__search_config.get("end_time",g_none_word)
        page = self.__search_config.get("page",g_none_word)
        if begin_time == g_none_word or end_time == g_none_word:
            print("开始时间或者结束时间设置为空")
            is_search_by_time = False
        if is_search_by_time:
            time_scope = f"custom%3A{begin_time}%3A{end_time}"
            print(f"构建搜索时间范围成功：字段参数为:{time_scope}")
            req_url = f"{g_weibo_host}q={keyword}&typeall=1&suball=1&timescope={time_scope}&Refer=g&page={page}"
            print(f"需要搜索的url地址构建成功，地址为: {req_url}")
            resp = requests.get(req_url, headers=g_weibo_headers)
            if resp.status_code !=200:
                print(f".....{req_url} 网址响应异常......")
                return False
            try:
                resp.encoding = "utf-8"
                resp_text = resp.text
                self.__search_result = True
                self.__result_text = resp_text
                return True
            except:
                print("搜索结果异常")
                return False
        else:
            req_url = f"https://s.weibo.com/weibo?q={keyword}&Refer=index"
            print(f"需要搜索的url地址构建成功，地址为: {req_url}")
            resp = requests.get(req_url, headers=g_weibo_headers)
            if resp.status_code !=200:
                print(f".....{req_url} 网址响应异常......")
                return False
            try:
                resp.encoding = "utf-8"
                resp_text = resp.text
                self.__result_text = resp_text # 返回结果保存
                self.__search_result = True
                return True
            except:
                print("搜索结果异常")
                return False
        return False
    
    def parse_blog_info(self, data):
        # print(f"blog_data:{data}")
        source_ = data.get("source",g_none_word)
        print(f"source_:{source_}")
        tweet = {
        "_id": str(data['mid']),
        "mblogid": data['mblogid'],  # 博客id
        "created_at": parse_time(data['created_at']),  # 文章发布时间
        "geo": data.get('geo',g_none_word),
        "ip_location": data.get('region_name', g_none_word),
        "reposts_count": data.get('reposts_count',g_none_word),
        "comments_count": data.get('comments_count',g_none_word),
        "attitudes_count": data.get('attitudes_count',g_none_word),
        "source": data.get("source",g_none_word),
        "content": data.get('text_raw',g_none_word).replace('\u200b', ''),
        "pic_urls": ["https://wx1.sinaimg.cn/orj960/" + pic_id for pic_id in data.get('pic_ids', [])],
        "pic_num": data['pic_num'],
        'isLongText': False,
        "user": parse_user_info(data['user']),
        }
        if 'page_info' in data and data['page_info'].get('object_type', '') == 'video':
            tweet['video'] = data['page_info']['media_info']['mp4_720p_mp4']
        tweet['url'] = f"https://weibo.com/{tweet['user']['_id']}/{tweet['mblogid']}"  # 文章地址
        if 'continue_tag' in data and data['isLongText']:
            tweet['isLongText'] = True
        return tweet
    
    
    def save_wb_data(self, file_name, wb_data:WeiboData):
        data_dict = wb_data.__dict__
        is_first = False
        if os.path.exists(file_name):
            is_first = False
        else:
            is_first = True
        is_mac = is_mac_os()
        if is_mac:
            with open(file_name, 'a+', newline='') as f:
                writer = csv.writer(f)
                if is_first == True:
                    first_data = ["关键词","帖子内容","帖子链接","帖子点赞数",
                              "帖子转发数","帖子评论数","图片视频链接",
                              "发布时间","发布者的id","发布者的姓名",
                              "发布人的账号类型","发布人的粉丝数","作者简介",
                              "ip归属地","性别","全部微博数量","微博标签","图片视频类型","博主分类","公司","大学","加入微博时间","信用","爬取时间","发布终端"]
                    writer.writerow(first_data)
                data = []
                for item_ in data_dict.values():
                    data.append(item_)
                writer.writerow(data)
        else:
            try:
                with open(file_name, 'a+', newline='',encoding='gbk') as f:
                    writer = csv.writer(f)
                    if is_first == True:
                        first_data = ["关键词","帖子内容","帖子链接","帖子点赞数",
                              "帖子转发数","帖子评论数","图片视频链接",
                              "发布时间","发布者的id","发布者的姓名",
                              "发布人的账号类型","发布人的粉丝数","作者简介",
                              "ip归属地","性别","全部微博数量","微博标签","图片视频类型","博主分类","公司","大学","加入微博时间","信用","爬取时间","发布终端"]
                        writer.writerow(first_data)
                    data = []
                    for item_ in data_dict.values():
                        data.append(item_)
                    writer.writerow(data)
            except:
                pass
            
    def save_to_file(self, file_name:str, is_appended:bool = True):
        """保存到文件中

        Args:
            file_name (str): 文件名
            is_appended (bool, optional): 是否需要追加的形式写入. Defaults to True.
        Returns:
            bool: 是否保存数据成功
            str: 相关说明
        """
        if self.__search_result == False:
            return False, "未搜索到数据，无法保存"
        else:
            result_text = self.__result_text # 结果
            tweet_ids = re.findall(r'\d+/(.*?)\?refer_flag=1001030103_\'\)">复制微博地址</a>', result_text)
            for tweet_id in tweet_ids:
                wb_data = WeiboData() # 需要记录的微博数据
                wb_data.keyword = self.__key_word # 关键词
                url = f"https://weibo.com/ajax/statuses/show?id={tweet_id}"
                resp_blog = requests.get(url, headers=g_weibo_headers)
                resp_blog.encoding = 'utf-8'
                response_text_blog = resp_blog.text
                data = json.loads(response_text_blog)
                item_blog = self.parse_blog_info(data) # 博客数据
                if item_blog["isLongText"]:
                    # 长篇文章
                    long_id = item_blog['mblogid']
                    url_long_text = "https://weibo.com/ajax/statuses/longtext?id=" + item_blog['mblogid']
                    resp_long = requests.get(url_long_text,headers=g_weibo_headers)
                    resp_long.encoding = 'utf-8'
                    data_long = json.loads(resp_long.text)['data']
                    wb_data.post_content = data_long['longTextContent']
                else:
                    wb_data.post_content = item_blog.get("content",g_none_word) # 帖子内容
                # wb_data.post_content = item_blog.get("content",g_none_word) # 帖子内容
                wb_data.post_release_terminal = item_blog.get('source',g_none_word) # 终端
                wb_data.post_url = item_blog.get("url",g_none_word) # 帖子链接
                wb_data.post_liked = item_blog.get("attitudes_count","0") # 点赞
                wb_data.post_transpond = item_blog.get("reposts_count","0") # 转发
                wb_data.post_comment = item_blog.get("comments_count","0") # 评论
                wb_data.post_image_videos_link = str(item_blog.get("video",g_none_word)) + str(item_blog.get("pic_urls",g_none_word)) # 图片记录
                if item_blog.get("video",g_none_word) != g_none_word:
                    wb_data.post_all_image_video_type = "视频"
                elif item_blog.get("pic_urls",g_none_word) != g_none_word:
                    wb_data.post_all_image_video_type = "图片"
                else:
                    wb_data.post_all_image_video_type = "None"
                try:
                    wb_data.post_release_time = item_blog.get("created_at",g_none_word) # 发布时间
                    wb_data.post_user_id = item_blog["user"]["_id"] # 发布者的id
                    wb_data.post_user_name = item_blog["user"]["nick_name"]
                except:
                    pass
                wb_data.post_scrapy_time = get_time_stamp_str() # 爬取微博的时间
                for key_, value_ in item_blog.items():
                    if key_ == "user":
                        user_dict = value_
                        user_id = user_dict["_id"]
                        user_url = f'https://weibo.com/ajax/profile/info?uid={user_id}' # 用户链接
                        resp_user = requests.get(user_url,headers=g_weibo_headers)
                        resp_user.encoding = "utf-8"
                        data_user = json.loads(resp_user.text)
                        base_info = data_user["data"]["user"]
                        print(f"用户base_info:{base_info}")
                        item_user = parse_user_info(data_user["data"]["user"])
                        url_user_info = f"https://weibo.com/ajax/profile/detail?uid={item_user['_id']}"
                        resp_user_info = requests.get(url_user_info,headers=g_weibo_headers)
                        data_user_info = json.loads(resp_user_info.text)['data']
                        print(f"用户user_info:{data_user_info}")
                        item_user['birthday'] = data_user_info.get('birthday', g_none_word)
                        wb_data.post_blogger_type = item_user.get('verified_reason',g_none_word)
                        if data_user_info.get("sunshine_credit",g_none_word) != g_none_word:
                            sunshine_ = data_user_info.get("sunshine_credit")
                            level_ = sunshine_.get("level",g_none_word)
                            wb_data.post_incredit = level_
                        wb_data.post_company = data_user_info.get('company', g_none_word)
                        if data_user_info.get("education",g_none_word) != g_none_word:
                            sunshine_ = data_user_info.get("education")
                            level_ = sunshine_.get("school",g_none_word)
                            wb_data.post_university = level_
                        try:
                            wb_data.post_add_time_to_weibo =  data_user_info.get('created_at', g_none_word)
                            label_desc = data_user_info.get("label_desc",g_none_word)
                            if label_desc == g_none_word:
                                pass
                            else:
                                tags_ = ""
                                for label in label_desc:
                                    name_ = label.get("name",g_none_word)
                                    if name_ != g_none_word:
                                        tags_ += f"{name_},"
                                if tags_!="":
                                    wb_data.post_all_weibo_tags = tags_
                                else:
                                     wb_data.post_all_weibo_tags = g_none_word
                        except:
                            pass
                        
                        if 'created_at' not in item_user:
                            item_user['created_at'] = data_user_info.get('created_at', g_none_word)
                        item_user['desc_text'] = data_user_info.get('desc_text', g_none_word)
                        item_user['ip_location'] = data_user_info.get('ip_location', g_none_word)
                        item_user['sunshine_credit'] = data_user_info.get('sunshine_credit', {}).get('level', g_none_word)
                        item_user['label_desc'] = [label['name'] for label in data_user_info.get('label_desc', [])]
                        if 'company' in data_user_info:
                            item_user['company'] = data_user_info['company']
                        if 'education' in data_user_info:
                            item_user['education'] = data_user_info['education']
                        verified_type_str = item_user.get("verified_type",g_none_word)
                        if verified_type_str != g_none_word:
                            if verified_type_str == 0 or verified_type_str == "0":
                                wb_data.post_account_type = "黄V"
                            elif verified_type_str == 7 or verified_type_str == "7":
                                wb_data.post_account_type = "蓝V"
                            else:
                                wb_data.post_account_type = "无认证"
                        else:
                            wb_data.post_account_type = "无认证"
                        
                        try:
                            wb_data.post_fans_num = item_user.get("friends_count",g_none_word) # 粉丝数
                            wb_data.post_author_brief = item_user.get("description",g_none_word) # 简介
                            wb_data.post_ip_pos = item_user.get("ip_location",g_none_word)
                        except:
                            pass
                        try:
                            sex = item_user.get("gender","m") # m 男性
                            if sex == "m":
                                wb_data.post_gender = "男"
                            else:
                                wb_data.post_gender = "女"
                            wb_data.post_all_weibo_nums  = item_user.get("statuses_count",g_none_word)
                        except:
                            pass
                        self.save_wb_data(file_name,wb_data)
                        
                        
                
                