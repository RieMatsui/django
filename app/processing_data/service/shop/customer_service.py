import pandas

from processing_data.domein.shop import CustomerName, CustomerEntryYearAndMonth
from processing_data.domein.shop import CustomerEntryDay
from processing_data.domein.shop import CustomerSale
from processing_data.model.shop.customer_model import CustomerModel
from processing_data.service.shop.sale_service import SaleService
from processing_data.service.util.data_frame_service import DataFrameService


class CustomerService(object):

    def __init__(self):
        self.customer_model = CustomerModel()

    def get_customer_list(self):
        return self.customer_model.customer

    def get_customer_num(self):
        return self.customer_model.num

    # 顧客データを全て取得する
    def get_customer_all(self):
        customer = self.customer_model.get_customer_all()
        data_flame = DataFrameService()
        customer_name = CustomerName(customer)
        entry_day = CustomerEntryDay(customer)

        # 名前の表記搖れを削除
        customer = data_flame.trim_space(customer, customer_name.col_name)
        # customer[customer_name.col_name] = customer[customer_name.col_name].str.replace("　", "")
        # customer[customer_name.col_name] = customer[customer_name.col_name].str.replace(" ", "")

        # 登録日が数値で登録されているかを確認
        is_num_format_day = data_flame.is_serial(entry_day.row_entry_day)
        if is_num_format_day.sum() > 0:
            # 登録日のフォーマットを調べ、データの欠損を修正する
            customer[entry_day.col_name] = data_flame.fix_entry_day(customer, is_num_format_day, entry_day.col_name)

        return customer

    # 月間登録者数を取得する
    def get_monthly_user_num(self):
        customer = self.get_customer_all()
        customer_name = CustomerName(customer)
        entry_day = CustomerEntryDay(customer)
        entry_year_and_month = CustomerEntryYearAndMonth(customer[entry_day.col_name])
        customer[entry_year_and_month.col_name] = entry_year_and_month.entry_year_month
        return customer.groupby(entry_year_and_month.col_name).count()[customer_name.col_name].to_dict()

    def get_customer_sale(self):
        sale_service = SaleService()
        customer_sale = CustomerSale()
        customer = self.get_customer_all()
        sale = sale_service.get_sale_all()
        customer_name = CustomerName(customer)

        join_data = pandas.merge(sale, customer, left_on=customer_name.col_name_en,
                                 right_on=customer_name.col_name, how='left')
        join_data = join_data.drop(customer_name.col_name_en, axis=1)
        return join_data

    @staticmethod
    def dump_customer_sale(dump_data, export_path, index=False):
        dump_data.to_csv(export_path, index=index)

    def sale_by_item(self):
        customer_sale = self.get_customer_sale()
        return customer_sale.pivot_table(index='purchase_month', columns='item_name', values='item_price',
                                         aggfunc='sum', fill_value=0)
