from django.contrib import admin
from cars.models import Car,Features
from django.utils.html import format_html
# Register your models here.
@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    def thumbnail(lef,object):
        return format_html('<img src="{}" width="40" style="border-radius:40%"/>'.format(object.car_photo.url))
    thumbnail.short_description = 'car_image'
    def display_features(self, obj):
        return ', '.join([feature.features for feature in obj.features.all()])
    display_features.short_description = 'features'
    list_display=(
                      'id',
                      'thumbnail',
                      'car_title',
                      'state',
                      'city',
                      'color',
                      'model',
                      'year',
                      'condition',
                      'price',
                      'description',
                      'display_features',
                      'car_photo',
                      'car_photo_1',
                      'car_photo_2',
                      'car_photo_3',
                      'car_photo_4',
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
    list_display_links=('thumbnail','car_title',)
    list_filter = ('price','color','city','year','model','engine','transmission','miles','fuel_type')
    search_fields = ('car_title','state','price','color','city','year','model','engine','transmission','miles','fuel_type')

@admin.register(Features)
class FeaturesModelAdmin(admin.ModelAdmin):
    list_display=('features',)