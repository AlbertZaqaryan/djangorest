from rest_framework import serializers
from .models import Car



# class CarSerializer(serializers.Serializer):
#     category_id = serializers.IntegerField()
#     name = serializers.CharField(max_length=30)
#     price = serializers.IntegerField()
#     about = serializers.CharField()
        
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'