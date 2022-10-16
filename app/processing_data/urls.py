from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ec
from .views import shop

urlpatterns = [
                  path('ec', ec.index, name='index'),
                  path('ec/item_master', ec.item_master, name='item_master'),
                  path('ec/transaction', ec.transaction, name='transaction'),
                  path('ec/transaction_detail', ec.transaction_detail, name='transaction_detail'),
                  path('ec/sale_data', ec.sale_data, name='sale_data'),
                  path('shop', shop.index, name='index'),
                  path('shop/sale_per_product', shop.get_sale_per_product, name='sale_per_product'),
                  path('shop/sale_per_price', shop.get_sale_per_price, name='sale_per_price'),
                  path('shop/monthly_user_num', shop.get_monthly_user_num, name='monthly_user_num'),
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
