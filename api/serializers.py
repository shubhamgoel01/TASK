from api.models import MobileCompany, Customer
from rest_framework import serializers

class MobileCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = MobileCompany
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    customer = MobileCompanySerializer(many=True,read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'