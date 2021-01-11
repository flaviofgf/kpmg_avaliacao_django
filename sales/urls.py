from rest_framework import routers
from .views import SalesViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('sales', SalesViewSet, basename='sales')

urlpatterns = router.urls
