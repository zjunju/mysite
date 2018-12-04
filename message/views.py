from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse

from my_site.utils import sendMessage
from message.models import Message

def send_message(request):
    user = request.user
    if user.is_authenticated:
        receiver_pk = request.POST.get('receiver_pk', None)
        content = request.POST.get('message', None)
        if receiver_pk:
            data = sendMessage(receiver_pk, user, content)
            return JsonResponse(data)
        else:
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, '请先登录')
        return redirect('/')
