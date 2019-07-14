# capitalfarmer
解析东方财富网上的API，包装成python库

## 调用方法
~~~
import capitalfarmer as cf
~~~

## 分时成交数据

### cf.time_sharing_trans_3s(code, pos, lang)
获取最近pos个每隔3秒统计一次的分时成交数据

### cf.time_sharing_trans(code, lang)
获取当日每隔3秒统计一次的分时成交数据

## 交易行情数据

### cf.recent_minutely(code, ndays, lang)
获取最近ndays内1分钟k线

### cf.recent_minutely_new(code, quota_type, fuquan, lang)
获取最近交易日内的1分钟行情数据  
quota_tyep: r,t2,t3,t4,t5 分别表示最近1天、2天、3天、4天、5天

### cf.quota_minutely(code, fuquan, lang)
获取最近1个交易日内的1分钟k线

### cf.quota(code, quota_type, fuquan, lang)
获取k线行情，5分钟、15分钟、30分钟、60分钟、日k、周k、月k

## 资金流向

### cf.moneyflow(code, lang)
当日个股资金流向

### cf.hist_moneyflow(code, lang)
历史每日统计的资金流向

## 机构持仓

### cf.insti_postion(code, date, insti_type, lang)
指定报告期，机构持有该股的仓位状况  
date:指定报告期  
insti_type:指定机构类型，0全部、1基金、2QFII、3社保、5保险、4券商、6信托

## 股东分析

### cf.biggest_stock_holder_lt(code, date, lang)
指定报告期，前十大流通股东

### cf.biggest_stock_holder_sd(code, date, lang)
指定报告期，前十大股东

### cf.stock_holder_number(code, lang)
不定期统计的股东数量

## 龙虎榜

### cf.longhu_detail(date, start_date, end_date, lang)
获取指定日期，或者指定日期区间内，龙虎榜数据

### cf.longhu_stock_stats(date, start_date, end_date, lang)
获取指定日期，或者指定日期区间内，根据stock统计龙虎榜的数据

### cf.longhu_insti_stats(date, start_date, end_date, lang)
获取指定日期，或者指定日期区间内，根据institutional统计龙虎榜的数据

## 证券营业部交易数据

### cf.active_business_dept(date, start_date, end_date, lang)
获取活跃营业部交易数据

### cf.insti_chair_track(date, start_date, end_date, lang)
追踪机构席位的交易数据

### cf.business_dept_stats(date, start_date, end_date, lang)
营业部交易统计

### cf.business_dept_ranking(date, start_date, end_date, lang)
营业部排序

### cf.business_dept_detail(sale_code, date, start_date, end_date, lang)
营业部交易数据详细

## 融资融券交易数据

### cf.hist_margin_trade(code, lang)
融资融券交易数据

## 沪深港股通交易数据

### cf.hgst_detail(code, date, start_date, end_date)
沪深港通交易数据详细

### cf.hgst_stats(code, lang)
沪深港通交易数据统计
