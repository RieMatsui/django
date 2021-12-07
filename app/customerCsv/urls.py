from django.urls import path

from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('itemMaster', views.itemMaster, name='itemMaster'),
    path('transaction', views.transaction, name='transaction'),
    path('transactionDetail', views.transactionDetail, name='transactionDetail'),
    path('saleData', views.saleData, name='saleData')
]
