from django.shortcuts import render
from .models import Task, Project1, Project2, Lab
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from accounts.models import Profile

@login_required
def tasks_list(request):
    data = { 'contest_published' : Task.objects.filter(task_type='1')[0].publish,
             'contest_link' : Task.objects.filter(task_type='1')[0].description_link,
             'contest_deadline' : Task.objects.filter(task_type='1')[0].deadline,

             'project_1_info' : Task.objects.filter(task_type='2')[0],
             'project_1_passed': len(Project1.objects.filter(user_id=request.user.id)) == 0,
             'project_1' : Project1.objects.filter(user_id=request.user.id)[0] if (len(Project1.objects.filter(user_id=request.user.id)) != 0) else '',

             'project_2_info': Task.objects.filter(task_type='3')[0],
             'project_2_passed': len(Project2.objects.filter(user_id=request.user.id)) == 0,
             'project_2': Project2.objects.filter(user_id=request.user.id)[0] if (
                         len(Project2.objects.filter(user_id=request.user.id)) != 0) else '',

             'project_lab_info': Task.objects.filter(task_type='4')[0],
             'project_lab_passed': len(Lab.objects.filter(user_id=request.user.id)) == 0,
             'project_lab': Lab.objects.filter(user_id=request.user.id)[0] if (
                     len(Lab.objects.filter(user_id=request.user.id)) != 0) else '',



             'lab_published': Task.objects.filter(task_type='4')[0].publish,
             'lab_link': Task.objects.filter(task_type='4')[0].description_link,
             'lab_deadline': Task.objects.filter(task_type='4')[0].deadline,
             }
    return render(request,
                  'tasks/tasks.html',
                  context=data,
                  )

@login_required
def create_1(request):
    if request.method == 'POST':
        project = Project1()
        user_profile = Profile.objects.get(user=request.user)
        project.user_id = request.user.id
        project.user_name = user_profile.last_name + ' ' + user_profile.first_name
        project.checker = user_profile.checker
        project.link = request.POST.get('link_1')
        project.save()
    return HttpResponseRedirect('/tasks/')


@login_required
def update_field_1(request):
    if request.method == 'POST':
        user_id = request.user.id
        obj = Project1.objects.filter(user_id=user_id)[0]
        print(obj)
        obj.status = "Сhecking"  # измените на нужное значение
        obj.save()
    return HttpResponseRedirect('/tasks/')

def create_2(request):
    if request.method == 'POST':
        project = Project2()
        user_profile = Profile.objects.get(user=request.user)
        project.user_id = request.user.id
        project.user_name = user_profile.last_name + ' ' + user_profile.first_name
        project.checker = user_profile.checker
        project.link = request.POST.get('link_2')
        project.save()
    return HttpResponseRedirect('/tasks/')


@login_required
def update_field_2(request):
    if request.method == 'POST':
        user_id = request.user.id
        obj = Project2.objects.filter(user_id=user_id)[0]
        print(obj)
        obj.status = "Сhecking"  # измените на нужное значение
        obj.save()
    return HttpResponseRedirect('/tasks/')

def create_lab(request):
    if request.method == 'POST':
        project = Lab()
        user_profile = Profile.objects.get(user=request.user)
        project.user_id = request.user.id
        project.user_name = user_profile.last_name + ' ' + user_profile.first_name
        project.checker = user_profile.checker
        project.link = request.POST.get('link_lab')
        project.save()
    return HttpResponseRedirect('/tasks/')


@login_required
def update_field_lab(request):
    if request.method == 'POST':
        user_id = request.user.id
        obj = Lab.objects.filter(user_id=user_id)[0]
        print(obj)
        obj.status = "Сhecking"  # измените на нужное значение
        obj.save()
    return HttpResponseRedirect('/tasks/')