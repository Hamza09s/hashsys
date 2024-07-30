from rest_framework.viewsets import ReadOnlyModelViewSet

from accounts.serializers import BuisnessSerializer
from tenant_shared.models import Buisness, City, Country, State
from .serializers import CountrySerializer, CitySerializer, StateSerializer


class CityViewSet(ReadOnlyModelViewSet):

    serializer_class = CitySerializer
    queryset = City.objects.all()


class CountryViewSet(ReadOnlyModelViewSet):

    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class StateViewSet(ReadOnlyModelViewSet):

    serializer_class = StateSerializer
    queryset = State.objects.all()
