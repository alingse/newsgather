# 采集站点文章摘要
  不是转载
  
  本质是一个爬虫项目
  
### 目的 
  
  采集多个`站点`的`文章`的标题，摘要，时间，作者，阅读、评论量等元数据
  
  以便搜索聚合挑选优质文章，然后联系转载，
  
### 模块
 -  reqsite 模块 **完成**
 
    提供某站点的对外网络请求等的封装
 -  db4site 模块 **完成**
    
    提供队列、url去重，旧数据加载等功能 + es 存储功能
 -  sites/* 模块 **完成**
    
    对单个站点的配置具体参考 [`sites／_cnblogs.py`](./sites/_cnblogs.py)
    

### 计划
  
  - 采集:
     * 爬虫，使用python写爬虫(`requests`+`pyquery`+`baidu`,`threading`或`gevent`)
     * 辅助数据库，使用`Berkeley DB`或／`leveldb` 来做去重、队列等数据库(内存限制)
  - 存储：
     * 使用 `elasticsearch` 来做 文章元数据的存储
  - Web:
     * 另一个项目`sitenews`,计划用 tornado + bootstrap

### TODO

  1. 结合几个模块，目前需要一个运行爬虫的模块
  2. 结合所有模块，写一个main函数出来
  2. <s>封装下爬虫 存储的，去重、url队列等。</s> 部分完成
  3. <s>规划下es 配置</s> 完成
  4. <s>站点配置</s> 完成
  