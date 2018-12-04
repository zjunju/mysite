from django.urls import path, include
from . import views
from message.views import send_message
from announcement.views import all_announcement, announcement_detail

urlpatterns = [
    path('', views.teacher_home, name = 'teacher_home' ),
    path('announcement/', all_announcement, name='teacher_announcement'),
    path('announcement/<int:announcement_pk>', announcement_detail, \
                                                name='teacher_ann_detail'),
    path('update_info/', views.update_info, name='teacher_update_info'),

    path('thesis/', views.teacher_thesis, name = 'teacher_thesis'),

    path('thesis/publish', views.publish_thesis, name = 'publish_thesis'),
    path('thesis/<int:thesis_pk>/update', views.update_thesis, name='update_thesis'),
    path('thesis/delete', views.delete_thesis, name='delete_thesis'),


    path('group/', include([
        path('', views.group, name='group'),
        path('files/', views.group_files, name='group_files'),
        path('member', views.student_info, name='student_info'),
        path('aggre_thesis/', views.aggre_thesis, name='aggre_thesis'),
        path('disaggre_thesis/', views.disaggre_thesis, name='disaggre_thesis'),
        ])),

    path('message/', views.latest_message, name='teacher_message'),
    path('message/message_with_student', views.message_with_student, name='message_with_student'),
    path('message/send_message', send_message, name='send_message'),
]
