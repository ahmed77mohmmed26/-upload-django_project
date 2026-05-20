from rest_framework import serializers
from .models import DeleviryInformation

class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = DeleviryInformation
        fields = '__all__'