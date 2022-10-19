from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from processing_data.service.shop.customer_service import CustomerService
from processing_data.service.shop.sale_service import SaleService


def index(request: HttpRequest) -> HttpResponse:
    # テンプレートファイル連携
    template_name = 'processing_data/shop/index.html'
    saleService = SaleService()
    sale = saleService.get_sale_list()
    sale_num = saleService.get_sale_num()

    customerService = CustomerService()
    customer = customerService.get_customer_all()
    customer_num = customerService.get_customer_num()

    context = {
        'sale': sale,
        'sale_num': sale_num,
        'customer': customer,
        'customer_num': customer_num,
    }
    return render(request, template_name, context)


def get_sale_per_product(request: HttpRequest) -> HttpResponse:
    template_name = 'processing_data/shop/sale_per_product.html'

    saleService = SaleService()
    sale_per_product = saleService.get_sale_per_product()

    column_count = len(sale_per_product.columns)
    context = {
        'sale_per_product': sale_per_product,
        'column_count': column_count,
    }
    return render(request, template_name, context)


def get_sale_per_price(request: HttpRequest) -> HttpResponse:
    template_name = 'processing_data/shop/sale_per_price.html'

    saleService = SaleService()
    sale_per_price = saleService.get_sale_per_price()

    column_count = len(sale_per_price.columns)

    context = {
        'sale_per_price': sale_per_price,
        'column_count': column_count,
    }
    return render(request, template_name, context)


def get_monthly_user_num(request: HttpRequest) -> HttpResponse:
    template_name = 'processing_data/shop/monthly_user_num.html'

    customerService = CustomerService()
    monthly_user_num = customerService.get_monthly_user_num()
    context = {
        'monthly_user_num': monthly_user_num,
        'sum': customerService.get_customer_num(),
    }
    return render(request, template_name, context)
