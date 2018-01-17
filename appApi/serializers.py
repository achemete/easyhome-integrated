from appApi import models
from rest_framework import serializers

class AccomodationsSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = models.Accomodations
        fields = ('title', 'description','price','image','image2','image3','image4','owner','visibility',
                  'guests', 'bedrooms', 'beds','bathroom','services','rules','extraInfo','city',
                  'kindOfHouse','reviews','locationMap','published_date')

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Users
        fields = ('first_name','last_name','email','location','postal',)

class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Reviews
        fields = ('count','stars')

class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Services
        fields = ('wifi','shower','kitchen','surveillanceCamera','HeatingSystem','Television')

class AttractionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Attractions
        fields = ('name','built','kindOfAttractions','title1','title2','title3','description1','description2','description3','address','image','image2','image3','city','link','locationMap')

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ('name','description','priceRange','address','image','image2','image3','city','link','locationMap','kindOfRestaurant')

class DealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Deal
        fields = ('price','accomodations','attractions','restaurant','description')
