import pandas
from django.test import TestCase

from processing_data.service.util.data_frame_service import DataFrameService


class DataFrameServiceTests(TestCase):
    """
    全角空白と半角空白をトリムする
    """
    def test_trim_space(self):
        list2 = [["P001", "iPhone 8 64GB", 85000],
                 ["P002", "iPhone X　256GB", 130000],
                 ["P003", "iPhone　SE 32GB", 37000]]
        columns2 = ["Product_ID", "Product_Name", "Price"]
        data = pandas.DataFrame(data=list2, columns=columns2)
        data_frame = DataFrameService()
        data_frame.trim_space(data, 'Product_Name')

        # 全角空白と半角空白をトリムできていること
        self.assertEqual(data.loc[0:, "Product_Name"][0], 'iPhone864GB')
        self.assertEqual(data.loc[0:, "Product_Name"][1], 'iPhoneX256GB')
        self.assertEqual(data.loc[0:, "Product_Name"][2], 'iPhoneSE32GB')
