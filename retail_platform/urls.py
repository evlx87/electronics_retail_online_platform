from rest_framework.routers import DefaultRouter

from retail_platform.apps import RetailPlatformConfig
from retail_platform.views import SupplierViewSet, ProductViewSet, ContactViewSet

app_name = RetailPlatformConfig.name

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = router.urls
