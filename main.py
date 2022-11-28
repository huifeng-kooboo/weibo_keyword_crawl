
from weibo_crawlers import WeiboCrawler

search_config = {
    "keyword" : "C罗", # 搜索关键词
    "begin_time":"2022-11-01-1",  # 开始时间 2022-11-08-1 ： 表示2022年11月8号1时
    "end_time":"2022-11-25-1",   # 结果时间： 2022-11-25-1：表示2022年11月25号1时
}

if __name__ == "__main__":
    """主程序入口
    """
    print("微博搜索BEGIN")
    wb = WeiboCrawler(search_config)
    wb.start_search()
    print("微博搜索END")