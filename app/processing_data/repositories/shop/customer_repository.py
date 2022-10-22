import pandas

from processing_data.domeins.shop import CustomerName, CustomerEntryDay, CustomerEntryYearAndMonth
from processing_data.models.shop.customer_model import CustomerModel
from processing_data.services.shop.sale_service import SaleService
from processing_data.services.util.data_frame_service import DataFrameService


class CustomerRepository(object):

    def __init__(self):
        self.customer_model = CustomerModel()

    def get_customer_all(self):
        customer = self.customer_model.get_customer_all()
        data_flame = DataFrameService()
        customer_name = CustomerName(customer)
        entry_day = CustomerEntryDay(customer)

        # 名前の表記搖れを削除
        customer = data_flame.trim_space(customer, customer_name.col_name)

        # 登録日が数値で登録されているかを確認
        is_num_format_day = data_flame.is_serial(entry_day.row_entry_day)
        if is_num_format_day.sum() > 0:
            # 登録日のフォーマットを調べ、データの欠損を修正する
            customer[entry_day.col_name] = data_flame.fix_entry_day(customer, is_num_format_day, entry_day.col_name)

        return customer

    def get_monthly_user_num(self):
        customer = self.get_customer_all()
        customer_name = CustomerName(customer)
        entry_day = CustomerEntryDay(customer)
        entry_year_and_month = CustomerEntryYearAndMonth(customer[entry_day.col_name])
        customer[entry_year_and_month.col_name] = entry_year_and_month.entry_year_month
        return customer.groupby(entry_year_and_month.col_name).count()[customer_name.col_name].to_dict()

    def get_customer_sale(self):
        customer = self.get_customer_all()
        customer_name = CustomerName(customer)
        # TODO 修正する
        sale_service = SaleService()
        sale = sale_service.get_sale_all()

        join_data = pandas.merge(sale, customer, left_on=customer_name.col_name_en,
                                 right_on=customer_name.col_name, how='left')
        join_data = join_data.drop(customer_name.col_name_en, axis=1)
        return join_data

    def get_sale_per_customer(self):
        customer = self.get_customer_all()
        customer_name = CustomerName(customer)
        # TODO 修正する
        sale_service = SaleService()
        sale = sale_service.get_sale_all()

        join_data = pandas.merge(sale, customer, left_on=customer_name.col_name_en,
                                 right_on=customer_name.col_name, how='left')
        join_data = join_data.drop(customer_name.col_name_en, axis=1)
        return join_data.pivot_table(index='purchase_month', columns=customer_name.col_name,
                              aggfunc='size', fill_value=0)