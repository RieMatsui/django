from processing_data.lib.file import read
from processing_data.domein.shop import CustomerEntryYearAndMonth, CustomerName
from processing_data.domein.shop import CustomerEntryDay


class CustomerModel(object):

    def __init__(self):
        self.customer = self.get_customer_all()
        self.num = len(self.customer)

    @staticmethod
    def get_customer_all():
        # 顧客名の空白文字を揃える
        customer = read.excel_read('/data/shop/customer.xlsx')
        return customer
