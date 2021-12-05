from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify


# Create your models here.
class Category (models.Model):
    cat_name = models.CharField(max_length=25)

    def __str__(self):
        return self.cat_name   


# fund ==> app
# project ==> project
class Funding(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name='funding')
    title = models.CharField(max_length=20)
    # tags
    project_tags = TaggableManager()
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    details = models.TextField(default='')
    target = models.IntegerField(default=0)
    start = models.DateField(auto_now=True)
    end = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to='fundings/')
    rating = models.FloatField(null=True, default=0)
   

    def __str__(self):
        return self.title


# Donations
class Project_donations(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name='Project_donations')
    project = models.ForeignKey(Funding, null=True, on_delete=models.CASCADE,related_name='Project_donations')
    donation = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Rating
class Project_rating(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Funding, null=True, on_delete=models.CASCADE)
    rating = models.FloatField()


# comments
class Project_comments(models.Model):
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    project = models.ForeignKey(Funding, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment


# Reports
class Reports(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    project = models.ForeignKey(Funding, null=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Project_comments, null=True, on_delete=models.CASCADE)
    report = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.report


# Multiple images
def get_image_name(instance, filename):
    title = instance.project.title
    slug = slugify(title)
    return "projects/images/%s-%s" % (slug, filename)


@property
def images(self):
    return Project_pics.objects.filter(project_id=self.id)


class Project_pics(models.Model):
    project = models.ForeignKey('Funding', null=True, on_delete=models.CASCADE)
    pic = models.ImageField(upload_to=get_image_name, verbose_name='Project Image')

    def __str__(self):
        return str(self.pic)



class InAppropriateProject(models.Model):
    project = models.ForeignKey(Funding, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
