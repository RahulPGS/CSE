from django import forms
from . import models
from django.forms import Textarea


class Faculty_form(forms.ModelForm):
    class Meta:
        model = models.Faculty
        exclude = {}

class Staff_form(forms.ModelForm):
    class Meta:
        model = models.Staff
        exclude = {}


class Event_form(forms.ModelForm):
    class Meta:
        model = models.Events
        exclude = {}

class A_cal_form(forms.ModelForm):
    class Meta:
        model = models.Timetablenacedemics
        exclude = {}

class publication_form(forms.ModelForm):
    class Meta:
        model = models.Publication
        exclude = {}

class gallery_form(forms.ModelForm):
    class Meta:
        model = models.Gallery
        fields = ['category', 'name']

class GalleryImage(gallery_form()):
     images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

     class Meta(gallery_form.Meta):
         fields = gallery_form.Meta.fields + ['images',]

class news_form(forms.ModelForm):
    class Meta:
        model = models.News
        exclude = {}

class slide_form(forms.ModelForm):
    class Meta:
        model = models.Slide
        exclude = {}
    
class award_form(forms.ModelForm):
    class Meta:
        model = models.Award
        exclude = {}


class batch_form(forms.ModelForm):
    class Meta:
        model = models.Batch
        exclude = {}

class placement_form(forms.ModelForm):
    class Meta:
        model = models.Placement
        exclude = {}

class internship_form(forms.ModelForm):
    class Meta:
        model = models.Internship
        exclude = {}

class collaboration_form(forms.ModelForm):
    class Meta:
        model = models.Collaboration
        exclude = {}

class message_form(forms.ModelForm):
    class Meta:
        model = models.Message
        exclude = {}