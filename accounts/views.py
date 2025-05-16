from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, User
from .form import Profile, UpdateModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return HttpResponse('Hello world')


@login_required(login_url='/accounts/login')

def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()

    return render(request, 'profile.html', {'profile': profile})

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateModelForm(instance=profile)
    if request.method == "POST":
            form = UpdateModelForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile')

    return render(request, 'update_profile.html', {"form": form})





