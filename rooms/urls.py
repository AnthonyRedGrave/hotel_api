from rest_framework.routers import SimpleRouter
from .views import HotelViewSet

router = SimpleRouter()

router.register("hotels", HotelViewSet)

urlpatterns = router.urls
