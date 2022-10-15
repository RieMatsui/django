from django.shortcuts import render
from pandas import pandas
import os
from ..lib.file import read


def index(request):
    # テンプレートファイル連携
    template_name = 'processing_data/customer/index.html'
    sale_data = get_sale_data()
    sale = sale_data['sale']

    customer = read.csv_read('/data/customer/customer.xlsx')
    customer_num = len(customer)

    context = {
        'sale': sale,
        'sale_num': sale_data['sale_num'],
        'customer': customer,
        'customer_num': customer_num,
    }
    return render(request, template_name, context)


def get_sale_data():
    sale = read.csv_read('/file/customer/sale.csv')
    sale['purchase_date'] = pandas.to_datetime(sale['purchase_date'])
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