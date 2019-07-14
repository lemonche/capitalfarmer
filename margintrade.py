from .network import *
import json


def hist_margin_trade(code, **kwargs):
    url = "http://api.dataide.eastmoney.com/data/get_rzrq_ggmx"

    params = {'code': code[:6],
              'orderby': kwargs.get('orderby', 'spj'),
              'order': kwargs.get('order', 'desc'),
              'pageindex': kwargs.get('pageindex', 1),
              'pagesize': kwargs.get('pagesize', 50),
              }

    try:
        h = html(url, params)
        data = json.loads(h.content)['data']
        return data
    except Exception as e:
        print(e)

