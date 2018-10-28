from rest_framework import routers
from .views import MarketProductSelledViewSet,MarketProductSelledAverageViewSet

router = routers.SimpleRouter()
router.register('markets', MarketProductSelledViewSet)
router.register('markets_average',MarketProductSelledAverageViewSet)

urlpatterns = router.urls