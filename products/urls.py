from django.urls import path

from products.views import create_product, delete_product, get_all_products, get_product, update_product


urlpatterns = [
    # path('get-list-of-categories/', get_all_categories)
    path('get-all-products', get_all_products, name='get-all-products'),
    path('create', create_product, name='create-product'),
    path('<int:pk>', get_product, name='get-product'),
    path('<int:pk>/update', update_product, name='update-product'),
    path('<int:pk>/delete', delete_product, name='delete-product'),
]