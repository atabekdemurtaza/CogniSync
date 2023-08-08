from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.getRoutes, name='routes'),
    path(route='products/', view=views.getProducts, name='products'),
    path(route='products/<str:pk>/', view=views.getProduct, name='product'),
]
