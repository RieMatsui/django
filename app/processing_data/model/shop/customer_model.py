import pandas

from processing_data.lib.file import read
from processing_data.domein.shop import CustomerName
from processing_data.domein.shop import CustomerEntryYearAndMonth


class CustomerModel(object):

    def __init__(self):
        self.col_customer_name = '顧客名'
        self.col_entry_day = '登録日'
        self.col_entry_year_and_month = '登録年月'
        self.customer = self.get_customer_all()
        self.num = len(self.customer)

    def get_customer_all(self):
        # 顧客名の空白文字を揃える
        customer = read.excel_read('/data/shop/customer.xlsx')
        customerName = CustomerName(customer_name=customer[self.col_customer_name])
        customer[self.col_customer_name] = customerName.trim_customer_name
        is_num_format_day = customer[self.col_entry_day].astype('str').str.isdigit()
        if is_num_format_day.sum() > 0:
            # 登録日のフォーマットを調べ、データの欠損を修正する
            customer[self.col_entry_day] = self.fix_entry_day(customer, is_num_format_day, self.col_entry_day)
        return customer

    @staticmethod
    def fix_entry_day(customer, flg_is_serial, colum_name):
        # 数値で取り込まれている対象を変換する
        entry_day = customer.loc[flg_is_serial, colum_name].astype('float')
        from_serial = pandas.to_timedelta(entry_day, unit='D') + pandas.to_datetime('1900/01/01')

        # 日付として取り込まれている対象の書式変換
        from_string = pandas.to_datetime(customer.loc[~flg_is_serial, colum_name])

        return pandas.concat([from_serial, from_string])

    def get_monthly_user_num(self):
        customer = self.customer
        customer[self.col_entry_year_and_month] = CustomerEntryYearAndMonth(entry_day=
                                                                            customer[self.col_entry_day]).entry_year_month
        return customer.groupby(self.col_entry_year_and_month).count()[self.col_customer_name]

