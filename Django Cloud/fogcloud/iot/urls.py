from django.urls import path
from . import views

urlpatterns = [
    path("api/fan", views.fan_data, name="fan_data"),
    path("control/", views.control_page, name="control_page"),
]
