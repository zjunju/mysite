from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q

#get_tag_list(college)  get_page_list(obj_list, page, num ,name) 
from my_site.utils import get_public_file, get_student_file, get_teacher_file, sendMessage
from announcement.utils import getAnnouncement
from message.models import Message

from .forms import StudentInfoForm
from .models import Student

def student_home(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        context = {}
        student = Student.objects.get(number = user.username)

        #获取公告文件
        public_files_dict = get_public_file(user.person)
        context['public_files_dict'] = public_files_dict

        if student.teacher:
            student_files_dict = get_student_file(student) #返回学生文件夹的所有文件
            teacher_files_dict = get_teacher_file(student.teacher)
            context['student_files_dict'] = student_files_dict
            context['teacher_files_dict'] = teacher_files_dict
            
        #获取未读信息数
        no_r_mesg_count = Message.objects.filter(receiver=user, is_read=False).count()
        if no_r_mesg_count != user.no_r_message_count:
            user.no_r_message_count = no_r_mesg_count
            user.save()

        #获取公告
        announcements = getAnnouncement(user)
        read_announcements = user.read_announcement.all()
        no_r_ann_count = 0
        for ann in announcements:
            if ann not in read_announcements:
                no_r_ann_count += 1
        if user.no_r_ann_count !=no_r_ann_count:
            user.no_r_ann_count = no_r_ann_count
            user.save()
        context['student'] = student
        return render(request, 'student/student_home.html', context)
    else:
        return redirect('/')

#学生修改信息
def student_update_info(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        if request.method == 'POST':
            student_info_form = StudentInfoForm(request.POST)
            student = Student.objects.get(number = user.username)
            if student_info_form.is_valid():
                student.email = student_info_form.cleaned_data['email']
                student.introduction = student_info_form.cleaned_data['introduction']
                student.phonenumber = student_info_form.cleaned_data['phonenumber']
                student.save()
                return redirect(request.GET.get('from', '/'))
        else:
            student = Student.objects.get(number = user.username)
            initial_data = {'email':student.email,'phonenumber':student.phonenumber,\
                            'introduction':student.introduction}
            student_info_form = StudentInfoForm(initial = initial_data)

        context = {}
        context['student_info_form'] = student_info_form
        return render(request, 'student/update_info.html', context)
    else:
        return redirect('/')

#查看与教师的信息记录
def student_message(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        no_r_messges = Message.objects.filter(receiver=user, is_read=False)
        no_r_messges.update(is_read=True)
        user.no_r_message_count = 0
        user.save()
        
        context = {}
        student = user.student
        teacher = student.teacher
        if teacher:
            student_messages = Message.objects.\
                                filter(Q(sender=student.user) \
                                    | Q(receiver=student.user))\
                                    .order_by('send_time')

            context['student_messages'] = student_messages
            context['teacher'] = teacher
            
        context['student'] = student
        
        return render(request, 'student/send_messages.html', context)

    else:
        return redirect('/')

def student_no_read_message(request):
    user = request.user
    if user.is_authenticated and user.person == 'student':
        context = {}
        student = user.student
        if student.teacher:
            no_read_messages = Message.objects.filter(receiver=user, is_read = False, \
                                                        sender=student.teacher.user)
            context['ann_or_mesgs'] = no_read_messages

        context['content_header'] = '未读消息'
        context['mesg'] = 'mesg'
        context['mesg_active'] = 'active'
        return render(request, 'student/all_ann_or_mesg.html', context)

    else:
        messages.error(request, '请先登录')
        return redirect('/')
