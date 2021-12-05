from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
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

@login_required(login_url='login')
def funding_list(request):
    funding_list = Funding.objects.all()
    myfilter = FundingFilter(request.GET, queryset=funding_list)
    funding_list = myfilter.qs
    paginator = Paginator(funding_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'funding_list': page_obj, 'listlength': funding_list, 'myfilter': myfilter}
    return render(request, 'funding/funding_list.html', context)


@login_required(login_url='login')
def home(request):
    top5 = Funding.objects.all().order_by('-rating')[0:5]
    least5 = Funding.objects.all().order_by('rating')[0:5]
    fundings5 = Funding.objects.all()[0:5]
    funding_all = Funding.objects.all()
    funding_list = Funding.objects.all()
    myfilter = FundingFilter(request.GET, queryset=funding_list)
    funding_list = myfilter.qs

    context = {'top5': top5, 'least5': least5, 'fundings5': fundings5, 'myfilter': myfilter,
               'funding_list': funding_list, 'funding_all': funding_all}
    return render(request, 'funding/home.html', context)

@login_required(login_url='login')
def funding_details(request, id):
    funding_detail = Funding.objects.get(id=id)
    new_comment = None
    message = None
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
                message = "Sorry you can not add donations that greater than the target"
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
    comments = Project_comments.objects.filter(project_id=id)
    donations = Project_donations.objects.filter(project_id=id).aggregate(Sum('donation'))['donation__sum']
    imgs = Project_pics.objects.filter(project_id=id)
    context = {
        'funding_detail': funding_detail,
        'donateform': donateform,
        'commentform': commentform,
        'new_comment': new_comment,
        'donations': donations,
        'comments': comments,
        'message': message,
        'images': imgs}
    return render(request, 'funding/funding_details.html', context)

@login_required(login_url='login')
def check_target(project_id, new_donation):
    do1 = Project_donations.objects.filter(project_id=project_id).aggregate(Sum('donation'))['donation__sum']
    if (do1):
        donations = do1 + int(new_donation)
    else:
        do1 = 0
        donations = do1 + int(new_donation)

    funding_target = Funding.objects.get(id=project_id).target
    if funding_target >= donations:
        return True
    return False

@login_required(login_url='login')
def addfunding(request):
    if request.method == 'POST':
        form = FundingForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            for file in request.FILES.getlist('images'):
                Project_pics(project=form.instance, pic=file).save()
            return redirect(reverse('funding:home'))
    else:
        form = FundingForm()
    return render(request, 'funding/funding_add.html', {'form': form})
    pass

@login_required(login_url='login')
def contacts(request):
    return render(request, 'funding/contacts.html', {})

@login_required(login_url='login')
def confirm_cancel(request, id):
    donations = Project_donations.objects.filter(project_id=id).aggregate(Sum('donation'))['donation__sum']
    if donations is None:
        donations = 0
    funding_target = Funding.objects.get(id=id).target
    over25 = (donations / funding_target) * 100
    return render(request, 'funding/confirm_cancel.html', {'id': id, 'over25': over25})

@login_required(login_url='login')
def cancel_project(request, id ):
    Funding.objects.get(id=id,user=request.user).delete()

    return redirect(reverse('funding:home'))
