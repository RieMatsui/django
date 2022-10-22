from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from processing_data.services.shop.customer_service import CustomerService
from processing_data.services.shop.sale_service import SaleService
from processing_data.services.util.data_frame_service import DataFrameService


def index(request: HttpRequest) -> HttpResponse:
    # テンプレートファイル連携
    template_name = 'processing_data/shop/index.html'
    saleService = SaleService()
    sale = saleService.get_sale_all()
    sale_num = saleService.get_sale_num()

    customerService = CustomerService()
    customer = customerService.get_customer_all()
    customer_num = len(customer)

    context = {
        'sale': sale,
        'sale_num': sale_num,
        'customer': customer,
        'customer_num': customer_num,
    }
    return render(request, template_name, context)


def show_sale_per_product(request: HttpRequest) -> HttpResponse:
    template_name = 'processing_data/shop/sale_per_product.html'

    saleService = SaleService()
    sale_per_product = saleService.get_sale_per_product()

    column_count = len(sale_per_product.columns)
    context = {
        'sale_per_product': sale_per_product,
        'column_count': column_count,
    }
    return render(request, template_name, context)


def show_sale_per_price(request: HttpRequest) -> HttpResponse:
    template_name = 'processing_data/shop/sale_per_price.html'

    saleService = SaleService()
    sale_per_price = saleService.get_sale_per_price()

    column_count = len(sale_per_price.columns)

    context = {
        'sale_per_price': sale_per_price,
        'column_count': column_count,
    }
    return render(request, template_name, context)


def show_monthly_user_num(request: HttpRequest) -> HttpResponse:
    template_name = 'processing_data/shop/monthly_user_num.html'

    customer_service = CustomerService()
    monthly_user_num = customer_service.get_monthly_user_num()
    context = {
        'monthly_user_num': monthly_user_num,
        'sum': customer_service.get_customer_num(),
    }
    return render(request, template_name, context)


def show_customer_sale(request: HttpRequest) -> HttpResponse:
    template_name = 'processing_data/shop/customer_sale.html'

    customer_service = CustomerService()
    data_frame = DataFrameService()
    customer_sale = customer_service.get_customer_sale()
    data_frame.dump_customer_sale(customer_sale, 'processing_data/static/csv/dump_data.csv', False)
    context = {
        'customer_sale': customer_sale,
    }
    return render(request, template_name, context)


def show_sale_per_customer(request: HttpRequest) -> HttpResponse:
    template_name = 'processing_data/shop/sale_per_customer.html'

    customer_service = CustomerService()
    sale_per_customer = customer_service.get_sale_per_customer()

    context = {
        'sale_per_customer': sale_per_customer,
    }
    return render(request, template_name, context)