from rest_framework.serializers import ModelSerializer
from trips.models import Trip
from airlines.models import Airline, Review


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class AirlineSerializer(ModelSerializer):
    class Meta:
        model = Airline
        fields = '__all__'


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
