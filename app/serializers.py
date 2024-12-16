# app/serializers.py
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class AdvanceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvanceBooking
        fields = '__all__'

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = '__all__'

class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = '__all__'