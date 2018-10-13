from django.urls import path
from .views import all_district,district_details,distric_school,male_user,female_user
urlpatterns = [
    path('info/district/list',all_district),
    path('districts/',district_details,name="district_details"),
    path('schools/<district>',distric_school,name="district-school"),
    path('male/',male_user,name="male-user"),
    path('female/',female_user,name="female-user"),
]
