from django.urls import path
from .views import index
from .views import list
from .views import seat
from .views import tuple
from .views import dict
from .views import sets

urlpatterns = [
    path("", index.Index.as_view(), name="index"),
    path("lists", list.Index.as_view(), name="lists.index"),
    path('lists/seat', seat.Seat.as_view(), name='lists.seat'),
    path("tuple", tuple.Tuple.as_view(), name="tuple"),
    path("dict", dict.Dict.as_view(), name="dict.index"),
    path("dict/price_check", dict.PriceCheck.as_view(), name="dict.price_check"),
    path("sets", sets.Index.as_view(), name="index")
]