from django.db import models


# Create your models here.
class User(models.Model):
    # uid = models.AutoField()
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    uemail = models.EmailField()
    upassword = models.CharField(max_length=20)
    mobile = models.IntegerField()

    def __str__(self):
        return self.fname

