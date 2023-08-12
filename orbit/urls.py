from django.urls import path
from .views import function_views
from .views import class_views as views


app_name = 'orbit'

urlpatterns = [
    path(
        'users/login',
        views.MyTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(route='', view=function_views.getRoutes, name='routes'),
    path(
        route='products/',
        view=views.ProductListView.as_view(),
        name='products'
    ),
    path(
        route='products/<str:pk>/',
        view=views.ProductDetailView.as_view(),
        name='product'
    ),
]
