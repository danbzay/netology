from django.urls import path
from rest_framework import routers

from .views import MeasurementViewSet, SensorViewSet

router = routers.SimpleRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'measurements',MeasurementViewSet)
urlpatterns = router.urls
    # TODO: зарегистрируйте необходимые маршруты

