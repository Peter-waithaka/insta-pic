from django.shortcuts import render

# Create your views here.
def Posts(request):
    return render(request,'index.html',)
