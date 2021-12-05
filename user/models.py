from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save ,pre_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

class ChildUser(User):
    pass

# Create your models here.
class Profile(models.Model):
    # uid = models.AutoField()
    user = models.OneToOneField(User, related_name="profile",on_delete=models.CASCADE)
    # mobile = models.CharField(max_length=15,null=True, blank=True)
    image = models.ImageField(upload_to='profile/', null=True , blank=True)
    phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$',
                                message="Phone number must match egyptian format")
    phone = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    face_regex = RegexValidator(regex='(?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?',
                                message='enter valid facebook profile url')
    facebook_profile = models.URLField(validators=[face_regex], blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    # is_active = models.BooleanField(_('active'), default=False,
    #     help_text=('Designates whether this user should be treated as '
    #                 'active. Unselect this instead of deleting accounts.'))

    def __str__(self):
        return str(self.user)
    
    # def check_profile_password(self, password):
    #     return self.user.check_password(password)

## create new user ---> create new empty profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance )

@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        print("Creating Inactive User")
        instance.is_active = False
    else:
        print("Updating User Record")