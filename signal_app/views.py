from django.shortcuts import render
from .forms import ProfileForm,UserForm

def register(request):
    if request.method =="POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit= False)
            profile.user = user
            profile.save()
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request,'signal_app/registration_form.html',{'user_form':user_form,'profile_form':profile_form})