from processing_data.service.util.data_frame_service import DataFrameService


class CustomerName(object):
    def __init__(self, customer):
        self.col_name = '顧客名'
        self.dataframe = DataFrameService()
        self.row_customer_name = customer[self.col_name]
        self.trim_customer_name = self.dataframe.trim_space(self.row_customer_name)


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
