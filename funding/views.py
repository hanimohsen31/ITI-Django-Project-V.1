from django.db.models.query import QuerySet
from django.shortcuts import render
from django.shortcuts import render
from .models import Funding, Project_comments, Project_donations, Project_pics
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import FundingForm, CommentForm, DonateForm
from taggit.models import Tag
from .filters import FundingFilter
from django.db.models import Sum

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
    new_comment = None
    message=None
    if request.method == 'POST':
        # ######################## To Add Comments ##############################        
        donateform = DonateForm(data=request.POST)
        if donateform.is_valid():  
            
            if check_target(funding_detail.id, donateform['donation'].data):
                # Create Comment object but don't save to database yet          
                new_donate = donateform.save(commit=False)
                # Assign the current post to the comment
                new_donate.project = funding_detail
                # Save the comment to the database
                new_donate.save()
                donateform = DonateForm()
            else:
                message="Sorry you can not add donations that greater than the target"
        # ######################## To Add Comments ##############################        
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
        donateform = DonateForm()
    comments=Project_comments.objects.filter(project_id=id)
    donations=Project_donations.objects.filter(project_id=id).aggregate(Sum('donation'))['donation__sum']   
    imgs = Project_pics.objects.filter(project_id=id)
    context = {
        'funding_detail': funding_detail,
        'donateform':donateform,
        'commentform': commentform,
        'new_comment':new_comment,
        'donations':donations,
        'comments':comments, 
        'message':message,
        'images': imgs}
    return render(request, 'funding/funding_details.html', context)
def check_target(project_id,new_donation):

    donations=Project_donations.objects.filter(project_id=project_id).aggregate(Sum('donation'))['donation__sum']+int(new_donation)   
    funding_target = Funding.objects.get(id=project_id).target
    print(donations)
    print(funding_target)
    if funding_target >= donations:
        return True
    return False

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


def contacts(request):
    return render(request, 'funding/contacts.html', {})

