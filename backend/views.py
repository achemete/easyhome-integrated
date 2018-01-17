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

from django.views.generic import TemplateView

import frontend

from .models import * #Attractions, Restaurants, Apartments
from .forms import * #PostRestaurant, PostAttraction, PostApartment

####
## Backend Views
####

class OperationsPageView(TemplateView):
	template_name = "backend/operations.html"

# class backend_ops_landing_PageView(TemplateView):
# 	template_name = "backend/backend_ops_landing.html"

# class backend_ops_contact_PageView(TemplateView):
# 	template_name = "backend/backend_ops_contact.html"

# class backend_ops_about_PageView(TemplateView):
# 	template_name = "backend/backend_ops_about.html"

# class backend_ops_deals_PageView(TemplateView):
# 	template_name = "backend/backend_ops_deals.html"

class backend_ops_restaurants_PageView(TemplateView):
	template_name = "backend/backend_ops_restaurants.html"

class backend_ops_attractions_PageView(TemplateView):
	template_name = "backend/backend_ops_attractions.html"

class backend_ops_apartments_PageView(TemplateView):
	template_name = "backend/backend_ops_apartments.html"

def backend_home(request):
	return render(request, 'backend/back_end_home.html')

def backend_ops_landing(request):
	restaurants = Restaurants.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	attractions = Attractions.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	apartments = Apartments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'backend/backend_ops_landing.html', {'restaurants': restaurants, 'attractions': attractions, 'apartments':apartments})

def backend_ops_about(request):
	titles = About_PageTitle.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	presentations = About_PresentationText.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	teams = About_TeamTitle.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	memberones = About_MemberOne.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	membertwos = About_MemberTwo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	memberthrees = About_MemberThree.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'backend/backend_ops_about.html', {'titles': titles, 'presentations': presentations, 'teams':teams, 'memberones':memberones, 'membertwos':membertwos, 'memberthrees':memberthrees})

def backend_ops_contact(request):
	headers = Contact_Header.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	informations = Contact_Information.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	addresses = Contact_Address.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'backend/backend_ops_contact.html', {'headers': headers, 'informations': informations, 'addresses':addresses})

def backend_ops_apartments(request):
	apartments = House_User.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'backend/backend_ops_apartments.html', {'apartments': apartments})

def landing_new_restaurant(request):
	if request.method == "POST":
		form = PostRestaurant(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_restaurant_detail', pk=section.pk)
	else:
		form = PostRestaurant()
	return render(request, 'backend/landing_restaurant_new.html', {'form': form})

def landing_new_attraction(request):
	if request.method == "POST":
		form = PostAttraction(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_attraction_detail', pk=section.pk)
	else:
		form = PostAttraction()
	return render(request, 'backend/landing_attraction_new.html', {'form': form})

def landing_new_apartment(request):
	if request.method == "POST":
		form = PostApartment(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_apartment_detail', pk=section.pk) ### add app backend
	else:
		form = PostApartment()
	return render(request, 'backend/landing_apartment_new.html', {'form': form})

def landing_restaurant_detail(request, pk):
	section = get_object_or_404(Restaurants, pk=pk)
	return render(request, 'backend/landing_restaurant_detail.html', {'section': section})

def landing_attraction_detail(request, pk):
	section = get_object_or_404(Attractions, pk=pk)
	return render(request, 'backend/landing_attraction_detail.html', {'section': section})

def landing_apartment_detail(request, pk):
	section = get_object_or_404(Apartments, pk=pk)
	return render(request, 'backend/landing_apartment_detail.html', {'section': section})

def landing_restaurant_edit(request, pk):
	section = get_object_or_404(Restaurants, pk=pk)
	if request.method == "POST":
		form = PostRestaurant(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_restaurant_detail', pk=section.pk)
	else:
		form = PostRestaurant(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def landing_attraction_edit(request, pk):
	section = get_object_or_404(Attractions, pk=pk)
	if request.method == "POST":
		form = PostAttraction(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_attraction_detail', pk=section.pk)
	else:
		form = PostAttraction(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def landing_apartment_edit(request, pk):
	section = get_object_or_404(Apartments, pk=pk)
	if request.method == "POST":
		form = PostApartment(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:landing_apartment_detail', pk=section.pk)
	else:
		form = PostApartment(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def landing_restaurant_remove(request, pk):
	restaurants = get_object_or_404(Restaurants, pk=pk)
	restaurants.delete()
	return redirect('backend:backend_ops_landing')

def landing_attraction_remove(request, pk):
	attractions = get_object_or_404(Attractions, pk=pk)
	attractions.delete()
	return redirect('backend:backend_ops_landing')

def landing_apartment_remove(request, pk):
	apartments = get_object_or_404(Apartments, pk=pk)
	apartments.delete()
	return redirect('backend:backend_ops_landing')


def about_new_pageTitle(request):
	if request.method == "POST":
		form = PostAboutTitle(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_pageTitle_detail', pk=section.pk)
	else:
		form = PostAboutTitle()
	return render(request, 'backend/about_pageTitle_new.html', {'form': form})

def about_new_presentation(request):
	if request.method == "POST":
		form = PostAboutPresentation(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_presentation_detail', pk=section.pk)
	else:
		form = PostAboutPresentation()
	return render(request, 'backend/about_presentation_new.html', {'form': form})

def about_new_teamTitle(request):
	if request.method == "POST":
		form = PostAboutTeamTitle(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_teamTitle_detail', pk=section.pk)
	else:
		form = PostAboutTeamTitle()
	return render(request, 'backend/about_teamTitle_new.html', {'form': form})

def about_new_member1(request):
	if request.method == "POST":
		form = PostAboutMemberOne(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_memberOne_detail', pk=section.pk)
	else:
		form = PostAboutMemberOne()
	return render(request, 'backend/about_member1_new.html', {'form': form})

def about_new_member2(request):
	if request.method == "POST":
		form = PostAboutMemberTwo(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_memberTwo_detail', pk=section.pk)
	else:
		form = PostAboutMemberTwo()
	return render(request, 'backend/about_member2_new.html', {'form': form})

def about_new_member3(request):
	if request.method == "POST":
		form = PostAboutMemberThree(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_memberThree_detail', pk=section.pk)
	else:
		form = PostAboutMemberThree()
	return render(request, 'backend/about_member3_new.html', {'form': form})

def about_pageTitle_detail(request, pk):
	section = get_object_or_404(About_PageTitle, pk=pk)
	return render(request, 'backend/about_pageTitle_detail.html', {'section': section})

def about_presentation_detail(request, pk):
	section = get_object_or_404(About_PresentationText, pk=pk)
	return render(request, 'backend/about_presentation_detail.html', {'section': section})

def about_teamTitle_detail(request, pk):
	section = get_object_or_404(About_TeamTitle, pk=pk)
	return render(request, 'backend/about_teamTitle_detail.html', {'section': section})

def about_member1_detail(request, pk):
	section = get_object_or_404(About_MemberOne, pk=pk)
	return render(request, 'backend/about_member1_detail.html', {'section': section})

def about_member2_detail(request, pk):
	section = get_object_or_404(About_MemberTwo, pk=pk)
	return render(request, 'backend/about_member2_detail.html', {'section': section})

def about_member3_detail(request, pk):
	section = get_object_or_404(About_MemberThree, pk=pk)
	return render(request, 'backend/about_member3_detail.html', {'section': section})

def about_pageTitle_edit(request, pk):
	section = get_object_or_404(About_PageTitle, pk=pk)
	if request.method == "POST":
		form = PostAboutTitle(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_pageTitle_detail', pk=section.pk)
	else:
		form = PostAboutTitle(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

# create urls in url.py and change current ones
def about_presentation_edit(request, pk):
	section = get_object_or_404(About_PresentationText, pk=pk)
	if request.method == "POST":
		form = PostAboutPresentation(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_presentation_detail', pk=section.pk)
	else:
		form = PostAboutPresentation(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def about_teamTitle_edit(request, pk):
	section = get_object_or_404(About_TeamTitle, pk=pk)
	if request.method == "POST":
		form = PostAboutTeamTitle(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_teamTitle_detail', pk=section.pk)
	else:
		form = PostAboutTeamTitle(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def about_member1_edit(request, pk):
	section = get_object_or_404(About_MemberOne, pk=pk)
	if request.method == "POST":
		form = PostAboutMemberOne(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_memberOne_detail', pk=section.pk)
	else:
		form = PostAboutMemberOne(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def about_member2_edit(request, pk):
	section = get_object_or_404(About_MemberTwo, pk=pk)
	if request.method == "POST":
		form = PostAboutMemberTwo(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_memberTwo_detail', pk=section.pk)
	else:
		form = PostAboutMemberTwo(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def about_member3_edit(request, pk):
	section = get_object_or_404(About_MemberThree, pk=pk)
	if request.method == "POST":
		form = PostAboutMemberThree(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:about_memberThree_detail', pk=section.pk)
	else:
		form = PostAboutMemberThree(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def about_pageTitle_remove(request, pk):
	title = get_object_or_404(About_PageTitle, pk=pk)
	title.delete()
	return redirect('backend:backend_ops_about')

def about_presentation_remove(request, pk):
	title = get_object_or_404(About_PresentationText, pk=pk)
	title.delete()
	return redirect('backend:backend_ops_about')

def about_teamTitle_remove(request, pk):
	title = get_object_or_404(About_TeamTitle, pk=pk)
	title.delete()
	return redirect('backend:backend_ops_about')

def about_member1_remove(request, pk):
	title = get_object_or_404(About_MemberOne, pk=pk)
	title.delete()
	return redirect('backend:backend_ops_about')

def about_member2_remove(request, pk):
	title = get_object_or_404(About_MemberTwo, pk=pk)
	title.delete()
	return redirect('backend:backend_ops_about')

def about_member3_remove(request, pk):
	title = get_object_or_404(About_MemberThree, pk=pk)
	title.delete()
	return redirect('backend:backend_ops_about')

def contact_new_header(request):
	if request.method == "POST":
		form = PostContactHeader(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:contact_header_detail', pk=section.pk)
	else:
		form = PostContactHeader()
	return render(request, 'backend/contact_header_new.html', {'form': form})

def contact_new_information(request):
	if request.method == "POST":
		form = PostContactInformation(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:contact_information_detail', pk=section.pk)
	else:
		form = PostContactInformation()
	return render(request, 'backend/contact_information_new.html', {'form': form})

def contact_new_address(request):
	if request.method == "POST":
		form = PostContactAddress(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:contact_address_detail', pk=section.pk)
	else:
		form = PostContactAddress()
	return render(request, 'backend/contact_address_new.html', {'form': form})

def contact_header_detail(request, pk):
	section = get_object_or_404(Contact_Header, pk=pk)
	return render(request, 'backend/contact_header_detail.html', {'section': section})

def contact_information_detail(request, pk):
	section = get_object_or_404(Contact_Information, pk=pk)
	return render(request, 'backend/contact_information_detail.html', {'section': section})

def contact_address_detail(request, pk):
	section = get_object_or_404(Contact_Address, pk=pk)
	return render(request, 'backend/contact_address_detail.html', {'section': section})

def contact_header_edit(request, pk):
	section = get_object_or_404(Contact_Header, pk=pk)
	if request.method == "POST":
		form = PostContactHeader(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:contact_header_detail', pk=section.pk)
	else:
		form = PostContactHeader(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def contact_information_edit(request, pk):
	section = get_object_or_404(Contact_Information, pk=pk)
	if request.method == "POST":
		form = PostContactInformation(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:contact_information_detail', pk=section.pk)
	else:
		form = PostContactInformation(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def contact_address_edit(request, pk):
	section = get_object_or_404(Contact_Address, pk=pk)
	if request.method == "POST":
		form = PostContactAddress(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:contact_address_detail', pk=section.pk)
	else:
		form = PostContactAddress(instance=section)
	return render(request, 'backend/section_edit.html', {'form': form})

def contact_header_remove(request, pk):
	title = get_object_or_404(Contact_Header, pk=pk)
	title.delete()
	return redirect('backend:backend_ops_contact')

def contact_information_remove(request, pk):
	title = get_object_or_404(Contact_Information, pk=pk)
	title.delete()
	return redirect('backend:backend_ops_contact')

def contact_address_remove(request, pk):
	title = get_object_or_404(Contact_Address, pk=pk)
	title.delete()
	return redirect('backend:backend_ops_contact')

def house_create(request):
	if request.method == "POST":
		form = PostHouse(request.POST)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:house_details', pk=section.pk)
	else:
		form = PostHouse()
	return render(request, 'backend/house_create.html', {'form': form})

def house_details(request, pk):
	section = get_object_or_404(House_User, pk=pk)
	return render(request, 'backend/house_detail.html', {'section': section})

def house_edit(request, pk):
	section = get_object_or_404(House_User, pk=pk)
	if request.method == "POST":
		form = PostHouse(request.POST, instance=section)
		if form.is_valid():
			section = form.save(commit=False)
			section.author = request.user
			section.published_date = timezone.now()
			section.save()
			return redirect('backend:house_details', pk=section.pk)
	else:
		form = PostHouse(instance=section)
	return render(request, 'backend/house_edit.html', {'form': form})

def house_remove(request, pk):
	title = get_object_or_404(House_User, pk=pk)
	title.delete()
	return redirect('backend:operations')
	house_remove

def to_del_user(request):
	user = User.objects.all()
	return render(request, 'backend/staff_delete_users.html', {'user': user})

def staff_accounts_abuse(request):
	user = User.objects.all()
	return render(request, 'backend/staff_accounts_abuse.html', {'user': user})

@staff_member_required
def staff_ban_user(request, pk):
	user = User.objects.get(pk = pk)
	user.is_active = False
	user.save()
	#messages.success(request, 'Profile successfully banned.')
	return redirect('backend:staff_accounts_abuse')

@staff_member_required
def staff_unban_user(request, pk):
	user = User.objects.get(pk = pk)
	user.is_active = True
	user.save()
	#messages.success(request, 'Profile successfully unbanned.')
	return redirect('backend:staff_accounts_abuse')

@staff_member_required
def del_user(request, pk):
	try:
		user = User.objects.get(pk = pk)
		user.delete()
		#messages.sucess(request, "The user is deleted")

	except User.DoesNotExist:
		#messages.error(request, "User doesnot exist")
		return render(request, 'backend/operations.html')

	except Exception as e:
		return render(request, 'backend/operations.html',{'err':e.message})

	return render(request, 'backend/operations.html')

def staff_list(request):
	user = User.objects.all()
	return render(request, 'backend/staff_list_users.html', {'user': user})

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('frontend:frontend_home')
	else:
		form = SignUpForm()
	return render(request, 'frontend/signup.html', {'form': form})
