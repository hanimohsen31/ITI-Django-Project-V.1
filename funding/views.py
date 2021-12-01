from django.shortcuts import render
from django.shortcuts import render
from .models import Funding


# Create your views here.
def funding_list(request):
    funding_list = Funding.objects.all()
    context = {'funding_list': funding_list}
    return render(request, 'funding/funding_list.html', context)


def funding_details(request,id):
    funding_details = Funding.objects.get(id=id)
    context = {'funding_details': funding_details}
    return render(request, 'funding/funding_details.html', context)
