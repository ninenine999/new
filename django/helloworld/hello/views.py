from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world !  django ~~")


def demo(request):
    return render(request, 'demo.html')

def home(request, year="2019", month="03"):
    return HttpResponse("获取当前页面home时间标签：%s年/%s月" %(year, month))

def baidu(request):
    return render(request, 'baidu.html')

def page(request, num):
    try:
        num = int(num)
        return render(request, 'demo.html')
    except:
        raise Http404