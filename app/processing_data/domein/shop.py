from processing_data.service.util.data_frame_service import DataFrameService


class CustomerName(object):
    def __init__(self, customer_name):
        self.dataframe = DataFrameService()
        self.row_customer_name = customer_name
        self.trim_customer_name = self.dataframe.trim_space(customer_name)


class CustomerEntryYearAndMonth(object):
    def __init__(self, entry_day):
        self.entry_year_month = entry_day.dt.strftime("%Y%m")
