from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
# from funding.models import Funding


class Profile(models.Model):
    # uid = models.AutoField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    uemail = models.EmailField()
    upassword = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='profile/')
    # project = models.ForeignKey('Funding', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)

## create new user ---> create new empty profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)