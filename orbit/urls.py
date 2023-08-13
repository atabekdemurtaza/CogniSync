from django.urls import path, include
from .views import function_views
from .views import class_views as views
from rest_framework import routers

app_name = 'orbit'

router = routers.SimpleRouter()
router.register(prefix=r'category', viewset=views.CategoryView)

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
    path(route='', view=include(router.urls)),
    path(
        route='users/profile/',
        view=function_views.getUserProfile,
        name='users-profile'
    )
]
