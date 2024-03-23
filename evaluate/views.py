from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def evl_test(request):
    return render(request,'interaction.html')
