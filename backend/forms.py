from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Attractions, Restaurants, Apartments, About_PageTitle, About_PresentationText, About_TeamTitle, About_MemberOne, About_MemberTwo, About_MemberThree, Contact_Header, Contact_Information, Contact_Address, House_User

# class PostNewHouse(forms.ModelForm):
#     # content = forms.CharField(widget=CKEditorUploadingWidget())
#     # Reminder: add some extra requirement before meta?
#     class Meta:
#         model = House_Creation
#         fields = ('title', 'description', 'city', 'price')

class PostHouse(forms.ModelForm):

    class Meta:
        model = House_User
        fields = ('title', 'description', 'city', 'price')

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    postal = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'location', 'postal', 'email', 'password1', 'password2', )

class PostAttraction(forms.ModelForm):

    class Meta:
        model = Attractions
        fields = ('title', 'text',)

class PostRestaurant(forms.ModelForm):

    class Meta:
        model = Restaurants
        fields = ('title', 'text',)

class PostApartment(forms.ModelForm):

    class Meta:
        model = Apartments
        fields = ('title', 'text',)

class PostAboutTitle(forms.ModelForm):

    class Meta:
        model = About_PageTitle
        fields = ('title',)

class PostAboutPresentation(forms.ModelForm):

    class Meta:
        model = About_PresentationText
        fields = ('title', 'text',)

class PostAboutTeamTitle(forms.ModelForm):

    class Meta:
        model = About_TeamTitle
        fields = ('title',)

class PostAboutMemberOne(forms.ModelForm):

    class Meta:
        model = About_MemberOne
        fields = ('title', 'text',)

class PostAboutMemberTwo(forms.ModelForm):

    class Meta:
        model = About_MemberTwo
        fields = ('title', 'text',)

class PostAboutMemberThree(forms.ModelForm):

    class Meta:
        model = About_MemberThree
        fields = ('title', 'text',)

class PostContactHeader(forms.ModelForm):

    class Meta:
        model = Contact_Header
        fields = ('title', 'text',)

class PostContactInformation(forms.ModelForm):

    class Meta:
        model = Contact_Information
        fields = ('title', 'text',)

class PostContactAddress(forms.ModelForm):

    class Meta:
        model = Contact_Address
        fields = ('title', 'text',)
