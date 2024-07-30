from rest_framework import serializers
from categories.models import Category
from rest_framework import serializers
from products.models import Product

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
