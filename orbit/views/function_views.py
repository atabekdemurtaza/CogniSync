from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from ..api.serializers import ProductSerializer, UserSerializer


@api_view(http_method_names=['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/category/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/<update>/<id>/',
        '/api/users/profile/'
    ]
    return Response(
        routes
    )


@api_view(http_method_names=['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)
