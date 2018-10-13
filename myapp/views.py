from django.shortcuts import render
from myapp.models import StudenInfo
from django.http import HttpResponse
from myapp.models import ScoreRecord
from myapp.models import Class_wise

# Create your views here.
def student_list(request):
    std_list = StudenInfo.objects.all()
    context = {'students':std_list}
    return render(request,'home.html',context)
def student_details(request,roll):
    std = StudenInfo.objects.get(roll=roll)
    context = {'student':std}
    return render(request,'student_detail.html',context)
def Odd_Even(request,no):
    if no % 2 == 0:
        msg="{} is even".format(no)
        return HttpResponse(msg)
    else:
        msg1="{} is odd".format(no)
        return HttpResponse(msg1)

def Num_List(request):
        range_list = range(50,101)
        context={'number':range_list}

        return render(request,'evenNolist.html',context)

def score_record_list(request):
    student_info = ScoreRecord.objects.all()

    context = {
        'students_all': student_info
    }

    return render(request, 'studentRecord.html', context)


def Call_class(request,cls):
    std_cls = StudenInfo.objects.filter(std_class=cls)

    context = {
    'student_class':std_cls
    }

    return render(request, 'class_id.html', context)


def wise_class(request):
    all_class = Class_wise.objects.all()
    context = {
        'class_all': all_class
    }
    return render(request, 'class_wise.html', context)

def first_letter(request,letter):
    name_letter = StudenInfo.objects.filter(name__istartswith=letter)
    context = {'name':name_letter}
    return render(request,'name_letter.html',context)







