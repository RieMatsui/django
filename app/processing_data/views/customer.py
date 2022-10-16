from django.shortcuts import render
from pandas import pandas
import os
from ..lib.file import read
from ..model import sale as m_sale


def index(request):
    # テンプレートファイル連携
    template_name = 'processing_data/customer/index.html'
    sale = m_sale.Sale.get_sale_data()
    sale_num = len(sale)

    customer = read.excel_read('/data/customer/customer.xlsx')
    customer_num = len(customer)

    context = {
        'sale': sale,
        'sale_num': sale_num,
        'customer': customer,
        'customer_num': customer_num,
    }
    return render(request, template_name, context)


def get_sale_per_product(request):
    template_name = 'processing_data/customer/sale_per_product.html'
    sale = m_sale.Sale.get_sale_data()
    sale_per_product = m_sale.Sale.get_sale_per_product(sale=sale)

    column_count = len(sale_per_product.columns)
    context = {
        'sale_per_product': sale_per_product,
        'column_count': column_count,
    }
    return render(request, template_name, context)