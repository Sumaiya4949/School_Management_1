from django.urls import path
from .views import school_list,all_details

urlpatterns = [
path('school/list',school_list,name = "school-list"),
     path('schools/', all_details, name="all-details"),

]