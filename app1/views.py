from django.shortcuts import render

# Create your views here.
def print1(request):
    d={'name':'CHARITHA'}
    return render(request,'print1.html',context=d)