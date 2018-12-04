import os
from datetime import timedelta
from django.core.paginator import Paginator
from django.conf import settings
from users.models import User
from message.models import Message
from thesis.models import Tag

upload_dir = settings.UPLOAD_DIR  #D:\1毕业设计\media\upload
public_dir = settings.PUBLIC_DIR  #D:\1毕业设计\media\public

#page==当前页的页码  num== 每页多少条数据 name== 要返回的每页存储的数据的context键名
def get_page_list(obj_list, page, num, name):
    paginator = Paginator(obj_list, num)
    max_page_num = paginator.num_pages
    page_obj_list = paginator.get_page(page)    #返回一个paginator对象，包含当前页面的数据列表
    current_page = int(page)

    page_range = [i for i in range (current_page - 2, current_page + 3) if i > 1 and i < max_page_num]
    if current_page - 3 > 1:
        page_range.insert(0, '...')
    if current_page + 3 < max_page_num:
        page_range.append('...')
    page_range.insert(0, 1)
    if max_page_num != 1:
        page_range.append(max_page_num)

    context = {}
    context[name] = page_obj_list
    context['page_range'] = page_range

    return context

def get_tag_list(college):
    tags_dict = {}
    tags = Tag.objects.filter(thesis__publisher__teacher__college = college)
    for tag in tags:
        tag_thesis_count = tag.thesis_set.filter(is_choiced=False).count()
        if tag_thesis_count > 0:
            tags_dict[tag] =  tag_thesis_count

    return tags_dict

def get_public_file(person):
    public_file_dict = {}

    #获取公共文件文件夹下的所有文件
    all_public_files = [file for file in os.listdir(public_dir) if \
                        os.path.isfile(os.path.join(public_dir,file))]

    for file in all_public_files:
            public_file_dict[file] = os.path.join(public_dir, file)

    #获取管理员发给学生的文件
    if person == 'student':
        student_public_files=[file for file in os.listdir(os.path.join(public_dir, 'student'))\
                              if os.path.isfile(os.path.join(public_dir,'student',file))]
        student_public_dir = os.path.join(public_dir, 'student')
        for file in student_public_files:
            public_file_dict[file] = os.path.join(student_public_dir, file)
        
    #获取管理员发给教师的文件
    else:
        teacher_public_files=[file for file in os.listdir(os.path.join(public_dir, 'teacher'))\
                              if os.path.isfile(os.path.join(public_dir,'teacher',file))]
        teacher_public_dir = os.path.join(public_dir, 'teacher')
        for file in teacher_public_files:
            public_file_dict[file] = os.path.join(teacher_public_dir, file)
    return public_file_dict

def get_student_file(student):
    teacher = student.teacher
    student_files_dict = {}

    #获取教师文件夹路径和学生文件夹路径
    teacher_dir = os.path.join(upload_dir, teacher.name + teacher.number)
    student_dir = os.path.join(teacher_dir, student.name + student.number)

    #判断是否有教师文件夹，如果没有则创建
    if not os.path.exists(teacher_dir) or not os.path.exists(student_dir):
        return None

    #获取学生文件夹下的所有文件,返回所有文件名的list
    student_files = [file for file in os.listdir(student_dir) \
                    if os.path.isfile(os.path.join(student_dir, file))]

    for file in student_files:
        student_files_dict[file] = os.path.join(student_dir, file)

    return student_files_dict

def get_teacher_file(teacher):
    teacher_files_dict = {}

    teacher_dir = os.path.join(upload_dir, teacher.name + teacher.number)
    if not os.path.exists(teacher_dir):
        return None

    #获取教师文件夹下的所有文件,返回所有文件名的list
    teacher_files = [file for file in os.listdir(teacher_dir) \
                    if os.path.isfile(os.path.join(teacher_dir, file))]
    for file in teacher_files:
        teacher_files_dict[file] = os.path.join(teacher_dir, file)

    return teacher_files_dict

def sendMessage(receiver_pk, sender, content ):
    data = {}
    receiver = User.objects.get(pk = receiver_pk)

    if content.strip():
        message = Message.objects.create(content=content, receiver=receiver, sender=sender)
        data['status'] = 'SUCCESS'
        data['message'] = content
        send_time = message.send_time + timedelta(hours=8)
        data['send_time'] = send_time.strftime('%m-%d %H:%M')
    else:
        data['status'] = 'ERROR'
        data['message_error'] = '不能为空'

    return data
