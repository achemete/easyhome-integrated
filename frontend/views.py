# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect, render, get_object_or_404

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

import backend
from backend.models import *
from appApi.models import Accomodations, Restaurant, Attractions


####
## frontend Views
####


from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

def listAllAttractions(request):
    attractions = Attractions.objects.all()
    return render(request, 'frontend/listAllA.html',{"attractions":attractions})

def listAllAccomodations(request):
    accomodations = Accomodations.objects.all()
    return render(request, 'frontend/listAll.html',{"accomodations":accomodations})

def listAllRestaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'frontend/listAllR.html',{"restaurants":restaurants})

def single(request):
    id  = request.GET.get('id', '')
    accomodations = Accomodations.objects.all()
    return render(request,'frontend/single.html',{"id":id,"accomodations":accomodations})

def singleR(request):
    id  = request.GET.get('id', '')
    restaurants = Restaurant.objects.all()
    return render(request,'frontend/single_restaurant.html',{"id":id,"restaurants":restaurants})

def singleA(request):
    id  = request.GET.get('id', '')
    attractions = Attractions.objects.all()
    return render(request,'frontend/single_attraction.html',{"id":id,"attractions":attractions})

def pageform(request):
    name = request.GET.get('name', '')
    accomodations = Accomodations.objects.all()
    return render(request, 'frontend/list.html',{"name" : name, "accomodations":accomodations})

def pageformR(request):
    name = request.GET.get('name', '')
    restaurants = Restaurant.objects.all()
    return render(request, 'frontend/listR.html',{"name" : name, "restaurants":restaurants})

def pageformA(request):
    name = request.GET.get('name', '')
    attractions = Attractions.objects.all()
    return render(request, 'frontend/listA.html',{"name" : name, "attractions":attractions})

# class AccomodationsListView(ListView):
#     model = Accomodations
#     template_name = 'frontend/home.html'
#     context_object_name = 'accomodations'

def frontend_home(request):
	restaurants = Restaurants.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	attractions = Attractions.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	apartments = Apartments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'frontend/home.html', {'restaurants': restaurants, 'attractions': attractions, 'apartments':apartments})

def frontend_about(request):
	pageTitles = About_PageTitle.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	presentations = About_PresentationText.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	teams = About_TeamTitle.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	memberones = About_MemberOne.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	membertwos = About_MemberTwo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	memberthrees = About_MemberThree.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'frontend/about.html', {'pageTitles': pageTitles, 'presentations': presentations, 'teams':teams, 'memberones':memberones, 'membertwos':membertwos, 'memberthrees':memberthrees})

def frontend_home(request):
	restaurants = Restaurants.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	attractions = Attractions.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	apartments = Apartments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'frontend/home.html', {'restaurants': restaurants, 'attractions': attractions, 'apartments':apartments})

def frontend_about(request):
	pageTitles = About_PageTitle.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	presentations = About_PresentationText.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	teams = About_TeamTitle.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	memberones = About_MemberOne.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	membertwos = About_MemberTwo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	memberthrees = About_MemberThree.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'frontend/about.html', {'pageTitles': pageTitles, 'presentations': presentations, 'teams':teams, 'memberones':memberones, 'membertwos':membertwos, 'memberthrees':memberthrees})

def frontend_contact(request):
	headers = Contact_Header.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	informations = Contact_Information.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	addresses = Contact_Address.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'frontend/contact.html', {'headers': headers, 'informations': informations, 'addresses':addresses})

class ProfilePageView(TemplateView):
 	template_name = "frontend/profile.html"

class LogoutPageView(TemplateView):
 	template_name = "registration/logged_out.html"
