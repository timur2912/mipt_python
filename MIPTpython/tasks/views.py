from django.shortcuts import render
from .models import Task, Project1
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound

@login_required
def tasks_list(request):
    data = { 'contest_published' : Task.objects.filter(task_type='1')[0].publish,
             'contest_link' : Task.objects.filter(task_type='1')[0].description_link,
             'contest_deadline' : Task.objects.filter(task_type='1')[0].deadline,

             'project_1_published' : Task.objects.filter(task_type='2')[0].publish,
             'project_1_link': Task.objects.filter(task_type='2')[0].description_link,
             'project_1_deadline': Task.objects.filter(task_type='2')[0].deadline,
             'project_1_passed': len(Project1.objects.filter(user_id=request.user.id)) == 0,
             'project_1_response_link': Project1.objects.filter(user_id=request.user.id)[0].link if (len(Project1.objects.filter(user_id=request.user.id)) != 0) else '',

             'project_2_published': Task.objects.filter(task_type='3')[0].publish,
             'project_2_link': Task.objects.filter(task_type='3')[0].description_link,
             'project_2_deadline': Task.objects.filter(task_type='3')[0].deadline,

             'lab_published': Task.objects.filter(task_type='4')[0].publish,
             'lab_link': Task.objects.filter(task_type='4')[0].description_link,
             'lab_deadline': Task.objects.filter(task_type='4')[0].deadline,
             }
    return render(request,
                  'tasks/tasks.html',
                  context=data,
                  )

@login_required
def create(request):
    if request.method == 'POST':
        project = Project1()
        project.user_id = request.user.id
        project.user_name = request.user.last_name + ' ' + request.user.first_name
        project.link = request.POST.get('name')
        project.save()
    return HttpResponseRedirect('/tasks/')