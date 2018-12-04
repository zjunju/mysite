from .models import Announcement
from student.models import Student
from django.db.models import Q


def getAnnouncement(obj):
    person = obj.person
    if person == 'teacher':
        announcements = Announcement.objects.filter(Q(receiver = 'all')\
                                                |Q(receiver = 'all_teacher'),
                                        Q(sender__name=obj.teacher.college)\
                                        |Q(sender__is_superuser=True))

        return announcements
    elif person == 'student':
        student = obj.student
        if student.is_choiced_thesis == False:
            announcements = Announcement.objects.\
                                        filter(Q(receiver='all_student')\
                                        |Q(receiver='all')\
                                        |Q(receiver='no_thesis_student'),
                                        Q(sender__name=student.college)\
                                        |Q(sender__is_superuser=True))
        elif student.is_choiced_thesis == True:
            announcements = Announcement.objects.\
                                        filter(Q(receiver='all_student')\
                                        |Q(receiver='all')\
                                        |Q(receiver='thesis_student'),\
                                        Q(sender__name=student.college)\
                                        |Q(sender__is_superuser=True))
        else:
            announcements = Announcement.objects.\
                                        filter(Q(receiver='all_student')\
                                             |Q(receiver='all'),
                                            Q(sender__name=student.college)\
                                            |Q(sender__is_superuser=True))
        return announcements
    else:
        return None
