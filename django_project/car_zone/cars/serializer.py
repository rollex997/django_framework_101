from rest_framework import serializers
from cars.models import *
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields=(
                      'id',
                      'car_title',
                      'state',
                      'city',
                      'color',
                      'model',
                      'year',
                      'condition',
                      'price',
                      'description',
                      'car_photo',
                      'car_photo_1',
                      'car_photo_2',
                      'car_photo_3',
                      'car_photo_4',
                      'features',
                      'body_style',
                      'engine',
                      'transmission',
                      'interior',
                      'miles',
                      'doors',
                      'passengers',
                      'vin_no',
                      'milage',
                      'fuel_type',
                      'no_of_owners',
                      'is_featured',
                      'created_date',
                 )
        read_only_fields=('created_date','doors','features','year','state')

class CarAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields = fields=(
                      'id',
                      'car_title',
                      'state',
                      'city',
                      'color',
                      'model',
                      'year',
                      'condition',
                      'price',
                      'description',
                      'car_photo',
                      'car_photo_1',
                      'car_photo_2',
                      'car_photo_3',
                      'car_photo_4',
                      'features',
                      'body_style',
                      'engine',
                      'transmission',
                      'interior',
                      'miles',
                      'doors',
                      'passengers',
                      'vin_no',
                      'milage',
                      'fuel_type',
                      'no_of_owners',
                      'is_featured',
        )

class CarFeaturesSerializer(serializers.ModelField):
    class Meta:
        model = Features
        fields=('features',)
        read_only_fields=('features',)