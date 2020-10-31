from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time


def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def send_datetime(request):
    # delay by 5 seconds
    time.sleep(5)
    return HttpResponse(str(datetime.datetime.now()))
