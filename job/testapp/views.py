from django.shortcuts import render
from testapp.models import Hydjobs

# Create your views here.
def homepage_view(request):
    return render(request, 'testapp/index.html')

def Hydjobs_view(request):
    job_list = Hydjobs.objects.all()
    my_dict = {'job_list' : job_list}

    return render(request, 'testapp/hydjobs.html')