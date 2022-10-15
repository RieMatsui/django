from django.views.generic import TemplateView
from django.shortcuts import render
from pandas import pandas as pd
import os

def index(request):
    # テンプレートファイル連携
    template_name = 'processing_data/customer/index.html'
    sale_data = get_sale_data()
    sale = sale_data['sale']

    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/file/customer/customer.xlsx'
    customer = pd.read_excel(filePath)
    customer_num = len(customer)

    context = {
        'sale': sale,
        'sale_num': sale_data['sale_num'],
        'customer': customer,
        'customer_num': customer_num,
    }
    return render(request, template_name, context)


def get_sale_data():
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/file/customer/sale.csv'
    sale = pd.read_csv(filePath)
    sale['purchase_date'] = pd.to_datetime(sale['purchase_date'])
    sale['purchase_month'] = sale['purchase_date'].dt.strftime("%Y%m")
    sale_num = len(sale)
    return {'sale': sale, 'sale_num': sale_num}


def get_sale_per_product(request):
    template_name = 'processing_data/customer/sale_per_product.html'
    sale_data = get_sale_data()
    sale = sale_data['sale']

    sale_per_product = sale.pivot_table(index="purchase_date", columns='item_name', aggfunc='size', fill_value=0)
    column_count = len(sale_per_product.columns)
    context = {
        'sale_per_product': sale_per_product,
        'column_count': column_count,
    }
    return render(request, template_name, context)