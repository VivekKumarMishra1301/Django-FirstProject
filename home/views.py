from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('this is homepage')
# to return string in response
def about(request):
    return HttpResponse('this is aboutpage')
