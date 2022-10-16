import pandas

from ..lib.file import read


class Sale:

    @staticmethod
    def get_sale_data():
        sale = read.csv_read('/data/customer/sale.csv')
        sale['purchase_date'] = pandas.to_datetime(sale['purchase_date'])
        sale['purchase_month'] = sale['purchase_date'].dt.strftime("%Y%m")
        return sale

    @staticmethod
    def get_sale_per_product(sale):
        sale_per_product = sale.pivot_table(index="purchase_date", columns='item_name', aggfunc='size', fill_value=0)
        return sale_per_product
