from django.urls import path, include
from .views import *
from .serializers import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'auth', LoginViewset, basename='auth')
router.register(r'signup', SignUpViewset, basename='signup')
router.register(r'review', ReviewViewset, basename='review')
router.register(r'listing', ListingViewset, basename='listing')
router.register(r'booking', BookingViewSet, basename='booking')
router.register(r'payment', PaymentViewSet, basename='payment')




urlpatterns = [
    path("", include(router.urls))
]
