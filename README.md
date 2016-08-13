# 采集站点文章摘要
  ----不是转载
  
### 目的 
  
  采集多个站点的`文章`的标题，摘要，时间，作者，阅读、评论量等元数据
  
  以便搜索聚合挑选优质文章，然后联系转载，
  

### 计划
  
  - 采集:
     * 爬虫，使用python写爬虫(`requests`+`pyquery`+`baidu`,`threading`或`gevent`)
     * 辅助数据库，使用`Berkeley DB`或／`leveldb` 来做去重、队列等数据库(内存限制)
  - 存储：
     * 使用 `elasticsearch` 来做 文章元数据的存储
  - Web:
     * 参考另一个项目`sitenews`,计划用 tornado + bootstrap

### TODO

  1. 写一个站点间通用的广度访问的东西，放到队列里，
  2. 封装下爬虫 存储的，去重、url队列等。
  3. 规划下es 配置
  