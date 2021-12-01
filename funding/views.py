from django.shortcuts import render
from django.shortcuts import render
from .models import Funding
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
def funding_list(request):
    funding_list = Funding.objects.all()

    paginator = Paginator(funding_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'funding_list': funding_list, 'listlength': funding_list}
    return render(request, 'funding/funding_list.html', context)


def funding_details(request,id):
    funding_details = Funding.objects.get(id=id)
    context = {'funding_details': funding_details}
    return render(request, 'funding/funding_details.html', context)
