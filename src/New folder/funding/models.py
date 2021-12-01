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
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    # pictures = models.FileField(upload_to='../src/uploads')
    # check on_delete condition
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # still need rate check
    # rate = models.Count()
    # funding_comment = models.ForeignKey('Comment', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#
# class Comment(models.Model):
#     comment = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.comment
