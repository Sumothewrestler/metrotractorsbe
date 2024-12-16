# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'units', UnitViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'bookings', AdvanceBookingViewSet)
router.register(r'demands', DemandViewSet)
router.register(r'supplies', SupplyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]