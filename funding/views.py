from django.shortcuts import render
from django.shortcuts import render
from .models import Funding
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse

from django.core.paginator import Paginator
from django.shortcuts import render
from .form import FundingForm

# Create your views here.
def funding_list(request):
    funding_list = Funding.objects.all()

    paginator = Paginator(funding_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'funding_list': page_obj, 'listlength': funding_list}
    return render(request, 'funding/funding_list.html', context)

#
# def funding_details(request, id):
#     funding_details = Funding.objects.get(id=id)
#     context = {'funding_details': funding_details}
#     return render(request, 'funding/funding_details.html', context)


def funding_details(request, id):
    funding_detail = Funding.objects.get(id=id)
    if request.method == 'POST':
        form = FundingForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = funding_detail
            myform.save()
        pass
    else:
        form = FundingForm()
    context = {'funding_detail': funding_detail, 'form': form}
    return render(request, 'funding/funding_details.html', context)


def addfunding(request):
    if request.method == 'POST':
        form = FundingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('funding:home'))
        pass
    else:
        form = FundingForm()
    return render(request, 'funding/funding_add.html', {'form': form})


# def addcomment(request):
#     if request.method == 'POST':
#         commentform = CommentForm(request.POST)
#         if commentform.is_valid():
#             commentform.save()
#             return redirect(reverse('funding:home'))
#         pass
#     else:
#         commentform = CommentForm()
#     return render(request, 'funding/funding_details.html', {'commentform': commentform})