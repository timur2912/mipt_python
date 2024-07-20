from django.shortcuts import render
# from .models import Task, Project1
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from  tasks.models import Project1, Task

@login_required
def scores_list(request):
    data = {
        'contest' : Task.objects.filter(task_type="1")[0],
        'project_1_score' : Project1.objects.filter(user_id=request.user.id)[0].score if (len(Project1.objects.filter(user_id=request.user.id))!=0) else '',
        'project_1_status': Project1.objects.filter(user_id=request.user.id)[0].status if (len(Project1.objects.filter(user_id=request.user.id))!=0) else '',
    }
    return render(request,
                  'scores/scores.html',
                  context=data,
                  )