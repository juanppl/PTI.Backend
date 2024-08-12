
from django.urls import path

from orders.views import cancel_order, create_order, get_all_orders, user_orders



urlpatterns = [
    path('get-order-list/', get_all_orders, name='get-all-orders'),
    path('create-order/', create_order),
    path('user-orders/<int:user_id>/', user_orders),
    path('cancel-order/<int:order_id>/', cancel_order),
]