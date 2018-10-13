from django.urls import path
from myapp.views import student_list,first_letter,wise_class,Call_class,Num_List,Odd_Even,student_details,score_record_list


urlpatterns = [

    path('list/',student_list,name="student-list"),
    path('detail/<int:roll>/',student_details,name="student-detail"),
    path('127.0.0.1:8000/even-odd/<int:no>',Odd_Even),
    path('numbers/',Num_List),
    path('roll/',score_record_list),
    path('student/class/<int:cls>',Call_class,name="Call-Class"),
    path('studentid/',wise_class,name="class-wise"),
    path('student/search/<letter>',first_letter,name="first-letter")
]