
from weibo_crawlers import WeiboCrawler
import dateutil
import datetime
import os
import platform

def parse_weibo_time_list(begin_time:str, end_time: str, day_interval: int = 4):
    """获取 begin 和end的列表集合

    Args:
        begin_time (str): 开始时间
        end_time (str): 结束时间
        day_interval (int, optional): 默认间隔时间4天. Defaults to 4.
    """
    time_list = []
    begin_time_date_ = datetime.datetime.strptime(begin_time,"%Y-%m-%d-%H")
    end_time_date_ = datetime.datetime.strptime(end_time,"%Y-%m-%d-%H")
    if (begin_time_date_+ datetime.timedelta(days=day_interval)) > end_time_date_:
        time_ = [begin_time_date_, end_time_date_]
        time_list.append(time_)
        return time_list
    else:
        time_begin_inter = begin_time_date_
        end_time_inter = begin_time_date_ +  datetime.timedelta(days=day_interval)
        while end_time_inter < end_time_date_:
            time_list.append([time_begin_inter, end_time_inter])
            time_begin_inter = time_begin_inter + datetime.timedelta(days=day_interval)
            end_time_inter = time_begin_inter + datetime.timedelta(days=day_interval) 
        return time_list
        
    
    

search_config = {
    "keyword" : "羽毛球", # 搜索关键词
    "begin_time":"2022-08-01-1",  # 开始时间 2022-11-08-1 ： 表示2022年11月8号1时
    "end_time":"2022-11-03-1",   # 结果时间： 2022-11-25-1：表示2022年11月25号1时
    "page" : "4"  # 页码
}

if __name__ == "__main__":
    """主程序入口
    """
    print("微博搜索BEGIN")
    # 4表示每隔4天搜索时间
    data_time_list = parse_weibo_time_list(search_config.get("begin_time",""),search_config.get("end_time",""),4)
    for time_list in data_time_list:
        begin_time_ = time_list[0].strftime('%Y-%m-%d-%H')
        end_time_ = time_list[1].strftime('%Y-%m-%d-%H')
        print(f"爬取数据开始时间:{begin_time_}, 结束时间:{end_time_}")
        search_config["begin_time"] = begin_time_
        search_config["end_time"] = end_time_
        try:
        # range 调整页码
            for page_num in range(0,20):
                key_word = search_config.get("keyword","")
                search_config["page"] = str(page_num)
                page = search_config.get("page","")
                begin_time = search_config.get("begin_time","")
                end_time = search_config.get("end_time","")
                wb = WeiboCrawler(search_config)
                wb.start_search()
                wb.save_to_file(f"{key_word}_开始时间{begin_time}_{end_time}.csv",True)
        except:
            continue
                
    print("微博搜索END")