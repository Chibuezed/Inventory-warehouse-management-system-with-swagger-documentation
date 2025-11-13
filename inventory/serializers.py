from rest_framework import serializers
from .models import Product, Supplier, StockMovement, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = "__all__"

    def create(self, validated_data):
      movement = StockMovement.objects.create(**validated_data)
      product = movement.product

      if movement.movement_type == "IN":
        product.quantity += movement.quantity
      else:
        if product.quantity < movement.quantity:
            raise serializers.ValidationError("Not enough stock.")
        product.quantity -= movement.quantity

      product.save()
      return movement

