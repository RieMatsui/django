from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("list", views.List.as_view(), name="list"),
    path("tuple", views.Tuple.as_view(), name="tuple"),
    path('seat', views.Seat.as_view(), name='seat'),
    ]