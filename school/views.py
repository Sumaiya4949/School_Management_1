from django.shortcuts import render
from .models import SchoolInfo

# Create your views here.
def school_list(request):
    scl_list = SchoolInfo.objects.all()
    context = {'school':scl_list}
    return render(request,'school_list.html',context)

def all_details(request):
    scl_details = SchoolInfo.objects.all()
    context = {'details': scl_details }
    return render(request, 'school_details.html', context)



