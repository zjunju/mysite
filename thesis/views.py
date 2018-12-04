import random
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .models import Thesis

def thesis_detail(request, thesis_pk):
    person = request.user.person
    context = {}
    if person == 'teacher':
        try:
            thesis = Thesis.objects.get(pk = thesis_pk)
            context['thesis'] = thesis
            return render(request, 'teacher/thesis_detail.html', context)
        except ObjectDoesNotExist:
            messages.error(request, '该选题不存在了！')
            return redirect(reverse('teacher_home'))

    elif person == 'student':
        college = request.user.student.college
        try:
            thesis = Thesis.objects.get(pk = thesis_pk)
            theses_list = []
            tags = thesis.tags.all()
            context['thesis'] = thesis
            if tags:
                for tag in tags:
                    #thesis_list 寻找类似于当前选题的选题集合，第一个找相同标签，
                    #第二个找同一发布者的为选题选题
                    theses_list += list(Thesis.objects.filter(tags=tag, is_choiced=False))

                theses_list += Thesis.objects.filter(publisher = thesis.publisher,\
                                                    is_choiced=False) 
                theses_set = set(theses_list)
            if thesis in theses_set:
                theses_set.remove(thesis)
            #如果类似于当前选题的数量大于5则随机抽5篇
            if len(theses_set) > 5:
                context['theses_with_like'] = random.sample(theses_set,5)
            #如果为0则在所有选题中随机抽5篇
            elif len(theses_set) == 0:
                theses = list(Thesis.objects.filter(publisher__teacher__college=college,\
                                                 is_choiced=False))
                if len(theses) > 5:
                    context['theses_with_like'] = random.sample(theses,5)
                else:
                    context['theses_with_like'] = theses.remove(thesis)
            else:
                context['theses_with_like'] = theses_set
            return render(request, 'student/thesis_detail.html', context)
        except ObjectDoesNotExist:
            theses = Thesis.objects.filter(publisher__teacher__college = college,\
                                            is_choiced=False)
            cache.set('theses', theses, 120)
            messages.error(request, '该选题不存在了！')
            return redirect( reverse('thesis_list'))
        
    else:
        return redirect('/')
        