from rest_framework import viewsets,mixins
from .serializers import MarketProductSelledSerializer,MarketProductSelledAverageSerializer
from ..models import Market

class MarketProductSelledViewSet(
	mixins.ListModelMixin,
	mixins.RetrieveModelMixin,
	viewsets.GenericViewSet):

    queryset = Market.objects.all()
    serializer_class = MarketProductSelledSerializer

class MarketProductSelledAverageViewSet(
	MarketProductSelledViewSet
	):

    serializer_class = MarketProductSelledAverageSerializer