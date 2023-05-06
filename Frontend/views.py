from django.shortcuts import  render, HttpResponseRedirect
from .forms import *
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'index.html')
    
# end def

def add_skills(request):
    if request.user.is_authenticated:
        skills_data = Skills.Skill_obj.all()
        if request.method == 'POST':
            
            form = SkillsForm(request.POST)
            if form.is_valid():
                skill_name = form.cleaned_data['skill_name']
                skill_grip = form.cleaned_data['skill_grip_value']
                data = Skills(skill_name=skill_name,grip_value=skill_grip, user_skills = request.user)
                data.save()
                messages.success(request,'Data saved successfully')
                skills_data = Skills.Skill_obj.filter(user_skills = request.user).all()
            else:
                messages.error(request,'Invalid Data entered!',extra_tags='danger')
                form = SkillsForm()
            return render(request,'skills.html',{'form':form,'skills_data': skills_data})
        else:
            form = SkillsForm()
        return render(request,'skills.html',{'form':form,'skills_data':skills_data})
    else:
        messages.error('You are not Authorized to access this page!')
    return HttpResponseRedirect('/auth/login/')