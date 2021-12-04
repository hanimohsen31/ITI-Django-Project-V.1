import django_filters
from .models import Funding

class FundingFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Funding
        fields = ['title', 'category',]