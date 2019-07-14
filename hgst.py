from .network import *
import json


def detail(code, date='', start_date='', end_date='', **kwargs):
    url = "http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get"

    params = {'type': 'HSGTHHDDET',
              'token': '70f12f2f4f091e459a279469fe49eca5',
              'p': kwargs.get('p', 1),
              'ps': kwargs.get('ps', 50),
              'filter': "(SCODE='%s')" % code[:6]}
    if date != '':
        params['filter'] += "(HDDATE='%s')" % date
    else:
        params['filter'] += "(HDDATE>='%s' and HDDATE<='%s')" % (start_date, end_date)

    try:
        h = html(url, params)
        data = json.loads(h.content)
        return data
    except Exception as e:
        print(e)


def stats(code, **kwargs):
    url = "http://dcfm.eastmoney.com//em_mutisvcexpandinterface/api/js/get"

    params = {'type': 'HSGTHDSTA',
              'token': '70f12f2f4f091e459a279469fe49eca5',
              'p': kwargs.get('p', 1),
              'ps': kwargs.get('ps', 50),
              'st': kwargs.get('st', 'HDDATE'),
              'sr': kwargs.get('sr', -1),
              'filter': "(SCODE='%s')" % code[:6]}

    try:
        h = html(url, params)
        data = json.loads(h.content)
        return data
    except Exception as e:
        print(e)
