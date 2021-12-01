from django.db import models
from user.models import User

# Create your models here.

Category = (
    ('Short Term', 'Short Term'),
    ('Long Term', 'Long Term')
)


class Funding(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=Category)
    details = models.TextField(default='')
    target = models.IntegerField(default=0)
    # start = models.DateTimeField(null=True)
    # end = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='fundings/')
    current_donation = models.IntegerField(default=0)
    commentinitial = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    connect = models.ForeignKey(Funding, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.comment
