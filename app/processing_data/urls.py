from django.conf import settings
from django.conf.urls.static import static
from .views import sale
from .views import customer
from django.urls import include, path

urlpatterns = [
                  path('sale', sale.index, name='index'),
                  path('sale/item_master', sale.item_master, name='item_master'),
                  path('sale/transaction', sale.transaction, name='transaction'),
                  path('sale/transaction_detail', sale.transaction_detail, name='transaction_detail'),
                  path('sale/sale_data', sale.sale_data, name='sale_data'),
                  path('customer', customer.index, name='index'),
                  path('customer/sale_per_product', customer.get_sale_per_product, name='sale_per_product'),
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
