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
 -  runutil 模块 **完成**
   
    多线程运行单元
   
 -  main  模块 **完成**
   
    程序主体部分，基本完成，不过还很粗糙

### 基本架构

   `main.py` 利用封装好的 `siteReq`,`siteDB`,`runUnit`等类加上提供的utils函数，
   
   预先从 `sites/*` 中读取`sitelist`，然后逐一采集

   `main.py`利用`runutil.py`中多线程辅助函数生成若干个线程，并等待这些线程工作完毕,
    并开始下一个`site`的采集。
   
   其中单一线程的运行流程即：
   
   1. 调用 sitedb ，从队列中取出 `link`
   2. 调用 sitereq 取得网页,解析得到两种链接`urls`,`indexes`,`urls` 即待采集的文章，`indexes`可看做索引页，将这些链接放回db
   3. 用上一步的`urls`采集文章的`meta`,调用sitedb 的接口存储，返回第一步

可以贴个图，但是懒得画，改天吧


### 计划
  
  - 采集:
     * 爬虫，使用python写爬虫(`requests`+`pyquery`+`baidu`,`threading`或`gevent`)
     * 辅助数据库，使用`Berkeley DB`或／`leveldb` 来做去重、队列等数据库(内存限制)
  - 存储：
     * 使用 `elasticsearch` 来做 文章元数据的存储
  - Web:
     * 另一个项目`sitenews`,计划用 tornado + bootstrap


### TODO

  1. <s>结合几个模块，目前需要一个运行爬虫的模块</s> 完成,不过没有单独放出来，在`main.py` 中
  2. <s>结合所有模块，写一个main函数出来</s> 完成
  3. <s>封装下爬虫 存储的，去重、url队列等。</s> 部分完成
  4. <s>规划下es 配置</s> 完成
  5. <s>站点配置</s> 完成
  6. `main`函数优化，以及相关参数配置
  