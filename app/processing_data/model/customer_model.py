import pandas
import pandas as pd

from ..lib.file import read


class CustomerModel(object):

    def __init__(self):
        self.customer = self.get_customer()
        self.num = len(self.customer)

    def get_customer(self):
        # 顧客名の空白文字を揃える
        customer = read.excel_read('/data/customer/customer.xlsx')
        customer['顧客名'] = customer['顧客名'].str.replace("　", "")
        customer['顧客名'] = customer['顧客名'].str.replace(" ", "")

        # 登録日のフォーマットを調べ、データの欠損を修正する
        flg_is_serial = customer['登録日'].astype('str').str.isdigit()
        if flg_is_serial.sum() > 0:
            customer['登録日'] = self.fix_entry_day(customer, flg_is_serial)
        return customer

    @staticmethod
    def fix_entry_day(customer, flg_is_serial):
        # 数値で取り込まれている対象を変換する
        entry_day = customer.loc[flg_is_serial, '登録日'].astype('float')
        from_serial = pandas.to_timedelta(entry_day, unit='D') + pd.to_datetime('1900/01/01')

        # 日付として取り込まれている対象の書式変換
        from_string = pd.to_datetime(customer.loc[~flg_is_serial, '登録日'])

        return pd.concat([from_serial, from_string])

    def get_monthly_user_num(self):
        customer = self.customer
        customer["登録年月"] = customer["登録日"].dt.strftime("%Y%m")
        return customer.groupby("登録年月").count()["顧客名"]

