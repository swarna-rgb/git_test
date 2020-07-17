from django.shortcuts import render
from django.http import HttpResponse

def say_hi(request):
    return HttpResponse("Hi Django !!")

def say_hi_student(request,student):
   # return HttpResponse('Hi ' + student)
   return render(request,'hi/hello.html', {'name':student})