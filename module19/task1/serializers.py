from rest_framework import serializers
from .models import Game, Buyer


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('title', 'cost', 'size', 'description', 'age_limited', 'buyer', )
