from rest_framework import serializers
from categories.models import Category
from rest_framework import serializers
from orders.models import Order, OrderItem
from products.models import Product
from users.models import User

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['categoryId', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all()) 

    class Meta:
        model = Product
        fields = ['id', 'fullName', 'displayName', 'description', 'price', 'isActive', 'creationDate', 
                  'expireDate', 'category', 'availableQty', 'lastModificationDate', 'isDeleted', 'deletedDate']

class ProductDtoSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'fullName', 'displayName', 'description', 'price', 'isActive', 'creationDate', 
                  'expireDate', 'category', 'availableQty', 'lastModificationDate', 'isDeleted', 'deletedDate']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'bio')
        read_only_fields = ('username', )
    
    
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'bio')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.bio = validated_data['bio']
        # instance.email = validated_data['email']
        # instance.username = validated_data['username']

        instance.save()

        return instance

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id',
        'user',
        'price',
        'creationDate',
        'paidDate',
        'status',
        'wasCancelled',
        'cancelledDate',
        'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
        

class OrderDtoItemSerializer(serializers.ModelSerializer):
    product = ProductDtoSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity']

class OrderDtoSerializer(serializers.ModelSerializer):
    items = OrderDtoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id',
        'user',
        'price',
        'creationDate',
        'paidDate',
        'status',
        'wasCancelled',
        'cancelledDate',
        'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order