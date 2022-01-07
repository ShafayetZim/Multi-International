from django import forms

from contact.models import Contact
from gallery.models import Gallery
from service.models import Service
from home.models import Feature, Slider, WorkingProcess
from about.models import About, Vision, Team, Choice


# ------contact-----
class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'location', 'mail1', 'mail2', 'phone1', 'phone2',)
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'mail1': forms.EmailInput(attrs={'class': 'form-control'}),
            'mail2': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone2': forms.TextInput(attrs={'class': 'form-control'}),
        }


# ------gallery------
class GalleryUpdateForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = (
            'title', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


class CreateGalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = (
            'title', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'rounded_list'}),
        }


# ------service------
class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'title', 'content', 'icon',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


# create service
class ServiceCreateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'title', 'content', 'icon',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


# ------home-----
class FeatureUpdateForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = (
            'right_title', 'description', 'icon',)
        widgets = {
            'right_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


class FeatureCreateForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = (
            'right_title', 'description', 'icon',)
        widgets = {
            'right_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


class WorkingProcessUpdateForm(forms.ModelForm):
    class Meta:
        model = WorkingProcess
        fields = (
            'title', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class WorkingProcessCreateForm(forms.ModelForm):
    class Meta:
        model = WorkingProcess
        fields = (
            'title', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SliderUpdateForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = (
            'image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


class SliderCreateForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = (
            'image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


# ------about------
class AboutUpdateForm(forms.ModelForm):
    class Meta:
        model = About
        fields = (
            'title', 'description', 'icon', 'shape')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded-list'}),
            'shape': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


class TeamUpdateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'name', 'position', 'pic',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'pic': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'name', 'position', 'pic',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'pic': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


class ChoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = (
            'title', 'description', 'icon',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


class ChoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = (
            'title', 'description', 'icon',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


class VisionUpdateForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = (
            'title', 'description', 'icon',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded-list'}),
        }


class VisionCreateForm(forms.ModelForm):
    class Meta:
        model = Vision
        fields = (
            'title', 'description', 'icon',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.FileInput(attrs={'class': 'rounded-list'}),
        }