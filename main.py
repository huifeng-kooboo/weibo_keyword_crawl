
from weibo_crawlers import WeiboCrawler

search_config = {
    "keyword" : "补气血", # 搜索关键词
    "begin_time":"2022-11-01-1",  # 开始时间 2022-11-08-1 ： 表示2022年11月8号1时
    "end_time":"2022-11-25-1",   # 结果时间： 2022-11-25-1：表示2022年11月25号1时
    "page" : "4"  # 页码
}

if __name__ == "__main__":
    """主程序入口
    """
    print("微博搜索BEGIN")
    # 设置页码：默认0---20页
    for page_num in range(0,20):
        key_word = search_config.get("keyword","")
        search_config["page"] = str(page_num)
        page = search_config.get("page","")
        begin_time = search_config.get("begin_time","")
        end_time = search_config.get("end_time","")
        wb = WeiboCrawler(search_config)
        wb.start_search()
        wb.save_to_file(f"{key_word}_开始时间{begin_time}_{end_time}.csv",True)
    print("微博搜索END")