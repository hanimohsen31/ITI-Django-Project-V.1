from django.db.models.query import QuerySet
from django.shortcuts import render
from django.shortcuts import render
from .models import Funding, Project_comments, Project_pics
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import FundingForm,CommentForm
from taggit.models import Tag

# Create your views here.


def funding_list(request):
    funding_list = Funding.objects.all()

    paginator = Paginator(funding_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'funding_list': page_obj, 'listlength': funding_list}
    return render(request, 'funding/funding_list.html', context)




def funding_details(request, id):
    funding_detail = Funding.objects.get(id=id)
    comments=Project_comments.objects.filter(project_id=id)
    new_comment = None
    if request.method == 'POST':
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
        
    imgs = Project_pics.objects.filter(project_id=id)
    context = {
        'funding_detail': funding_detail,
        'commentform': commentform,
        'new_comment':new_comment,
        'comments':comments, 
        'images': imgs}
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


