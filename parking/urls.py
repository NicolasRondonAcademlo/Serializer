from django.urls import  path
from parking import  views

urlpatterns = [
    path("cars/", views.car_list),
    path("cars/<int:pk>", views.car_get_info),
]