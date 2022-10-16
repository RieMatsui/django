from ..model.sale_model import SaleModel


class SaleService(object):

    def __init__(self):
        self.sale_model = SaleModel()

    def get_sale_list(self):
        return self.sale_model.sale

    def get_sale_num(self):
        return self.sale_model.num

    def get_sale_per_product(self):
        return self.sale_model.get_sale_per_product()

    def get_sale_per_price(self):
        return self.sale_model.get_sale_per_price()