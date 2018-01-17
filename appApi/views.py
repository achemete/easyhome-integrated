from django.shortcuts import render
from appApi.serializers import UsersSerializer, AccomodationsSerializer,ReviewsSerializer,ServicesSerializer,AttractionsSerializer,RestaurantSerializer,DealSerializer
from rest_framework import viewsets
from appApi.models import Users,Reviews,Accomodations,Services,Attractions,Restaurant,Deal
import backend
from backend.models import *

class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

"""import django_filters.rest_framework"""
from rest_framework import generics

from django.views.generic import ListView

# class AccomodationsListView(ListView):
#     model = Accomodations
#     template_name = 'frontend/templates/frontend/index.html'
#     context_object_name = 'accomodations'

def AccomodationsListView(request):
	restaurants = Restaurants.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	attractions = Attractions.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	apartments = Apartments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	accomodations = Accomodations.objects.all()
	return render(request, 'appApi/accomodations_list.html', {'restaurants': restaurants, 'attractions': attractions, 'apartments':apartments, 'accomodations':accomodations})

class ReviewsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
class AccomodationsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Accomodations.objects.all()
    serializer_class = AccomodationsSerializer
# Create your views here.

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class AttractionsViewSet(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionsSerializer

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
