from . import quotation
from . import capitalflow
from . import longhu
from . import margintrade
import pandas as pd
from .finance import zcfzb as BalanceReport
from .finance import lrb as ProfitReport
from .finance import xjllb as CashFlowReport
import numpy as np
import json
import datetime
from . import hgst


def time_sharing_trans_3s(code, pos=-10, lang='en'):
    info, data = quotation.time_sharing_trans_3s(code, pos)
    data = pd.DataFrame(data, columns=info['fields'])
    data = data[["time", "price", "hands", "color"]]
    if lang == 'zh':
        headers = {"time": '时间',
                   'price': '价格',
                   'hands': '手数',
                   }
        data.rename(columns=headers, inplace=True)
    return data


def recent_minutely(code, ndays=1, lang='en'):
    info, data = quotation.recent_minutely(code, ndays)
    data = pd.DataFrame(data, columns=info['fields'])
    if lang == 'zh':
        headers = {'datetime': '日期',
                   'open': '开盘价',
                   'close': '收盘价',
                   'high': '最高价',
                   'low': '最低价',
                   'hands': '手数',
                   'amount': '总额',
                   'avgprice': '均价'
                   }
        data.rename(columns=headers, inplace=True)
    return data


def recent_minutely_new(code, quota_type='r', fuquan='', lang='en', **kwargs):
    info, data = quotation.recent_minutely_new(code, quota_type, fuquan, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])
    data = data[['datetime', 'close', 'hands', 'avgprice']]
    if lang == 'zh':
        headers = {'datetime': '日期',
                   'close': '收盘价',
                   'hands': '手数',
                   'avgprice': '均价'
                   }
        data.rename(columns=headers, inplace=True)
    return data


def quota_minutely(code, fuquan='', lang='en', **kwargs):
    fields, data = quotation.quota_minutely(code, fuquan, **kwargs)
    data = pd.DataFrame(data, columns=fields)
    data = data[['datetime', 'open', 'high', 'low', 'close', 'avgprice', 'volume', 'amount']]
    if lang == 'zh':
        headers = {'datetime': '日期',
                   'open': '开盘价',
                   'close': '收盘价',
                   'high': '最高价',
                   'low': '最低价',
                   'volume': '总量',
                   'amount': '总额',
                   'avgprice': '均价'
                   }
        data.rename(columns=headers, inplace=True)
    return data


def quota(code, quota_type='k', fuquan='', lang='en', **kwargs):
    info, data = quotation.quota(code, quota_type, fuquan, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])
    headers = {'datetime': '日期',
               'open': '开盘价',
               'close': '收盘价',
               'high': '最高价',
               'low': '最低价',
               'volume': '总量',
               'amount': '总额',
               'zhenfu': '振幅'
               }
    data = data[list(headers.keys())]
    if lang == 'zh':
        data.rename(columns=headers, inplace=True)
    return data


def time_sharing_transaction(code, lang='en', **kwargs):
    fields, data = quotation.time_sharing_trans(code, **kwargs)
    data = pd.DataFrame(data, columns=fields)
    data = data[['time', 'price', 'hands', 'color', 'direction']]
    if lang == 'zh':
        headers = {'time': '时间',
                   'price': '价格',
                   'hands': '手数',
                   'direction': '涨跌方向',
                   }
        data.rename(columns=headers, inplace=True)
    return data


def moneyflow(code, lang='en', **kwargs):
    fields, data = capitalflow.moneyflow(code, lang='en', **kwargs)
    data = pd.DataFrame(data, columns=fields)
    headers = {'time': '时间',
               'inflow': '总流入',
               'outflow': '总流出',
               'net_inflow': '净流入',
               'super_infow': '超大单流入',
               'super_outflow': '超大单流出',
               'super_net_inflow': '超大单净流入',
               'large_inflow': '大单流入',
               'large_outflow': '大单流出',
               'large_net_inflow': '大单净流入',
               'mid_inflow': '中单流入',
               'mid_outflow': '中单流出',
               'mid_net_inflow': '中单净流入',
               'small_inflow': '小单流入',
               'small_outflow': '小单流出',
               'small_net_inflow': '小单净流入',
               }
    data = data[list(headers.keys())]
    if lang == 'zh':
        data.rename(columns=headers, inplace=True)
    return data


def hist_moneyflow(code, lang='en', **kwargs):
    fields, data = capitalflow.hist_moneyflow(code, **kwargs)
    data = pd.DataFrame(data, columns=fields).sort_values("date", ascending=False).reset_index(drop=True)
    headers = {'date': '日期',
               'inflow': '总流入',
               'outflow': '总流出',
               'net_inflow': '净流入',
               'super_inflow': '超大单流入',
               'super_outflow': '超大单流出',
               'super_net_inflow': '超大单净流入',
               'super_net_infow_percentage': '超大单净流入占比',
               'large_inflow': '大单流入',
               'large_outflow': '大单流出',
               'large_net_inflow': '大单净流入',
               'large_net_infow_percentage': '大单净流入占比',
               'mid_inflow': '中单流入',
               'mid_outflow': '中单流出',
               'mid_net_inflow': '中单净流入',
               'mid_net_infow_percentage': '中单净流入占比',
               'small_inflow': '小单流入',
               'small_outflow': '小单流出',
               'small_net_inflow': '小单净流入',
               'small_net_infow_percentage': '小单净流入占比',
               'close': '收盘价',
               'up_down_percentage': '涨跌幅',
               }
    data = data[list(headers.keys())]
    if lang == 'zh':
        data.rename(columns=headers, inplace=True)
    return data


def insti_position(code, date, insti_type='', lang='en', **kwargs):
    info, data = capitalflow.insti_position(code, date, insti_type=insti_type, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])
    if lang == 'zh':
        headers = {
            "SCode": "证券代码",
            "SName": "证券名称",
            "RDate": "报告期",
            "SHCode": "产品代码",
            "SHName": "产品名称",
            "IndtCode": "机构代码",
            "InstSName": "机构名称",
            "TypeCode": "机构类型编码",
            "Type": "机构类型",
            "ShareHDNum": "持仓股数",
            "Vposition": "持仓市值",
            "TabRate": "持仓占总股本比",
            "TabProRate": "持仓占流通股比",
        }
        data.rename(columns=headers, inplace=True)
    return data


def biggest_stock_holder_lt(code, date, lang='en'):
    data = capitalflow.biggest_stock_holder(code, date, type="Lt")
    data = pd.DataFrame(data)
    headers = {
        'RDATE': '报告期',
        'NDATE': '公告日期',
        'SCODE': '证券代码',
        'SNAME': '证券名称',
        'RANK': '股东排序',
        'SHAREHDCODE': '股东机构代码',
        'SHAREHDNAME': '股东机构名称',
        'SHAREHDTYPE': '机构类型',
        'SHAREHDNUM': '持股数量',
        'LTAG': '持仓市值',
        'SHAREHDRATIO': '占总股本比例',
        'ZB': '占流通股比例',
        'SHARESTYPE': '股份类型',
        'BDBL': '增长率',
        'BDSUM': '增长',
        'BZ': '较上期变化',
    }
    data = data[list(headers.keys())]
    if lang == 'zh':
        data.rename(columns=headers, inplace=True)
    return data


def biggest_stock_holder_sd(code, date, lang='en'):
    data = capitalflow.biggest_stock_holder(code, date, type="Sd")
    data = pd.DataFrame(data)
    headers = {
        'RDATE': '报告期',
        'NDATE': '公告日期',
        'SCODE': '证券代码',
        'SNAME': '证券名称',
        'RANK': '股东排序',
        'SHAREHDCODE': '股东机构代码',
        'SHAREHDNAME': '股东机构名称',
        'SHAREHDTYPE': '机构类型',
        'SHAREHDNUM': '持股数量',
        'LTAG': '持仓市值',
        'SHAREHDRATIO': '占总股本比例',
        'ZB': '占流通股比例',
        'SHARESTYPE': '股份类型',
    }
    data = data[list(headers.keys())]
    if lang == 'zh':
        data.rename(columns=headers, inplace=True)
    return data


def stock_holder_number(code, lang='en', **kwargs):
    data = capitalflow.stock_holder_number(code, **kwargs)
    data = pd.DataFrame(data)
    if lang == 'zh':
        headers = {
            'CapitalStock': '总股本',
            'CapitalStockChange': '股本变动',
            'CapitalStockChangeEvent': '股本变动原因',
            'ClosePrice': '收盘价',
            'EndDate': '统计截止日期',
            'HolderAvgCapitalisation': '户均持仓市值',
            'HolderAvgStockQuantity': '户均持仓数量',
            'HolderNum': '股东数量',
            'HolderNumChange': '股东数量变动',
            'HolderNumChangeRate': '股东数量变动比例',
            'NoticeDate': '公告日期',
            'PreviousHolderNum': '上期股东数量',
            'RangeChangeRate': '区间涨跌幅',
            'TotalCapitalisation': '总市值'
        }
        data.rename(columns=headers, inplace=True)
    return data


def longhu_detail(date='', start_date='', end_date='', lang='en', beautify=True, **kwargs):
    info, data = longhu.detail(date, start_date, end_date, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])
    if beautify:
        data = data.replace('', np.nan).dropna(axis=1)
    if lang == 'zh':
        headers = {
            "SCode": "证券代码",
            "SName": "证券名称",
            "ClosePrice": "收盘价",
            "Chgradio": "涨跌幅",
            "Dchratio": "换手率",
            "JmMoney": "净买额",
            "Turnover": "市场总成交额",
            "Ctypedes": "上榜原因",
            "Smoney": "卖出额",
            "Tdate": "日期",
            "JmRate": "净买额占总成交比",
            "ZeRate": "成交额占总成交比",
            "Ltsz": "流通市值",
            "DP": "解读",
            "Rchange1m": "近1个月涨跌幅",
            "Rchange3m": "近3个月涨跌幅",
            "Rchange6m": "近6个月涨跌幅",
            "Rchange1y": "近1年涨跌幅",
            "BMoney": "买入额",
            "Bmoney": "买入额",
            "SumCount": "上榜次数",
            "JGBSumCount": "买方机构次数",
            "JGSSumCount": "卖方机构次数",
        }
        data.rename(columns=headers, inplace=True)
    return data


def longhu_stock_stats(date='', start_date='', end_date='', lang='en', beautify=True, **kwargs):
    info, data = longhu.stock_stats(date, start_date, end_date, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])
    if beautify:
        data = data.replace('', np.nan).dropna(axis=1)
    if lang == 'zh':
        headers = {
            "SCode": "证券代码",
            "SName": "证券名称",
            "ClosePrice": "收盘价",
            "Chgradio": "涨跌幅",
            "Dchratio": "换手率",
            "JmMoney": "净买额",
            "Turnover": "市场总成交额",
            "Ctypedes": "上榜原因",
            "Smoney": "卖出额",
            "Tdate": "日期",
            "JmRate": "净买额占总成交比",
            "ZeRate": "成交额占总成交比",
            "Ltsz": "流通市值",
            "DP": "解读",
            "Rchange1m": "近1个月涨跌幅",
            "Rchange3m": "近3个月涨跌幅",
            "Rchange6m": "近6个月涨跌幅",
            "Rchange1y": "近1年涨跌幅",
            "BMoney": "买入额",
            "Bmoney": "买入额",
            "SumCount": "上榜次数",
            "JGBSumCount": "买方机构次数",
            "JGSSumCount": "卖方机构次数",
        }
        data.rename(columns=headers, inplace=True)
    return data


def longhu_insti_stats(date='', start_date='', end_date='', lang='en', beautify=True, **kwargs):
    info, data = longhu.insti_stats(date, start_date, end_date, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])
    if beautify:
        data = data.replace('', np.nan).dropna(axis=1, how='all')
    if lang == 'zh':
        headers = {
            "SCode": "证券代码",
            "SName": "证券名称",
            "CPrice": "收盘价",
            "TurNover": "市场总成交额",
            "SMoney": "机构卖出总额",
            "BMoney": "机构买入额",
            "TDate": "日期",
            "RChange1M": "近1个月涨跌幅",
            "RChange3M": "近3个月涨跌幅",
            "RChange6M": "近6个月涨跌幅",
            "RChange1Y": "近1年涨跌幅",
            "TrunRate": "换手率",
            "CTypeDes": "上榜原因",
            "Chgradio": "涨跌幅",
            "AGSZBHXS": "流通市值",
            "SSL": "卖方机构数",
            "BSL": "买方机构数",
            "PBRate": "机构净买额占总成交比",
            "TurnRate": "换手率",
            "PBuy": "机构买入净额",
            }
        data.rename(columns=headers, inplace=True)
    return data


def active_business_dept(date='', start_date='', end_date='', lang='en', beautify=True, **kwargs):
    info, data = longhu.active_business_dept(date, start_date, end_date, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])

    def convert_SName(s):
        if s == '':
            return s
        else:
            s = ["[%s, %s]" % (x["SCode"], x["CodeName"]) for x in json.loads(s)]
            return ";".join(s)
    data['SName'] = data.SName.apply(convert_SName)

    if beautify:
        data = data.replace('', np.nan).dropna(axis=1, how='all')
    if lang == 'zh':
        headers = {
            "SName": "买入证券",
            "TDate": "上榜日期",
            "YybCode": "营业部代码",
            "YybName": "营业部名称",
            "Smoney": "卖出总金额",
            "Bmoney": "买入总金额",
            "JmMoney": "买入净额",
            "YybBCount": "买入个股数",
            "YybSCount": "卖出个股数"
            }
        data.rename(columns=headers, inplace=True)
    return data


def instit_chair_track(date='', start_date='', end_date='', lang='en', beautify=True, **kwargs):
    info, data = longhu.insti_chair_track(date, start_date, end_date, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])

    if beautify:
        data = data.replace('', np.nan).dropna(axis=1, how='all')
    if lang == 'zh':
        headers = {
            "SCode": "证券代码",
            "SName": "证券名称",
            "CPrice": "收盘价",
            "Chgradio": "涨跌幅",
            "TMoney": "龙虎榜成交金额",
            "RChange1M": "近1个月涨跌幅",
            "RChange3M": "近3个月涨跌幅",
            "RChange6M": "近6个月涨跌幅",
            "RChange1Y": "近1年涨跌幅",
            "UPCount": "上榜次数",
            "JGBMoney": "机构买入额",
            "JGBCount": "机构买入次数",
            "JGSMoney": "机构卖出额",
            "JGSCount": "机构卖出次数",
            "JGPBuy": "机构净买额",
            }
        data.rename(columns=headers, inplace=True)
    return data


def business_dept_stats(date='', start_date='', end_date='', lang='en', beautify=True, **kwargs):
    info, data = longhu.business_dept_stats(date, start_date, end_date, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])

    if beautify:
        data = data.replace('', np.nan).dropna(axis=1, how='all')
    if lang == 'zh':
        headers = {
            "SalesCode": "营业部代码",
            "SalesName": "营业部名称",
            "SumActBMoney": "买入额",
            "SumActSMoney": "卖出额",
            "SumActMoney": "龙虎榜成交金额",
            "BCount": "买入次数",
            "SCount": "卖出次数",
            "UpCount": "上榜次数",
            }
        data.rename(columns=headers, inplace=True)
    return data


def business_dept_ranking(date='', start_date='', end_date='', lang='en', beautify=True, **kwargs):
    info, data = longhu.business_dept_ranking(date, start_date, end_date, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])

    if beautify:
        data = data.replace('', np.nan).dropna(axis=1, how='all')
    if lang == 'zh':
        headers = {
            "AvgRate10DC": "上榜后10天平均涨幅",
            "AvgRate15DC": "上榜后15天平均涨幅",
            "AvgRate1DC": "上榜后1天平均涨幅",
            "AvgRate1M": "上榜后1月平均涨幅",
            "AvgRate1Y": "上榜后1年平均涨幅",
            "AvgRate20DC": "上榜后20天平均涨幅",
            "AvgRate2DC": "上榜后2天平均涨幅",
            "AvgRate30DC": "上榜后30天平均涨幅",
            "AvgRate3DC": "上榜后3天平均涨幅",
            "AvgRate3M": "上榜后3月平均涨幅",
            "AvgRate5DC": "上榜后5天平均涨幅",
            "AvgRate6M": "上榜后6月平均涨幅",
            "BCount10DC": "上榜后10天买入次数",
            "BCount15DC": "上榜后15天买入次数",
            "BCount1DC": "上榜后1天买入次数",
            "BCount1M": "上榜后1月买入次数",
            "BCount1Y": "上榜后1年买入次数",
            "BCount20DC": "上榜后20天买入次数",
            "BCount2DC": "上榜后2天买入次数",
            "BCount30DC": "上榜后30天买入次数",
            "BCount3DC": "上榜后3天买入次数",
            "BCount3M": "上榜后3月买入次数",
            "BCount5DC": "上榜后5天买入次数",
            "BCount6M": "上榜后6月买入次数",
            "UpRate10DC": "上榜后10天上涨概率",
            "UpRate15DC": "上榜后15天上涨概率",
            "UpRate1DC": "上榜后1天上涨概率",
            "UpRate1M": "上榜后1月上涨概率",
            "UpRate1Y": "上榜后1年上涨概率",
            "UpRate20DC": "上榜后20天上涨概率",
            "UpRate2DC": "上榜后2天上涨概率",
            "UpRate30DC": "上榜后30天上涨概率",
            "UpRate3DC": "上榜后3天上涨概率",
            "UpRate3M": "上榜后3月上涨概率",
            "UpRate5DC": "上榜后5天上涨概率",
            "UpRate6M": "上榜后6月上涨概率",
            "SalesCode": "营业部代码",
            "SalesName": "营业部名称",
            }
        data.rename(columns=headers, inplace=True)
    return data


def business_dept_detail(sale_code, date='', start_date='', end_date='', lang='en', beautify=True, **kwargs):
    info, data = longhu.business_dept_detail(sale_code, date, start_date, end_date, **kwargs)
    data = pd.DataFrame(data, columns=info['fields'])

    if beautify:
        data = data.replace('', np.nan).dropna(axis=1, how='all')
    if lang == 'zh':
        headers = {
            "ActBuyNum": "营业部买入额",
            "ActSellNum": "营业部卖出额",
            "CPrice": "收盘价",
            "CTypeDes": "上榜原因",
            "ChgRadio": "涨跌幅",
            "PBuy": "买卖净额",
            "RChange10DC": "上榜后10天涨跌幅",
            "RChange15DC": "上榜后10天涨跌幅",
            "RChange1DC": "上榜后10天涨跌幅",
            "RChange1M": "上榜后10天涨跌幅",
            "RChange1Y": "上榜后10天涨跌幅",
            "RChange20DC": "上榜后10天涨跌幅",
            "RChange2DC": "上榜后10天涨跌幅",
            "RChange30DC": "上榜后10天涨跌幅",
            "RChange3DC": "上榜后10天涨跌幅",
            "RChange3M": "上榜后10天涨跌幅",
            "RChange5DC": "上榜后10天涨跌幅",
            "RChange6M": "上榜后10天涨跌幅",
            "SCode": "证券代码",
            "SName": "证券名称",
            "TDate": "日期",
            "SalesCode": "营业部代码",
            "SalesName": "营业部名称",
            }
        data.rename(columns=headers, inplace=True)
    return data


def hist_margin_trade(code, lang='en', **kwargs):
    data = margintrade.hist_margin_trade(code, **kwargs)
    data = pd.DataFrame(data)
    func = lambda x: datetime.datetime.fromtimestamp(x / 1000).strftime("%Y-%m-%d")
    data['date'] = data.date.apply(func)

    if lang == 'zh':
        headers = {
            "date": "交易日期",
            "market": "市场类型",
            "rqchl": "偿还量",
            "rqchl10d": "10天偿还量",
            "rqchl3d": "3天偿还量",
            "rqchl5d": "5天偿还量",
            "rqjmg": "净卖出",
            "rqjmg10d": "10天净卖出",
            "rqjmg3d": "3天净卖出",
            "rqjmg5d": "5天净卖出",
            "rqmcl": "卖出量",
            "rqmcl10d": "10天卖出量",
            "rqmcl3d": "3天卖出量",
            "rqmcl5d": "5天卖出量",
            "rqye": "融券余额",
            "rqyl": "余量",
            "rzche": "偿还额",
            "rzche10d": "10天偿还额",
            "rzche3d": "3天偿还额",
            "rzche5d": "5天偿还额",
            "rzjme": "净买入",
            "rzjme10d": "10天净买入",
            "rzjme3d": "3天净买入",
            "rzjme5d": "5天净买入",
            "rzmre": "买入额",
            "rzmre10d": "10天买入额",
            "rzmre3d": "3天买入额",
            "rzmre5d": "5天买入额",
            "rzrqye": "融资融券余额",
            "rzrqyecz": "融资融券余额差值",
            "rzye": "融资余额",
            "rzyezb": "融资余额占流通市值比",
            "scode": "证券代码",
            "secname": "证券名称",
            "spj": "收盘价",
            "sz": "市值",
            "zdf": "涨跌幅",
        }
        data.rename(columns=headers, inplace=True)
    return data


def hgst_detail(code, date='', start_date='', end_date='', lang='en', beautify=True, **kwargs):
    data = hgst.detail(code, date, start_date, end_date, **kwargs)
    data = pd.DataFrame(data)

    if beautify:
        data = data.replace('', np.nan).dropna(axis=1, how='all')
    if lang == 'zh':
        headers = {
            "CLOSEPRICE": "收盘价",
            "HDDATE": "持股日期",
            "HKCODE": "港股代码",
            "MARKET": "市场类型",
            "PARTICIPANTCODE": "机构代码",
            "PARTICIPANTNAME": "机构名称",
            "SCODE": "证券代码",
            "SHAREHOLDPRICE": "持股市值",
            "SHAREHOLDPRICEFIVE": "持股市值5日变化",
            "SHAREHOLDPRICEONE": "持股市值1日变化",
            "SHAREHOLDPRICETEN": "持股市值10日变化",
            "SHAREHOLDSUM": "持股数量",
            "SNAME": "证券名称",
            "ShareHoldSumChg": "",
            "ZDF": "涨跌幅",
            "Zb": "持股占A股流通股比",
            "Zzb": "持股占总股本比",
            }
        data.rename(columns=headers, inplace=True)
    return data


def hgst_stats(code, lang='en', beautify=True, **kwargs):
    data = hgst.stats(code, **kwargs)
    data = pd.DataFrame(data)

    if beautify:
        data = data.replace('', np.nan).dropna(axis=1, how='all')
    if lang == 'zh':
        headers = {
            "CLOSEPRICE": "收盘价",
            "HDDATE": "持股日期",
            "HKCODE": "港股代码",
            "MARKET": "市场类型",
            "PARTICIPANTCODE": "机构代码",
            "PARTICIPANTNAME": "机构名称",
            "SCODE": "证券代码",
            "SHAREHOLDPRICE": "持股市值",
            "SHAREHOLDPRICEFIVE": "持股市值5日变化",
            "SHAREHOLDPRICEONE": "持股市值1日变化",
            "SHAREHOLDPRICETEN": "持股市值10日变化",
            "SHAREHOLDSUM": "持股数量",
            "SNAME": "证券名称",
            "ZDF": "涨跌幅",
            "Zb": "持股占A股流通股比",
            "Zzb": "持股占总股本比",
            }
        data.rename(columns=headers, inplace=True)
    return data





