from django.urls import path

from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('item_master', views.item_master, name='item_master'),
    path('transaction', views.transaction, name='transaction'),
    path('transaction_detail', views.transaction_detail, name='transaction_detail'),
    path('sale_data', views.sale_data, name='sale_data')
]
