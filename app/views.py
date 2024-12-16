# app/views.py
from rest_framework import viewsets
from .models import *
from .serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AdvanceBookingViewSet(viewsets.ModelViewSet):
    queryset = AdvanceBooking.objects.all()
    serializer_class = AdvanceBookingSerializer

class DemandViewSet(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer

class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer