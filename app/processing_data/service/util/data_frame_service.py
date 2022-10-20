import pandas


class DataFrameService(object):

    @staticmethod
    def trim_space(value):
        """
        トリムするためのクラス
        :param value:
        :return:
        """
        return value.str.replace("　", "").replace(" ", "")

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

