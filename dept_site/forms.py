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

class event_form(forms.ModelForm):
    class Meta:
        model = models.Events
        exclude = {}

class gallery_form(forms.ModelForm):
    class Meta:
        model = models.Gallery
        exclude = {}

class news_form(forms.ModelForm):
    class Meta:
        model = models.Notification
        exclude = {}
