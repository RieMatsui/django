import pandas

from processing_data.services.util.data_frame_service import DataFrameService


class SaleModel(object):

    def __init__(self):
        self.sale = self.get_sale_all()
        self.num = len(self.sale)

    @staticmethod
    def get_sale_all():
        sale = DataFrameService.csv_read('processing_data/static/data/shop/sale.csv')

        sale["purchase_date"] = pandas.to_datetime(sale["purchase_date"])
        sale["purchase_month"] = sale["purchase_date"].dt.strftime("%Y%m")

        # 商品名のゆれを修正
        sale["item_name"] = sale["item_name"].str.upper()
        sale["item_name"] = sale["item_name"].str.replace("　", "")
        sale["item_name"] = sale["item_name"].str.replace(" ", "")
        sale.sort_values(by=["item_name"], ascending=True)

        # 金額の欠損値を修正
        flg_is_null = sale['item_price'].isnull()
        # 金額の欠損値しているものを処理する
        for trg in list(sale.loc[flg_is_null, "item_name"].unique()):
            # 同じ商品で、金額を取得する
            price = sale.loc[(~flg_is_null) & (sale["item_name"] == trg), "item_price"].max()
            # 欠損しているデータに正しい金額を代入する
            sale["item_price"].loc[flg_is_null & (sale["item_name"] == trg)] = price

        return sale

    def get_sale_per_product(self):
        return self.sale.pivot_table(index="purchase_month", columns='item_name', aggfunc='size', fill_value=0)

    def get_sale_per_price(self):
        return self.sale.pivot_table(index="purchase_month", columns='item_name',
                                     values='item_price', aggfunc='sum', fill_value=0)


