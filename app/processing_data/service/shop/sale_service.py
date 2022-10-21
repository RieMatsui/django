from processing_data.model.shop.sale_model import SaleModel


class SaleService(object):

    def __init__(self):
        self.sale_model = SaleModel()

    def get_sale_all(self):
        return self.sale_model.get_sale_all()

    def get_sale_num(self):
        return self.sale_model.num

    def get_sale_per_product(self):
        return self.sale_model.get_sale_per_product()

    def get_sale_per_price(self):
        return self.sale_model.get_sale_per_price()
