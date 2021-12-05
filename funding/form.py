from django import forms
from .models import Funding, Project_pics, Reports, Project_donations, Project_comments, InAppropriateProject
# from django.forms import ModelForm
import datetime
from django import forms
from django.forms import Select
from django.core.exceptions import ValidationError
from django import forms


class FundingForm(forms.ModelForm):
    class Meta:
        model = Funding
        # fields = '__all__'
        fields = ['title', 'project_tags', 'category', 'details', 'target', 'end', 'image']

        exclude = ['rating']
        # widgets = {'user': forms.HiddenInput()}


class Report(forms.ModelForm):
    class Meta:
        model = InAppropriateProject
        fields = ('body',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Project_comments
        fields = ('comment',)


class DonateForm(forms.ModelForm):
    donation = forms.IntegerField(min_value=1)

    class Meta:
        model = Project_donations
        fields = ('donation',)


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Project_pics
        fields = ('image',)
