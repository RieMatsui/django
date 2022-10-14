from django.conf import settings
from django.conf.urls.static import static
from .views import sale_data
from .views import customer
from django.urls import include, path

urlpatterns = [
                  path('', sale_data.index, name='index'),
                  path('item_master', sale_data.item_master, name='item_master'),
                  path('transaction', sale_data.transaction, name='transaction'),
                  path('transaction_detail', sale_data.transaction_detail, name='transaction_detail'),
                  path('sale_data', sale_data.sale_data, name='sale_data'),
                  path('customer', customer.Customer.as_view(), name='index'),
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
