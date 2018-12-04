from django.shortcuts import render, redirect
from django.contrib import messages
from announcement.utils import getAnnouncement
from announcement.models import Announcement

def all_announcement(request):
    user = request.user
    if user.is_authenticated:
        if user.person == 'student':
            announcements = getAnnouncement(user)
            read_announcements = user.read_announcement.all()
            no_r_ann_count = 0
            for ann in announcements:
                if ann not in read_announcements:
                    no_r_ann_count += 1

            user.no_r_ann_count = no_r_ann_count
            user.save()
            context = {}
            context['content_header'] = '所有公告'
            context['ann'] = 'ann'
            context['ann_active'] = 'active'
            context['ann_or_mesgs'] = announcements
            return render(request, 'student/all_ann_or_mesg.html', context)
        elif user.person == 'teacher':
            announcements = getAnnouncement(user)

            read_announcements = user.read_announcement.all()
            no_r_ann_count = 0
            for ann in announcements:
                if ann not in read_announcements:
                    no_r_ann_count += 1

            user.no_r_ann_count = no_r_ann_count
            user.save()
            
            context = {}
            context['announcements'] = announcements
            return render(request, 'teacher/teacher_ann.html', context)
        else:
            pass
    messages.error(request, '请先登录')
    return redirect('/')

def announcement_detail(request, announcement_pk):
    user = request.user
    if user.is_authenticated:
        announcement = Announcement.objects.get(pk = announcement_pk)
        if announcement not in user.read_announcement.all():
            user.read_announcement.add(announcement)
            user.no_r_ann_count -= 1
            user.save()

        context = {}
        context['announcement'] = announcement
        if user.person == 'student':
            return render(request, 'student/announcement_detail.html', context)
        elif user.person == 'teacher':
            return render(request, 'teacher/announcement_detail.html', context)
        else:
            messages.error(request, '请先登录')
    return redirect('/')
