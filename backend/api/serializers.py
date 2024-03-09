from rest_framework import serializers
from .models import *

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = ['query', 'timestamp']

class ProductComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comparison
        fields = ['product1', 'product2', 'timestamp']

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comparison
        fields = ['query', 'timestamp']