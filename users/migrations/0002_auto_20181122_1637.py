# Generated by Django 2.1.2 on 2018-11-22 08:37

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUser',
            fields=[
            ],
            options={
                'verbose_name': '学生用户',
                'verbose_name_plural': '学生用户',
                'proxy': True,
                'indexes': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherUser',
            fields=[
            ],
            options={
                'verbose_name': '教师用户',
                'verbose_name_plural': '教师用户',
                'proxy': True,
                'indexes': [],
            },
            bases=('users.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-username'], 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
        migrations.AddField(
            model_name='user',
            name='read_announcement',
            field=models.ManyToManyField(blank=True, to='announcement.Announcement'),
        ),
    ]
