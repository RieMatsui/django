from processing_data.model.shop.customer_model import CustomerModel


class CustomerService(object):

    def __init__(self):
        self.customer_model = CustomerModel()

    def get_customer_list(self):
        return self.customer_model.customer

    def get_customer_num(self):
        return self.customer_model.num

    def get_monthly_user_num(self):
        return self.customer_model.get_monthly_user_num()

    def get_customer(self):
        return self.customer_model.get_customer()