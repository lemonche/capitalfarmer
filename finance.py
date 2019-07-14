from .network import *
import json
import pandas as pd
import numpy as np


_zcfzb_headers = {"ACCOUNTPAY": "应付账款",
            "ACCOUNTPAY_YOY": "应付账款增长率",
            "ACCOUNTREC": "应收账款",
            "ACCOUNTREC_YOY": "应收账款增长率",
            "ADVANCEPAY": "预付款项",
            "ADVANCEPAY_YOY": "预付款项增长率",
            "ADVANCERECEIVE": "预收款项",
            "ADVANCERECEIVE_YOY": "预付款项增长率",
            "BILLPAY": "应付票据",
            "BILLPAY_YOY": "应付票据增长率",
            "BILLREC": "应收票据",
            "BILLREC_YOY": "应收票据增长率",
            "CAPITALRESERVE": "资本公积",
            "CAPITALRESERVE_YOY": "资本公积增长率",
            "CONSTRUCTIONPROGRESS": "在建工程",
            "CONSTRUCTIONPROGRESS_YOY": "在建工程增长率",
            "DEFERINCOME": "递延收益",
            "DEFERINCOMETAXASSET": "递延所得税资产",
            "DEFERINCOMETAXASSET_YOY": "递延所得税资产增长率",
            "DEFERINCOMETAXLIAB": "递延所得税负债",
            "DEFERINCOMETAXLIAB_YOY": "递延所得税负债增长率",
            "ESTATEINVEST": "投资性房地产",
            "ESTATEINVEST_YOY": "投资性房地产增长率",
            "FIXEDASSET": "固定资产",
            "FIXEDASSET_YOY": "固定资产增长率",
            "GOODWILL": "商誉",
            "GOODWILL_YOY": "商誉增长率",
            "INTANGIBLEASSET": "无形资产",
            "INTANGIBLEASSET_YOY": "无形资产增长率",
            "INTERESTPAY": "应付利息",
            "INTERESTPAY_YOY": "应付利息增长率",
            "INTERESTREC": "应收利息",
            "INVENTORY": "存货",
            "INVENTORY_YOY": "存货增长率",
            "LTACCOUNTPAY": "长期应付款",
            "LTACCOUNTPAY_YOY": "长期应付款增长率",
            "LTBORROW": "长期借款",
            "LTBORROW_YOY": "长期借款增长率",
            "LTDEFERASSET": "长期待摊费用",
            "LTDEFERASSET_YOY": "长期待摊费用增长率",
            "LTEQUITYINV": "长期股权投资",
            "LTEQUITYINV_YOY": "长期股权投资增长率",
            "MINORITYEQUITY": "少数股东权益",
            "MINORITYEQUITY_YOY": "少数股东权益增长率",
            "MONETARYFUND": "货币资金",
            "MONETARYFUND_YOY": "货币资金增长率",
            "NONLLIABONEYEAR": "一年内到期的非流动负债",
            "NONLLIABONEYEAR_YOY": "一年内到期的非流动负债增长率",
            "OTHERLASSET": "其他流动资产",
            "OTHERLASSET_YOY": "其他流动资产增长率",
            "OTHERLLIAB": "其他流动负债",
            "OTHERLLIAB_YOY": "其他流动负债增长率",
            "OTHERNONLASSET": "其他非流动资产",
            "OTHERNONLASSET_YOY": "其他非流动资产增长率",
            "OTHERPAY": "其他应付款",
            "OTHERPAY_YOY": "其他应付款增长率",
            "OTHERREC": "其他应收款",
            "OTHERREC_YOY": "其他应收款增长率",
            "RETAINEDEARNING": "未分配利润",
            "RETAINEDEARNING_YOY": "未分配利润增长率",
            "SALARYPAY": "应付职工薪酬",
            "SALARYPAY_YOY": "应付职工薪酬增长率",
            "SALEABLEFASSET": "可供出售金融资产",
            "SALEABLEFASSET_YOY": "可供出售金融资产增长率",
            "SECURITYCODE": "证券代码",
            "SHARECAPITAL": "实收资本（或股本）",
            "SHARECAPITAL_YOY": "实收资本（或股本）增长率",
            "SPECIALRESERVE": "专项储备",
            "SPECIALRESERVE_YOY": "专项储备增长率",
            "STBORROW": "短期借款",
            "STBORROW_YOY": "短期借款增长率",
            "SUMASSET": "资产总计",
            "SUMASSET_YOY": "资产总计增长率",
            "SUMLASSET": "流动资产合计",
            "SUMLASSET_YOY": "流动资产合计增长率",
            "SUMLIAB": "负债合计",
            "SUMLIAB_YOY": "负债合计增长率",
            "SUMLIABSHEQUITY": "负债和股东权益合计",
            "SUMLIABSHEQUITY_YOY": "负债和股东权益合计增长率",
            "SUMLLIAB": "流动负债合计",
            "SUMLLIAB_YOY": "流动负债合计增长率",
            "SUMNONLASSET": "非流动资产合计",
            "SUMNONLASSET_YOY": "非流动资产合计增长率",
            "SUMNONLLIAB": "非流动负债合计",
            "SUMNONLLIAB_YOY": "非流动负债合计增长率",
            "SUMPARENTEQUITY": "归属于母公司股东权益合计",
            "SUMPARENTEQUITY_YOY": "归属于母公司股东权益合计增长率",
            "SUMSHEQUITY": "股东权益合计",
            "SUMSHEQUITY_YOY": "股东权益合计增长率",
            "SURPLUSRESERVE": "盈余公积",
            "SURPLUSRESERVE_YOY": "盈余公积增长率",
            "TAXPAY": "应交税费",
            "TAXPAY_YOY": "应交税费增长率",
            "REPORTTYPE": "报告类型",
            "DEFERINCOME_YOY": "递延收益增长率",
            "CURRENCY": "计量货币",
            "LENDFUND": "拆出资金",
            "LENDFUND_YOY": "拆出资金增长率",
            "BORROWFUND": "拆入资金",
            "BORROWFUND_YOY": "拆入资金增长率",
            "LIQUIDATEFIXEDASSET": "发放贷款及垫款",
            "LIQUIDATEFIXEDASSET_YOY": "发放贷款及垫款增长率",
            "BUYSELLBACKFASSET": "买入返售金融资产",
            "BUYSELLBACKFASSET_YOY": "买入返售金融资产增长率",
            "SELLBUYBACKFASSET": "卖出回购金融资产款",
            "SELLBUYBACKFASSET_YOY": "卖出回购金融资产款增长率",
            "OTHEREQUITY": "其他权益工具",
            "OTHEREQUITY_YOY": "其他权益工具增长率",
            "PREFERREDSTOCK": "其中:优先股",
            "PREFERREDSTOCK_YOY": "其中:优先股增长率",
            "BORROWFROMCBANK": "向中央银行借款",
            "BORROWFROMCBANK_YOY": "向中央银行借款增长率",
            "GENERALRISKPREPARE": "一般风险准备",
            "GENERALRISKPREPARE_YOY": "一般风险准备增长率",
            "BONDPAY": "应付债券",
            "BONDPAY_YOY": "应付债券增长率",
            "ANTICIPATELIAB": "预计负债",
            "ANTICIPATELIAB_YOY": "预计负债增长率",
            "DIVIDENDPAY": "应付股利",
            "DIVIDENDPAY_YOY": "应付股利增长率",
            "REPORTDATE": "报告期",
            }


class Report:

    def __init__(self):
        self.headers = None
        self.content = None

    def indicator(self, indicator_name):
        indicator_name = self.headers.get(indicator_name, indicator_name)
        r = [{indicator_name: b.get(indicator_name), 'REPORTDATE': b.get('REPORTDATE')} for b in self.content]
        return r

    def indicators(self, *indicator_names):
        indicator_names = [self.headers.get(idt, idt) for idt in indicator_names] + ['REPORTDATE']
        r = []
        for b in self.content:
            rp = {}
            for idt in indicator_names:
                rp[idt] = b.get(idt)
            r.append(rp)
        return r

    def to_dataframe(self, language='en', beautrify=False, report_type='absolute'):
        r = pd.DataFrame(self.content)

        if beautrify:
            # indicator全部为空值的列
            r = r.replace('', np.nan).dropna(axis=1)

        # 绝对值、百分比报表
        if report_type == 'absolute':
            r = r[list(filter(lambda x: "YOY" not in x, r.columns))]
        elif report_type == 'percentage':
            r = r[["REPORTDATE", "CURRENCY","REPORTTYPE"] + list(filter(lambda x: "YOY" in x, r.columns))]

        if language == 'zh':
            r.rename(columns=self.headers, inplace=True)

        return r

    def report(self):
        return


class zcfzb(Report):

    url = 'http://f10.eastmoney.com/NewFinanceAnalysis/zcfzbAjax'

    def __init__(self, code, companyType=4, reportDateType=0, reportType=2, endDate=''):
        """
        资产负债表
        :param code:
        :param companyType:
        :param reportDateType: 0：按报告期；1：按年度
        :param reportType:
        :param endDate: 2015/9/30 0:00:00，获取endDate前5个报告期的数据，默认为空值，表示当前时间前5个报告期数据
        :return:
        """
        super().__init__()

        params = {'companyType': companyType,
                'code': code,
                'reportDateType': reportDateType,
                'reportType': reportType,
                'endDate': endDate}
        h = html(url=self.url, params=params)
        if h is not None:
            try:
                self.content = eval(json.loads(h.content))
            except Exception as e:
                print(e)
                return

        headers = self.content[0].copy()
        for k, v in headers.items():
            headers[k] = _zcfzb_headers.get(k, k)
        self.headers = headers


_lrb_headers = {
    "ASSETDEVALUELOSS":"资产减值损失",
    "BASICEPS":"基本每股收益",
    "COMMEXP":"手续费及佣金支出",
    "COMMREVE":"其中:手续费及佣金收入",
    "CURRENCY":"计量货币",
    "DILUTEDEPS":"稀释每股收益",
    "EXCHANGEINCOME":"汇兑收益",
    "FINANCEEXP":"财务费用",
    "FVALUEINCOME":"公允价值变动收益",
    "INCOMETAX":"减:所得税费用",
    "INTEXP":"利息支出",
    "INTREVE":"其中:利息收入",
    "INVESTINCOME":"加:投资收益",
    "INVESTJOINTINCOME":"其中:对联营企业和合营企业的投资收益",
    "KCFJCXSYJLR":"资产减值损失",
    "MANAGEEXP":"管理费用",
    "MINORITYCINCOME":"归属于少数股东的综合收益总额",
    "MINORITYINCOME":"少数股东损益",
    "MINORITYOTHERCINCOME":"归属于少数股东的其他综合收益",
    "NETPROFIT":"综合收益总额",
    "NONOPERATEEXP":"减:营业外支出",
    "NONOPERATEREVE":"加:营业外收入",
    "OPERATEEXP":"营业成本",
    "OPERATEPROFIT":"营业利润",
    "OPERATEREVE":"营业收入",
    "OPERATETAX":"营业税金及附加",
    "OTHERCINCOME":"其他综合收益",
    "OTHEREXP":"其他业务成本",
    "OTHERREVE":"其他业务收入",
    "PARENTCINCOME":"归属于母公司所有者的综合收益总额",
    "PARENTNETPROFIT":"其中:归属于母公司股东的净利润",
    "PARENTOTHERCINCOME":"归属于母公司股东的其他综合收益",
    "REPORTDATE":"报告期",
    "REPORTTYPE":"报告类型",
    "SALEEXP":"销售费用",
    "SECURITYCODE":"证券代码",
    "SUMCINCOME":"净利润",
    "SUMPROFIT":"营业利润",
    "TOTALOPERATEEXP":"营业总成本",
    "TOTALOPERATEREVE":"营业总收入",
}


class lrb(Report):

    url = 'http://f10.eastmoney.com/NewFinanceAnalysis/lrbAjax'

    def __init__(self, code, companyType=4, reportDateType=0, reportType=2, endDate=''):
        """
        资产负债表
        :param code:
        :param companyType:
        :param reportDateType: 0：按报告期；1：按年度
        :param reportType:
        :param endDate: 2015/9/30 0:00:00，获取endDate前5个报告期的数据，默认为空值，表示当前时间前5个报告期数据
        :return:
        """
        super().__init__()

        params = {'companyType': companyType,
                'code': code,
                'reportDateType': reportDateType,
                'reportType': reportType,
                'endDate': endDate}
        h = html(url=self.url, params=params)
        if h is not None:
            try:
                self.content = eval(json.loads(h.content))
            except Exception as e:
                print(e)
                return

        headers = self.content[0].copy()
        for k, v in headers.items():
            headers[k] = _lrb_headers.get(k, k)
        self.headers = headers


_xjllb_headers = {
    "BUYFILASSETPAY":"购建固定资产、无形资产和其他长期资产支付的现金",
    "BUYGOODSSERVICEPAY":"购买商品、接受劳务支付的现金",
    "CASHEQUIBEGINNING":"加:期初现金及现金等价物余额",
    "CASHEQUIENDING":"期末现金及现金等价物余额",
    "CURRENCY":"计量货币",
    "DISPOSALINVREC":"收回投资收到的现金",
    "EMPLOYEEPAY":"支付给职工以及为职工支付的现金",
    "INVINCOMEREC":"取得投资收益收到的现金",
    "INVPAY":"投资支付的现金",
    "NETFINACASHFLOW":"筹资活动产生的现金流量净额",
    "NETINVCASHFLOW":"投资活动产生的现金流量净额",
    "NETOPERATECASHFLOW":"经营活动产生的现金流量净额",
    "NICASHEQUI":"现金及现金等价物净增加额",
    "OTHEROPERATEPAY":"支付其他与经营活动有关的现金",
    "OTHEROPERATEREC":"收到其他与经营活动有关的现金",
    "REPORTDATE":"报告期",
    "REPORTDATETYPE":"报告期类型",
    "REPORTTYPE":"报告类型",
    "SALEGOODSSERVICEREC":"销售商品、提供劳务收到的现金",
    "SECURITYCODE":"证券代码",
    "SUMFINAFLOWOUT":"筹资活动现金流出小计",
    "SUMINVFLOWIN":"投资活动现金流入小计",
    "SUMINVFLOWOUT":"投资活动现金流出小计",
    "SUMOPERATEFLOWIN":"经营活动现金流入小计",
    "SUMOPERATEFLOWOUT":"经营活动现金流出小计",
    "TAXPAY":"支付的各项税费",
}


class xjllb(Report):

    url = 'http://f10.eastmoney.com/NewFinanceAnalysis/xjllbAjax'

    def __init__(self, code, companyType=4, reportDateType=0, reportType=2, endDate=''):
        """
        资产负债表
        :param code:
        :param companyType:
        :param reportDateType: 0：按报告期；1：按年度
        :param reportType:
        :param endDate: 2015/9/30 0:00:00，获取endDate前5个报告期的数据，默认为空值，表示当前时间前5个报告期数据
        :return:
        """
        super().__init__()

        params = {'companyType': companyType,
                'code': code,
                'reportDateType': reportDateType,
                'reportType': reportType,
                'endDate': endDate}
        h = html(url=self.url, params=params)
        if h is not None:
            try:
                self.content = eval(json.loads(h.content))
            except Exception as e:
                print(e)
                return

        headers = self.content[0].copy()
        for k, v in headers.items():
            headers[k] = _xjllb_headers.get(k, k)
        self.headers = headers