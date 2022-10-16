import os

from django.shortcuts import render
from pandas import pandas

from ..lib.file import read
from ..model import customer as m_customer
from ..model import sale as m_sale


def index(request):
    # テンプレートファイル連携
    template_name = 'processing_data/customer/index.html'
    saleObject = m_sale.Sale()
    sale = saleObject.sale
    sale_num = saleObject.num

    customerObject = m_customer.Customer()
    customer = customerObject.customer
    customer_num = customerObject.num

    context = {
        'sale': sale,
        'sale_num': sale_num,
        'customer': customer,
        'customer_num': customer_num,
    }
    return render(request, template_name, context)


def get_sale_per_product(request):
    template_name = 'processing_data/customer/sale_per_product.html'

    sale = m_sale.Sale()
    sale_per_product = sale.get_sale_per_product()

    column_count = len(sale_per_product.columns)
    context = {
        'sale_per_product': sale_per_product,
        'column_count': column_count,
    }
    return render(request, template_name, context)


def get_sale_per_price(request):

    template_name = 'processing_data/customer/sale_per_price.html'

    sale = m_sale.Sale()
    sale_per_price = sale.get_sale_per_price()

    column_count = len(sale_per_price.columns)

    context = {
        'sale_per_price': sale_per_price,
        'column_count': column_count,
    }
    return render(request, template_name, context)


def get_monthly_user_num(request):

    template_name = 'processing_data/customer/monthly_user_num.html'

    customer = m_customer.Customer()
    monthly_user_num = customer.get_monthly_user_num()
    monthly_user_num = monthly_user_num.to_dict()

    context = {
        'monthly_user_num': monthly_user_num,
        'sum': customer.num,
    }
    return render(request, template_name, context)