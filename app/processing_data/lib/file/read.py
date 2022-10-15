from pandas import pandas
import os


def csv_read(file_path):
    # TODO ファイルパスを適切に読み込みたい
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + file_path
    csv_data = pandas.read_csv(filePath)
    return csv_data


def excel_read(file_path):
    # TODO ファイルパスを適切に読み込みたい
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + file_path
    csv_data = pandas.read_csv(filePath)
    return csv_data
