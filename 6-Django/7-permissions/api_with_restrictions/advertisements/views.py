from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
import django_filters.rest_framework as filters
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer

class AdvertisementFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at']

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AdvertisementFilter 

    def get_permissions(self):
        # Получение прав для действий.
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
