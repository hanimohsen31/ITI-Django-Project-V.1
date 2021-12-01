from django import forms
from .models import Funding, Comment


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = '__all__'


class FundingForm(forms.ModelForm):
    class Meta:
        model = Funding
        fields = '__all__'
        # fields = ['title', 'job_type', 'description', 'description', 'vacancy', 'salary', 'category', 'experience']
