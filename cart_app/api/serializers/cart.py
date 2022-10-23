from rest_framework import serializers

from ...models import Cart, CartProduct


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['owner']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='owner',
    )


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'
        read_only_fields = ['user', 'content_type', 'content_object']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user',
    )
