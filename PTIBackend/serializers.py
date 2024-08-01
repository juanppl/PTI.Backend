from rest_framework import serializers
from categories.models import Category
from rest_framework import serializers
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