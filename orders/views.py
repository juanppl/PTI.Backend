from django.shortcuts import render
from datetime import date
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from PTIBackend.serializers import OrderSerializer
from orders.models import Order
from users.models import User

# Create your views here.

@api_view(['GET'])
def get_all_orders(request):
    orders = Order.objects.filter(wasCancelled=False)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_orders(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    
    orders = Order.objects.filter(user=user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def pay_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    order.paidDate = date.today()
    order.status = "Pagada"

    order.save()

    return Response(status=status.HTTP_204_NO_CONTENT)    

@api_view(['POST'])
def cancel_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)

    order.wasCancelled = True
    order.cancelledDate = date.today()
    order.status = "Cancelada"

    order.save()

    return Response(status=status.HTTP_204_NO_CONTENT)    
