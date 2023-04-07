from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, 'main/mainpage.html')
def setting(request):
    return render(request, 'main/setting.html')
def study(request):
    return render(request, 'main/study.html')