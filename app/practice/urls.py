from django.urls import path
from .views import index
from .views import list
from .views import seat
from .views import tuple
from .views import dict

urlpatterns = [
    path("", index.Index.as_view(), name="index"),
    path("list", list.List.as_view(), name="list"),
    path('seat', seat.Seat.as_view(), name='seat'),
    path("tuple", tuple.Tuple.as_view(), name="tuple"),
    path("dict", dict.Dict.as_view(), name="dict"),
    path("dict/price_check", dict.PriceCheck.as_view(), name="price_check"),
]