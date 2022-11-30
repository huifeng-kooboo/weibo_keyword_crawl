from config import g_none_word, g_weibo_host, g_weibo_headers
import requests
from bs4 import BeautifulSoup
import csv

class WeiboCrawler(object):
    """爬虫主入口

    Args:
        object (_type_): _description_
    """
    def __init__(self, search_config: dict):
        self.__search_config = search_config
        self.__search_result = False
    
    
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
            bs_ = BeautifulSoup(self.__result_text,"lxml")
            node_type_list = bs_.find_all("div",{"class":"from"})
            for node_type in node_type_list:
                #print(node_type)
                a_ = node_type.find("a")
                href_link = a_.attrs["href"] # 链接
                redbook_link = f"http:{href_link}"
                with open(file_name, 'a+', newline='') as f:
                    writer = csv.writer(f)
                    data = []
                    data.append(str(redbook_link))
                    writer.writerow(data)
                print(f"微博链接为:{redbook_link}")
            # feed_list = bs_.find_all("a",{"action-type":"feed_list"})
            # print(feed_list)
        # 执行保存操作