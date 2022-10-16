import os

from django.shortcuts import render
from pandas import pandas

from ..lib.file import read
from ..service import customer_service
from ..service import sale_service


def index(request):
    # テンプレートファイル連携
    template_name = 'processing_data/customer/index.html'
    saleService = sale_service.SaleService()
    sale = saleService.get_sale_list()
    sale_num = saleService.get_sale_num()

    customerService = customer_service.CustomerService()
    customer = customerService.get_customer()
    customer_num = customerService.get_customer_num()

    context = {
        'sale': sale,
        'sale_num': sale_num,
        'customer': customer,
        'customer_num': customer_num,
    }
    return render(request, template_name, context)


def get_sale_per_product(request):
    template_name = 'processing_data/customer/sale_per_product.html'

    saleService = sale_service.SaleService()
    sale_per_product = saleService.get_sale_per_product()

    column_count = len(sale_per_product.columns)
    context = {
        'sale_per_product': sale_per_product,
        'column_count': column_count,
    }
    return render(request, template_name, context)


def get_sale_per_price(request):

    template_name = 'processing_data/customer/sale_per_price.html'

    saleService = sale_service.SaleService()
    sale_per_price = saleService.get_sale_per_price()

    column_count = len(sale_per_price.columns)

    context = {
        'sale_per_price': sale_per_price,
        'column_count': column_count,
    }
    return render(request, template_name, context)


def get_monthly_user_num(request):

    template_name = 'processing_data/customer/monthly_user_num.html'

    customerService = customer_service.CustomerService()
    monthly_user_num = customerService.get_monthly_user_num()
    monthly_user_num = monthly_user_num.to_dict()

    context = {
        'monthly_user_num': monthly_user_num,
        'sum': customerService.get_customer_num(),
    }
    return render(request, template_name, context)