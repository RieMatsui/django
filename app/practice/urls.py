from django.urls import path
from .views import index
from .views import list
from .views import seat
from .views import tuple

urlpatterns = [
    path("", index.Index.as_view(), name="index"),
    path("list", list.List.as_view(), name="list"),
    path('seat', seat.Seat.as_view(), name='seat'),
    path("tuple", tuple.Tuple.as_view(), name="tuple"),
]