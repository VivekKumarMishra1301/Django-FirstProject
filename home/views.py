from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        'variable':"this is sent",
        "kuchbhi":"kuch bhi bhej sakte ho"
    }
    return render(request,'index.html',context)
    # return HttpResponse('this is homepage')
# to return string in response
def about(request):
    return render(request,'about.html')




def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contact=Contact(name=name,email=email,password=password,date=datetime.today())
        contact.save()
        messages.success(request, "Message sent!")

    return render(request,'contact.html')