from django.db.models.query import QuerySet
from django.forms.models import modelformset_factory
from django.shortcuts import render
from django.shortcuts import render
from .models import Funding, Project_comments, Project_pics, images
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import FundingForm, CommentForm
from taggit.models import Tag
from .filters import FundingFilter

# Create your views here.


def funding_list(request):
    funding_list = Funding.objects.all()

    myfilter = FundingFilter(request.GET, queryset=funding_list)
    funding_list = myfilter.qs

    paginator = Paginator(funding_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'funding_list': page_obj, 'listlength': funding_list ,'myfilter':myfilter}
    return render(request, 'funding/funding_list.html', context)


def home(request):

    top5 = Funding.objects.all().order_by('-rating')[0:5]
    least5 = Funding.objects.all().order_by('rating')[0:5]
    fundings5 = Funding.objects.all()[0:5]

    funding_all = Funding.objects.all()


    funding_list = Funding.objects.all()
    myfilter = FundingFilter(request.GET, queryset=funding_list)
    funding_list = myfilter.qs

    context = {'top5': top5, 'least5': least5, 'fundings5': fundings5, 'myfilter': myfilter , 'funding_list':funding_list, 'funding_all':funding_all}
    return render(request, 'funding/home.html', context)


def funding_details(request, id):
    funding_detail = Funding.objects.get(id=id)
    fund_form = FundingForm(request.POST or None, request.FILES, instance=funding_detail)
    comments=Project_comments.objects.filter(project_id=id)
    new_comment = None
    if request.method == 'POST':
        if fund_form.is_valid():
            myform = fund_form.save(commit=False)
            myform.job = funding_detail
            myform.save()
            for file in request.FILES.getlist('images'):
                Project_pics(project=fund_form.instance, pic=file).save()

        # ########################To Add Comments##############################        
        commentform = CommentForm(data=request.POST)
        if commentform.is_valid():  
            # Create Comment object but don't save to database yet          
            new_comment = commentform.save(commit=False)
            # Assign the current post to the comment
            new_comment.project = funding_detail
            # Save the comment to the database
            new_comment.save()
            commentform = CommentForm()
    else:
        commentform = CommentForm()
        
    imgs = Project_pics.objects.filter(project_id=id)
    context = {'funding_detail': funding_detail, 'fund_form': fund_form, 'commentform': commentform,'new_comment':new_comment,'comments':comments, 'images': imgs}
    return render(request, 'funding/funding_details.html', context)


def addfunding(request):
    if request.method == 'POST':
        form = FundingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            for file in request.FILES.getlist('images'):
                Project_pics(project=form.instance, pic=file).save()

            return redirect(reverse('funding:home'))

    else:
        form = FundingForm()
    return render(request, 'funding/funding_add.html', {'form': form})
    pass


# def filter_title(request, title):
#     funding_list = Funding.objects.filter(title=title)
#     paginator = Paginator(funding_list, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {'funding_list': page_obj, 'listlength': funding_list}
#     return render(request, 'funding/filter_title.html', context)
#
#
# def filter_category(request, category):
#     funding_list = Funding.objects.filter(category=category)
#     paginator = Paginator(funding_list, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     context = {'funding_list': page_obj, 'listlength': funding_list}
#     return render(request, 'funding/filter_title.html', context)
