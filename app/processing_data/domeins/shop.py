from processing_data.services.util.data_frame_service import DataFrameService


class CustomerSale(object):
    def __init__(self):
        self.columns = ['purchase_date', 'purchase_month', 'item_name',
                        'item_price', '顧客名', 'かな', '地域', 'メールアドレス', '登録日']


class CustomerName(object):
    def __init__(self, customer):
        self.col_name = '顧客名'
        self.col_name_en = 'customer_name'
        self.row_customer_name = customer[self.col_name]


class CustomerEntryYearAndMonth(object):
    def __init__(self, entry_day):
        self.col_name = '登録年月'
        self.entry_year_month = entry_day.dt.strftime("%Y%m")


class CustomerEntryDay(object):
    def __init__(self, customer):
        self.col_name = '登録日'
        self.row_entry_day = customer[self.col_name]
        self.dataframe = DataFrameService()
        self.is_serial = self.dataframe.is_serial(self.row_entry_day)
