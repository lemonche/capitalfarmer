from .network import *
import json


def time_sharing_trans_3s(code, pos=-10):
    """
    3秒分时成交
    :param code:
    :param pos:
    :return:
    """
    url = 'http://push2.eastmoney.com/api/qt/stock/details/get'
    params = {'secid': params_converter.symbol_code_1(code),
              'pos': pos,
              'fields1': 'f1,f2,f3,f4',
              'fields2': 'f51,f52,f53,f54,f55',
              }
    fields = ['time', 'price', 'hands', 'col1', 'color']
    h = html(url=url, params=params)
    if h is not None:
        try:
            data = json.loads(h.content)['data']
            data['fields'] = fields
            details = [x.split(',') for x in data.pop('details')]
            return data, details
        except Exception as e:
            print(e)
            return


def recent_minutely(code, ndays=1):
    """
    最近1、2、3、4、5天内的1分钟行行情
    :param code:
    :param ndays:
    :return:
    """
    url = 'http://push2his.eastmoney.com/api/qt/stock/trends2/get'
    params = {'secid': params_converter.symbol_code_1(code),
              'fields1': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11',
              'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58',
              'ndays': ndays,
              }
    fields = ['datetime', 'open', 'close', 'high', 'low', 'hands', 'amount', 'avgprice']
    h = html(url=url, params=params)
    if h is not None:
        try:
            data = json.loads(h.content)['data']
            data['fields'] = fields
            trends = [x.split(",") for x in data.pop('trends')]
            return data, trends
        except Exception as e:
            print(e)
            return h


def recent_minutely_new(code, quota_type='r', fuquan='', **kwargs):
    """
    最近1、2、3、4、5天的1分钟交易行情
    :param code:
    :param quota_type: r：最近一个交易日的1分钟行情
            t2、t3、t4、t5：最近2、3、4、5个交易日的1分钟行情
    :param fuquan:复权
            空值：不复权；fa：前复权；ba：后复权
    :param iscr:是否获取开盘前15分钟内的行情
    :return:
    """
    url = 'http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js'
    params = {'id': params_converter.symbol_code_2(code),
              'quota_type': quota_type,
              'authorityType': fuquan,
              'rtntype': kwargs.get('rtntype', 5),
              'iscr': kwargs.get('iscr', 'false'),
              }
    fields = ['datetime', 'close', 'hands', 'avgprice', 'col1']
    h = html(url=url, params=params)
    if h is not None:
        try:
            data = json.loads(h.content[1:-1])
            info = data['info']
            info['name'] = data['name']
            info['code'] = data['code']
            info['fields'] = fields
            quotation = [x.split(",") for x in data['data']]
            return info, quotation
        except Exception as e:
            print(e)
            return h


def quota_minutely(code, fuquan='', **kwargs):
    """
    获取最近1个交易日内的1分钟行情
    :param code:
    :param fuquan: 复权
            空值：不复权；fa：前复权；ba：后复权
    :param iscr: 是否获取开盘前15分钟内的行情
    :return:
    """
    url = 'http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js'
    params = {'id': params_converter.symbol_code_2(code),
              'type': 'm1',
              'authorityType': fuquan,
              'rtntype': kwargs.get('rtntype', 5),
              'iscr': kwargs.get('iscr', 'false'),
              }
    fields = ['datetime', 'open', 'high', 'low', 'close', 'avgprice', 'volume', 'amount', 'col1']
    h = html(url=url, params=params)
    if h is not None:
        try:
            data = [x.split(",") for x in h.content[1:-1].decode(encoding='utf-8').split("\r\n")]
            return fields, data
        except Exception as e:
            print(e)
            return h


def quota(code, quota_type='k', fuquan='', **kwargs):
    """
    行情数据
    :param code:
    :param quota_type: 行情数据类型
            m5k、m15k、m30k、m60k：最近30个交易日的5分钟、15分钟、30分钟、60分钟行情
            k、wk、mk：日线、周线、月线行情
    :param fuquan: 复权
            空值：不复权；fa：前复权；ba：后复权
    :param iscr: 是否获取开盘前15分钟内的行情
    :return:
    """
    url = 'http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js'
    params = {'id': params_converter.symbol_code_2(code),
              'type': quota_type,
              'authorityType': fuquan,
              'rtntype': kwargs.get('rtntype', 5),
              'iscr': kwargs.get('iscr', 'false'),
              }
    fields = ['datetime', 'open', 'close', 'high', 'low', 'volume', 'amount', 'zhenfu', 'clo1']
    h = html(url=url, params=params)
    if h is not None:
        try:
            data = json.loads(h.content[1:-1])
            info = data['info']
            info['name'] = data['name']
            info['code'] = data['code']
            info['fields'] = fields
            quotation = [x.split(",") for x in data['data']]
            return info, quotation
        except Exception as e:
            print(e)
            return h


def time_sharing_trans(code, **kwargs):
    """
    分时成交
    :param code:
    :param gtvolume: 大单筛选
            空值：全部，100、200、500、1000、2000、5000、10000：大于100、200、500、1000、2000、5000、10000手
    :param sort:
    :return:
    """
    url = 'http://mdfm.eastmoney.com/EM_UBG_MinuteApi/Js/Get'
    params = {'id': params_converter.symbol_code_2(code),
              'dtype': 'all',
              'gtvolume': kwargs.get("gtvolume", ""),
              'sort': kwargs.get("sort", 'asc'),
              'page': kwargs.get("page", 0),
              }
    fields = ['time', 'price', 'hands', 'color', 'direction', 'col1', 'col2', 'col3']
    page = 1
    tst = []
    while True:
        params['page'] = page
        h = html(url=url, params=params)
        if h is not None:
            try:
                data = json.loads(h.content[1:-1])['value']['data']
                if len(data) == 0:
                    tst = [x.split(",") for x in tst]
                    return fields, tst
                tst += data
            except Exception as e:
                print(e)
                return h
        page += 1

