from .network import *
import json


def moneyflow(code, **kwargs):
    """
    当日资金流向
    """
    url = 'http://ff.eastmoney.com/EM_CapitalFlowInterface/api/js'
    params = {'id': params_converter.symbol_code_2(code),
              'type': 'ff',
              'rtntype': kwargs.get('rtntype', 2),
              'acces_token': '1942f5da9b46b069953c873404aad4b5',
              }
    fields = ['time', 'inflow', 'outflow', 'net_inflow', 'super_infow', 'super_outflow',
              'super_net_inflow', 'large_inflow', 'large_outflow', 'large_net_inflow',
              'mid_inflow', 'mid_outflow', 'mid_net_inflow', 'small_inflow',
              'small_outflow', 'small_net_inflow', 'col1']
    h = html(url=url, params=params)
    try:
        data = [x.split(",") for x in json.loads(h.content[1:-1])]
        return fields, data
    except Exception as e:
        print(e)
        return h


def hist_moneyflow(code, **kwargs):
    """
    历史资金流向，只能获取最近100个交易日的数据
    """
    url = 'http://ff.eastmoney.com/EM_CapitalFlowInterface/api/js'
    params = {'id': params_converter.symbol_code_2(code),
              'type': 'hff',
              'rtntype': kwargs.get('rtntype', 2),
              'acces_token': '1942f5da9b46b069953c873404aad4b5',
              }
    fields = ['date', 'inflow', 'outflow', 'net_inflow', 'net_infow_percentage',
              'super_inflow', 'super_outflow', 'super_net_inflow', 'super_net_infow_percentage',
              'large_inflow', 'large_outflow', 'large_net_inflow', 'large_net_infow_percentage',
              'mid_inflow', 'mid_outflow', 'mid_net_inflow', 'mid_net_infow_percentage',
              'small_inflow', 'small_outflow', 'small_net_inflow', 'small_net_infow_percentage',
              'close', 'up_down_percentage', 'col1']
    h = html(url=url, params=params)
    try:
        data = [x.split(",") for x in json.loads(h.content[1:-1])]
        return fields, data
    except Exception as e:
        print(e)
        return h


def insti_position(code, date, insti_type='', **kwargs):
    """
    机构持仓仓位
    :param date: 报告期, 2019-03-31
    :param insti_type: 机构类型
            空值：所有机构；
            1：基金；
            2：QFII；
            3：社保；
            5：保险；
            4：券商；
            6：信托
    :param SHCode: 指定投资产品代码，查看持有该股状况
    :return:
    """
    url = "http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/ZLCCMX/GetZLCCMX"
    params = {"tkn": "eastmoney",
              "cfg": "ZLCCMX",
              "SHType": insti_type,
              "SCode": code,
              "ReportDate": date,
              "pageNum": kwargs.get('page', ''),  # 空值表示不分页
              "pageSize": kwargs.get('pagesize', ''),
              "sortField": kwargs.get("sortField", 'ShareHDNum'),
              "sortDirec": kwargs.get("sortDirec", 1),
              "SHCode": kwargs.get("SHCode", '')
              }
    h = html(url, params)
    try:
        info = json.loads(h.content)['Data'][0]
        info['fields'] = info["FieldName"].split(",")
        data = [x.split(info['SplitSymbol']) for x in info.pop("Data")]
        return info, data
    except Exception as e:
        print(e)
        return h


def biggest_stock_holder(code, date, type='Lt'):
    """
    前十大流通股东、前十大股东
    :param date: 报告期
    :param type: Lt：十大流通股东；Sd：十大股东
    :return:
    """
    url = "http://data.eastmoney.com/DataCenter_V3/gdfx/stockholder.ashx"
    params = {'type': type,
              'code': code[:6],
              'date': date,
              }
    h = html(url, params)
    try:
        data = json.loads(h.content.decode(encoding='gbk'))['data']
        return data
    except Exception as e:
        print(e)
        return h


def stock_holder_number(code, **kwargs):
    """
    股东户数
    """
    url = "http://data.eastmoney.com/DataCenter_V3/gdhs/GetDetial.ashx"
    params = {'page': kwargs.get('page', ''),
              'pagesize': kwargs.get('pagesize', ''),
              'code': code[:6],
              }
    h = html(url, params)
    try:
        data = json.loads(h.content.decode(encoding='gbk'))['data']
        return data
    except Exception as e:
        print(e)
        return h



































