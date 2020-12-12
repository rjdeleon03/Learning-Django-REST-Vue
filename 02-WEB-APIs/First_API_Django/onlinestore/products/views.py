from django.http import JsonResponse
from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()  # [:30]
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_cost": product.shipping_cost,
            "quantity": product.quantity,
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {

                "code": 404,
                "message": "Product not found!"
            }
        }, status=404)

    return response


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    data = {"manufacturers": [m for m in
                              list(manufacturers.values()) if m["active"] == True]}
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        products = manufacturer.products.values()
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
            "products": list(products.values())
        }}
        response = JsonResponse(data)
    except:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "Manufacturer not found!"
            }
        }, status=404)

    return response


# Create your views here.
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"


# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"
