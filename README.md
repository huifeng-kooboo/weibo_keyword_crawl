# weibo_keyword_crawl
Python爬取微博关键词，并且记录相关数据

优势在于：
1. 完善的数据写入机制，方便用户进行数据分析
2. 针对于搜索日期进行优化，有增加了对时间间隔的处理
3. 每天对单个关键词至多可以爬取50页的数据

# 环境安装
1. 需要Python3.8 +的版本

2. 安装依赖环境
```pip install -r requirements.txt```

# 如何使用

1. 配置cookie
在```config.py```文件 ```g_weibo_headers```修改cookie，
cookie从谷歌浏览器上```https://s.weibo.com/```中获取

2.```main.py```中修改```search_config```配置相关搜索信息

3. 运行程序
执行脚本```python main.py```

# 参考部分
借鉴了```https://github.com/nghuyong/WeiboSpider``` 的相关代码

---
#  Join

* if you want to join the projects to contribute the code to this project, you can email 942840260@qq.com or gisdoing@gmail.com, or connect with wechat: ytouching

* 如果想加入这个工程一起贡献开源代码的话，欢迎联系邮箱: 942840260@qq.com 或者 gisdoing@gmail.com 或者微信: ytouching

---

# 使用Q&A
使用过程中存在任何问题，麻烦联系邮箱```942840260@qq.com```,
或者微信```ytouching```

# 支持捐赠 Sponsor
觉得对大家有用的话，欢迎支持，作者也将继续支持爬虫等更新

支付宝收款码
<img src = "https://ytouch-1258011219.cos.ap-nanjing.myqcloud.com/uPic/naicha_zhifu.jpg">

微信收款码
<img src = "https://ytouch-1258011219.cos.ap-nanjing.myqcloud.com/uPic/naicha_weixin.jpg">


-----
#### todo

* 优化代码【已完成】

* 增加搜索多个关键词的功能 【已完成】

* 自动生成cookie的功能
