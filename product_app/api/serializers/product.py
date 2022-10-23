from rest_framework import serializers

from product_app.models import Sport, Goods, TV, Toys


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class TVSerializer(serializers.ModelSerializer):
    class Meta:
        model = TV
        fields = '__all__'


class ToysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toys
        fields = '__all__'
