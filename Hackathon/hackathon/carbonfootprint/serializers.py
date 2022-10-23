from rest_framework import serializers
from .models import users, device, calculation_of_carbon_footprint, treek

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = ('id',
                  'user_id',
                  )

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = ('id',
                  'users_id',
                  'device_id',
                  'device_type')

class Carbon_footprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = calculation_of_carbon_footprint
        fields = ('id',
                  'device_id',
                  'userss_id',
                  'electricty_consumption',
                  'mileage',
                  'family_members',
                  'created_date')




