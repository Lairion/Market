
from rest_framework import serializers
from ..models import Market

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = "__all__"

class MarketProductSelledSerializer(MarketSerializer):
    """docstring for """   

    def to_representation(self, obj):
        rep = super(MarketSerializer,self).to_representation(obj)
        rep.update({
            "sellers":{
            seller.username:seller.how_many_product_selled() for seller in obj.sellers.all()
                }
            })
        return rep

class MarketProductSelledAverageSerializer(MarketSerializer):
    """docstring for """
        

    def to_representation(self, obj):
        rep = super(MarketSerializer,self).to_representation(obj)
        sellers = obj.sellers.all()
        rep.update({
            "average_sale":sum([
                seller.how_many_product_selled() for seller in sellers
            ])/len(sellers)
            })
        return rep
