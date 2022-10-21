from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from processing_data.views import ec
from processing_data.views import shop

urlpatterns = [
                  path('ec', ec.index, name='index'),
                  path('ec/item_master', ec.item_master, name='item_master'),
                  path('ec/sale_data', ec.sale_data, name='sale_data'),
                  path('ec/transaction', ec.transaction, name='transaction'),
                  path('ec/transaction_detail', ec.transaction_detail, name='transaction_detail'),
                  path('shop', shop.index, name='index'),
                  path('shop/customer_sale', shop.show_customer_sale, name='customer_sale'),
                  path('shop/monthly_user_num', shop.show_monthly_user_num, name='monthly_user_num'),
                  path('shop/sale_per_product', shop.show_sale_per_product, name='sale_per_product'),
                  path('shop/sale_per_price', shop.show_sale_per_price, name='sale_per_price'),
                  path('shop/sale_per_customer', shop.show_sale_per_customer, name='sale_per_customer'),
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
