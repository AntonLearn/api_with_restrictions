from django.contrib.auth import get_user_model
from django_filters.rest_framework.filterset import FilterSet
from django_filters.rest_framework.filters import DateFromToRangeFilter
from django_filters.rest_framework.filters import ModelChoiceFilter
from advertisements.models import Advertisement


User = get_user_model()


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    creator = ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', 'status', 'favorite']


