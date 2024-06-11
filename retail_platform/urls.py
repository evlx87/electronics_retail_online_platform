from rest_framework.routers import DefaultRouter

from electronic_network.apps import ElectronicNetworkConfig
from electronic_network.views import SupplierViewSet, ProductViewSet, ContactViewSet

app_name = ElectronicNetworkConfig.name

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'contact', ContactViewSet, basename='contact')

urlpatterns = router.urls