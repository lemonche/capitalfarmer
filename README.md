# capitalfarmer
解析东方财富网上的API，包装成python库

## 调用方法
~~~
import capitalfarmer as cf
~~~

### cf.time_sharing_trans_3s(code, pos, lang)

获取每隔3秒统计一次的分时成交数据

### cf.recent_minutely(code, ndays, lang)

获取最近ndays内1分钟k线

### cf.recent_minutely_new(code, quota_type, fuquan, lang)

获取最近交易日内的1分钟行情数据  
quota_tyep: r,t2,t3,t4,t5 分别表示最近1天、2天、3天、4天、5天

