from rest_framework import serializers

from .models import Board, Cartegory

class CartegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartegory
        fields = ('name',)

class BoardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    hit = serializers.IntegerField(read_only=True)

    class Meta:
        model = Board
        fields = (
            'id',
            'user',
            'title',
            'content',
            'created_at',
            'updated_at',
            'hit'
        )