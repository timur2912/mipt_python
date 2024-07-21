from django.shortcuts import render
# from .models import Task, Project1
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound
from  tasks.models import Project1, Task, Project2, Lab

@login_required
def scores_list(request):
    score_1 = Project1.objects.filter(user_id=request.user.id)[0].score if (
                    len(Project1.objects.filter(user_id=request.user.id))!=0) else 0
    score_2 = Project2.objects.filter(user_id=request.user.id)[0].score if (
                    len(Project2.objects.filter(user_id=request.user.id)) != 0) else 0
    score_lab = Lab.objects.filter(user_id=request.user.id)[0].score if (
                len(Lab.objects.filter(user_id=request.user.id)) != 0) else 0
    status_1 = Project1.objects.filter(user_id=request.user.id)[0].status if (len(Project1.objects.filter(user_id=request.user.id))!=0) else ''
    status_2 = Project2.objects.filter(user_id=request.user.id)[0].status if (
                    len(Project2.objects.filter(user_id=request.user.id)) != 0) else ''
    status_lab = Lab.objects.filter(user_id=request.user.id)[0].status if (
                len(Lab.objects.filter(user_id=request.user.id)) != 0) else ' '
    data = {
        'contest' : Task.objects.filter(task_type="1")[0],
        'project_1_score' : score_1,
        'project_1_status': status_1,

        'project_2_score': score_2,
        'project_2_status': status_2,

        'lab_score': score_lab,
        'lab_status': status_lab,

        'total_score' : score_1 + score_2 + score_lab if (status_1 == 'Accepted' and
                                                          status_2 == 'Accepted' and
                                                          status_lab == 'Accepted') else 'Неуд(1)', ## ATTENTION! Here is Total mark for the course

    }
    return render(request,
                  'scores/scores.html',
                  context=data,
                  )