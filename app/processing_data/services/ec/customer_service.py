from processing_data.models.ec.customer_model import CustomerModel


class CustomerService(object):

    def __init__(self):
        self.customer_model = CustomerModel()

    def get_customer_list(self):
        return self.customer_model.get_all()

