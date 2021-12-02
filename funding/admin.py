from django.contrib import admin

# Register your models here.
from .models import Funding,Category
admin.site.register(Funding)
admin.site.register(Category)
