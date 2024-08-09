from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from django_filters.rest_framework.backends import DjangoFilterBackend
from advertisements.filters import AdvertisementFilter
from advertisements.permissions import AdvertisementPermission
from rest_framework.decorators import action


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    # queryset = Advertisement.objects.exclude(status='DRAFT')
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    permission_classes = (AdvertisementPermission,)

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Advertisement.objects.exclude(status='DRAFT')
        else:
            if user.is_superuser:
                return Advertisement.objects.all()
            else:
                queryset = Advertisement.objects.exclude(status='DRAFT')
                queryset_draft = Advertisement.objects.filter(status='DRAFT') & Advertisement.objects.filter(creator=user)
                return queryset | queryset_draft

    @action(detail=True, methods=['PUT'])
    def mark_as_favorite(self, request, pk=None):
        advertisement = self.get_object()
        advertisement.favorite = request.user.username
        advertisement.save()
        return Response(data={"message": f"Запрос на добавление объявления '{advertisement.title}' в избранное успешно выполнен"})

    @action(detail=False, methods=['GET'])
    def favorite_advertisements(self, request):
        favorite_advertisements = self.queryset.filter(favorite=request.user.username)
        serializer = self.get_serializer(favorite_advertisements, many=True)
        return Response(serializer.data)



