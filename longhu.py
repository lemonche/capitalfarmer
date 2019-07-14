from .network import *
import json


def detail(date='', start_date='', end_date='', **kwargs):
    """
    指定日期区间内的龙虎榜数据
    :param market: 0:全部，1：沪市；2：深市
    """

    if date != '':
        start_date = date
        end_date = date

    params = {'tkn': 'eastmoney',
              'cfg': 'lhbggdrtj',
              'mkt': kwargs.get('market', 0),
              'startDateTime': start_date,
              'endDateTime': end_date,
              'dateNum': kwargs.get('dateNum', ''),
              'sortRule': kwargs.get('sortdirection', 1),
              'sortColumn': kwargs.get('sortcolumn', "Tdate"),
              'pageNum': kwargs.get('page', ''),
              'pageSize': kwargs.get('pagesize', ''),
              }
    url = "http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/LHBGGDRTJ/GetLHBGGDRTJ"

    try:
        h = html(url, params=params)
        info = json.loads(h.content)['Data'][0]
        info['fields'] = info['FieldName'].split(',')
        data = [x.split(info['SplitSymbol']) for x in info.pop('Data')]
        return info, data
    except Exception as e:
        print(e)


def stock_stats(date='', start_date='', end_date='', **kwargs):
    """
    指定日期区间内的龙虎榜上个股统计
    :param market: 0:全部，1：沪市；2：深市
    """

    if date != '':
        start_date = date
        end_date = date

    params = {'tkn': 'eastmoney',
              'mkt': kwargs.get('market', 0),
              'startDateTime': start_date,
              'endDateTime': end_date,
              'cfg': 'lhbxqsum',
              'dateNum': kwargs.get('dateNum', ''),
              'sortRule': kwargs.get('sortdirection', 1),
              'sortColumn': kwargs.get('sortcolumn', "Tdate"),
              'pageNum': kwargs.get('page', ''),
              'pageSize': kwargs.get('pagesize', ''),
              }
    url = "http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/LHBXQSUM/GetLHBXQSUM"

    try:
        h = html(url, params=params)
        info = json.loads(h.content)['Data'][0]
        info['fields'] = info['FieldName'].split(',')
        data = [x.split(info['SplitSymbol']) for x in info.pop('Data')]
        return info, data
    except Exception as e:
        print(e)


def insti_stats(date='', start_date='', end_date='', **kwargs):
    """
    龙虎榜，机构统计
    :param market: 0:全部，1：沪市；2：深市
    """

    if date != '':
        start_date = date
        end_date = date

    params = {'tkn': 'eastmoney',
              'mkt': kwargs.get('market', 0),
              'startDateTime': start_date,
              'endDateTime': end_date,
              'cfg': 'lhbjgtj',
              'dateNum': kwargs.get('dateNum', ''),
              'code': '',
              'pageNum': kwargs.get('page', ''),
              'pageSize': kwargs.get('pagesize', ''),
              'sortdirec': kwargs.get('sortdirection', 1),
              'sortfield': kwargs.get('sortcolumn', 'PBuy'),
              }
    url = "http://datainterface3.eastmoney.com/EM_DataCenter_V3/api/LHBJGTJ/GetHBJGTJ"

    try:
        h = html(url, params=params)
        info = json.loads(h.content)['Data'][0]
        info['fields'] = info['FieldName'].split(',')
        data = [x.split(info['SplitSymbol']) for x in info.pop('Data')]
        return info, data
    except Exception as e:
        print(e)


def active_business_dept(date='', start_date='', end_date='', **kwargs):
    """
    活跃营业部
    :param market: 0:全部，1：沪市；2：深市
    :return:
    """

    if date != '':
        start_date = date
        end_date = date

    params = {'tkn': 'eastmoney',
              'mkt': kwargs.get('market', 0),
              'startDateTime': start_date,
              'endDateTime': end_date,
              'cfg': 'lhbyybsbcs',
              'dateNum': kwargs.get('dateNum', ''),
              'sortRule': kwargs.get('sortdirection', 1),
              'sortColumn': kwargs.get('sortcolumn', 'JmMoney'),
              'pageNum': kwargs.get('page', ''),
              'pageSize': kwargs.get('pagesize', ''),
              }
    url = "http://datainterface3.eastmoney.com//EM_DataCenter_V3/api/LHBYYBSBCS/GetLHBYYBSBCS"

    try:
        h = html(url, params=params)
        info = json.loads(h.content)['Data'][0]
        info['fields'] = info['FieldName'].split(',')
        data = [x.split(info['SplitSymbol']) for x in info.pop('Data')]
        return info, data
    except Exception as e:
        print(e)


def insti_chair_track(date='', start_date='', end_date='', **kwargs):
    """
    机构席位追踪
    :param market: 0:全部，1：沪市；2：深市
    """

    if date != '':
        start_date = date
        end_date = date

    params = {'tkn': 'eastmoney',
              'mkt': kwargs.get('market', 0),
              'startDateTime': start_date,
              'endDateTime': end_date,
              'cfg': 'lhbjgxwzz',
              'code': '',
              'dateNum': kwargs.get('dateNum', ''),
              'sortdirec': kwargs.get('sortdirection', 1),
              'sortfield': kwargs.get('sortcolumn', 'PBuy'),
              'pageNum': kwargs.get('page', ''),
              'pageSize': kwargs.get('pagesize', ''),
              }
    url = "http://datainterface3.eastmoney.com//EM_DataCenter_V3/api/LHBJGXWZZ/GetLHBJGXWZZ"

    try:
        h = html(url, params=params)
        info = json.loads(h.content)['Data'][0]
        info['fields'] = info['FieldName'].split(',')
        data = [x.split(info['SplitSymbol']) for x in info.pop('Data')]
        return info, data
    except Exception as e:
        print(e)


def business_dept_stats(date='', start_date='', end_date='', **kwargs):
    """
    营业部统计
    """

    if date != '':
        start_date = date
        end_date = date

    params = {'tkn': 'eastmoney',
              'startDateTime': start_date,
              'endDateTime': end_date,
              'cfg': 'yybmmtj',
              'salesCode': kwargs.get('salesCode', ''),
              'dayNum': kwargs.get('dateNum', ''),
              'sortdirec': kwargs.get('sortdirection', 1),
              'sortfield': kwargs.get('sortcolumn', 'PBuy'),
              'pageNum': kwargs.get('page', ''),
              'pageSize': kwargs.get('pagesize', ''),
              }
    url = "http://datainterface3.eastmoney.com//EM_DataCenter_V3/api/LHBYYBMMTJ/GetLHBYYBMMTJ"

    try:
        h = html(url, params=params)
        info = json.loads(h.content)['Data'][0]
        info['fields'] = info['FieldName'].split(',')
        data = [x.split(info['SplitSymbol']) for x in info.pop('Data')]
        return info, data
    except Exception as e:
        print(e)


def business_dept_ranking(date='', start_date='', end_date='', **kwargs):
    """
    营业部统计
    """

    if date != '':
        start_date = date
        end_date = date

    params = {'tkn': 'eastmoney',
              'startDateTime': start_date,
              'endDateTime': end_date,
              'cfg': 'yybph',

              'salesCode': kwargs.get('salesCode', ''),
              'monthNum': kwargs.get('dateNum', ''),
              'sortdirec': kwargs.get('sortdirection', 1),
              'sortfield': kwargs.get('sortcolumn', ''),
              'pageNum': kwargs.get('page', 1),
              'pageSize': kwargs.get('pagesize', 500),
              }
    url = "http://datainterface3.eastmoney.com//EM_DataCenter_V3/api/LHBYYBPH/GetLHBYYBPH"

    try:
        h = html(url, params=params)
        info = json.loads(h.content)['Data'][0]
        info['fields'] = info['FieldName'].split(',')
        data = [x.split(info['SplitSymbol']) for x in info.pop('Data')]
        return info, data
    except Exception as e:
        print(e)


def business_dept_detail(salesCode, date='', start_date='', end_date='', **kwargs):
    """
        营业部交易明细
        """
    if date != '':
        start_date = date
        end_date = date

    params = {'tkn': 'eastmoney',
              'startDateTime': start_date,
              'endDateTime': end_date,
              'cfg': 'yybjymx',
              'salesCode': salesCode,

              'dayNum': kwargs.get('dateNum', ''),
              'tdir': kwargs.get('tdir', ''),
              'sortdirec': kwargs.get('sortdirection', 1),
              'sortfield': kwargs.get('sortcolumn', ''),
              'pageNum': kwargs.get('page', 1),
              'pageSize': kwargs.get('pagesize', 500)
              }
    url = "http://datainterface3.eastmoney.com//EM_DataCenter_V3/api/YYBJXMX/GetYYBJXMX"

    try:
        h = html(url, params=params)
        info = json.loads(h.content)['Data'][0]
        info['fields'] = info['FieldName'].split(',')
        data = [x.split(info['SplitSymbol']) for x in info.pop('Data')]
        return info, data
    except Exception as e:
        print(e)



















