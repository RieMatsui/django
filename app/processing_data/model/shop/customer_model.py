from processing_data.service.util.data_frame_service import DataFrameService


class CustomerModel(object):

    def __init__(self):
        self.customer = self.get_customer_all()
        self.num = len(self.customer)

    @staticmethod
    def get_customer_all():
        # 顧客名の空白文字を揃える
        customer = DataFrameService.excel_read('processing_data/static/data/shop/customer.xlsx')
        return customer
