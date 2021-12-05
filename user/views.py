from collections import UserDict
from django.shortcuts import redirect, render

from funding.models import Funding
from .forms import Profileform, SignupForm, Userform 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from django.urls import reverse
# activate#
from django.views import View
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.sites.shortcuts import get_current_site
#end activate#

# Create your views here.
def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            #  no understand for next line#
            user = form.save(commit=False)
            # user.image = request.FILES['image']
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username,password=password)
            mail_subject = 'Activate your account.'
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = account_activation_token.make_token(user)
            activation_link = "{0}{1}{2}{3}/{4}".format("http://",current_site,"/accounts/activate/", uid, token)
            # print(activation_link)
            # print(user.first_name)
            # print(user.last_name)
            # print(user.id)
            message = "Hello {0},\n {1}".format(user.first_name + " " + user.last_name, activation_link)
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
            # login(request,user)
        return redirect('login')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    projects = Funding.objects.filter(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile,'projects':projects})
    # return render(request,'accounts/profile.html')



def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform = Userform(request.POST,instance=request.user)
        profileform = Profileform(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else :
        userform = Userform(instance=request.user)
        profileform = Profileform(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})

def warn(request):
    context = {
        'cancel': 'accounts:my_profile',
        'delete': 'accounts:delete_account',
        'msg': 'Are you sure you want to delete your account ? All your projects and donations will be deleted',

    }
    return render(request, 'accounts/warn.html', context)

def delete(request):
    user = User.objects.get(id=request.user.id);
    logout(request)
    user.delete()
    return redirect( reverse('login'))


class Activate(View):
    def get(self, request, uid, token):
        try:
            uid = force_text(urlsafe_base64_decode(uid))
            print(uid)
            user = User.objects.get(id=uid)
            print(user)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            # activate user and login:
            user.is_active = True
            print(user.is_active)
            user.save()
            return redirect(reverse('login'))

        else:
            return HttpResponse('Activation link is invalid!')

    # def post(self, request):
    #     form = PasswordChangeForm(request.user, request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         update_session_auth_hash(request, user)  # Important, to update the session with the new password
    #         return HttpResponse('Password changed successfully')
