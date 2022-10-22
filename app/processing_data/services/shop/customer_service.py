from processing_data.repositories.shop.customer_repository import CustomerRepository

class CustomerService(object):

    def __init__(self):
        self.customer_repository = CustomerRepository()

    # 顧客データを全て取得する
    def get_customer_all(self):
        return self.customer_repository.get_customer_all()

    # 月間登録者数を取得する
    def get_monthly_user_num(self):
        return self.customer_repository.get_monthly_user_num()

    def get_customer_sale(self):
        return self.customer_repository.get_customer_sale()

    def get_sale_per_customer(self):
        return self.customer_repository.get_sale_per_customer()




