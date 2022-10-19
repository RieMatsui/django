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