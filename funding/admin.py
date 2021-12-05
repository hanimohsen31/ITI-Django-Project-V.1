from django.contrib import admin

# Register your models here.
from .models import Funding, Category, Project_comments, Project_pics, InAppropriateProject

admin.site.register(Funding)
admin.site.register(Category)
admin.site.register(Project_comments)
admin.site.register(InAppropriateProject)
