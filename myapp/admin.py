from django.contrib import admin

from .models import ScoreRecord,StudenInfo,Class_wise,Gurdian



# Register your models here.

admin.site.register(StudenInfo)
admin.site.register(ScoreRecord)
admin.site.register(Class_wise)
admin.site.register(Gurdian)

