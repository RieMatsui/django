from django.views.generic import TemplateView
from django.shortcuts import render
from pandas import pandas as pd
import os


class Customer(TemplateView):

    def get(self, request):
        # テンプレートファイル連携
        template_name = 'processing_data/customer/index.html'
        filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/file/customer/sale.csv'
        sale = pd.read_csv(filePath)
        sale_num = len(sale)

        filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/file/customer/customer.xlsx'
        customer = pd.read_excel(filePath)
        customer_num = len(customer)

        context = {
            'sale': sale,
            'sale_num': sale_num,
            'customer': customer,
            'customer_num': customer_num,
        }
        return render(request, template_name, context)


customerView = Customer.as_view()
