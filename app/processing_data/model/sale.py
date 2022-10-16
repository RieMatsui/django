import pandas

from ..lib.file import read


class Sale:

    @staticmethod
    def get_sale_data():
        sale = read.csv_read('/data/customer/sale.csv')
        sale['purchase_date'] = pandas.to_datetime(sale['purchase_date'])
        sale['purchase_month'] = sale['purchase_date'].dt.strftime("%Y%m")
        return sale

