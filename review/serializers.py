from rest_framework import serializers
from . import Review




class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'