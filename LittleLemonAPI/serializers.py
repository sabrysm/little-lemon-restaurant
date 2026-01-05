from decimal import Decimal
from rest_framework import serializers
from .models import MenuItem, Category 

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'category', 'price_after_tax']
        depth = 1
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value
    
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock must be a non-negative integer.")
        return value
    
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category, created = Category.objects.get_or_create(**category_data)
        menu_item = MenuItem.objects.create(category=category, **validated_data)
        return menu_item
    
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal('0.1')