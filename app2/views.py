from django.shortcuts import render

# Create your views here.
def print2(request):
    d={'name':'CHERRY'}
    return render(request,'print2.html',context=d)