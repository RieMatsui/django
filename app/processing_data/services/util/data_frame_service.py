import os

import pandas

from config import settings


class DataFrameService(object):

    @staticmethod
    def trim_space(data, column_name):
        """
        トリムするメソッド
        :param data:
        :param column_name:
        :return:
        """
        data[column_name] = data[column_name].str.replace("　", "")
        data[column_name] = data[column_name].str.replace(" ", "")
        return data

    @staticmethod
    def is_serial(value):
        is_serial = value.astype('str').str.isdigit()
        return is_serial

    @staticmethod
    def fix_entry_day(customer, flg_is_serial, colum_name):
        # 数値で取り込まれている対象を変換する
        entry_day = customer.loc[flg_is_serial, colum_name].astype('float')
        from_serial = pandas.to_timedelta(entry_day, unit='D') + pandas.to_datetime('1900/01/01')

        # 日付として取り込まれている対象の書式変換
        from_string = pandas.to_datetime(customer.loc[~flg_is_serial, colum_name])

        return pandas.concat([from_serial, from_string])

    @staticmethod
    def csv_read(file_path):
        filePath = settings.APP_URL + file_path
        csv_data = pandas.read_csv(filePath)
        return csv_data

    @staticmethod
    def excel_read(file_path):
        filePath = settings.APP_URL + file_path
        csv_data = pandas.read_excel(filePath)
        return csv_data

    @staticmethod
    def dump_customer_sale(dump_data, export_path, index=False):
        dump_data.to_csv(export_path, index=index)
