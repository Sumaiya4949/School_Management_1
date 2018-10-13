from django.shortcuts import render
from school.models import SchoolInfo
from .models import UserInfo

from .models import District

def all_district(request):
    all_dis = District.objects.all()
    context = {'dictricts':all_dis}
    return render(request,'distric_list.html',context)

def district_details(request):
    detail_district = District.objects.all()
    context = {'dic_details': detail_district}
    return render(request, 'district_details.html', context)

def distric_school(request,district):
    dis_scl = SchoolInfo.objects.filter(district=district)
    context = {'dis':dis_scl}
    return render(request,'school_name.html', context)
def male_user(request):
    user_male = UserInfo.objects.filter(user_gender='m',user_age__gt=18)
    context = {'male_people':user_male}
    return render(request,'older_male.html',context)
def female_user(request):
    user_female=UserInfo.objects.filter(user_gender='f',user_age__gt=18,user_age__lt=25)
    context = {'female_people': user_female}
    return render(request, 'older_female.html', context)
