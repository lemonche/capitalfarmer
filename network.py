import requests


def html(url, params=None):
    try:
        r = requests.get(url, params=params)
        if r.status_code != 200:
            print("network error[{}]: couldn't get url [{}]".format(r.status_code, r.url))
            return None
        return r
    except Exception as e:
        print(e)
        print(url)
        return None


class params_converter:

    @staticmethod
    def symbol_code_1(code):
        # 600000.SH ==> 1.600000
        if code[-3:] == ".SH":
            code = "{}.{}".format(1, code[:6])
        elif code[-3:] == ".SZ":
            code = "{}.{}".format(0, code[:6])
        return code

    @staticmethod
    def symbol_code_2(code):
        # 600000.SH ==> 6000001
        if code[-3:] == ".SH":
            code = code[:6] + '1'
        elif code[-3:] == ".SZ":
            code = code[:6] + '0'
        return code


