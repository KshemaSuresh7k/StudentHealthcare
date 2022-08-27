from django.contrib import admin
from .models import addteacher,addstudent,crud

# Register your models here.
admin.site.register(addteacher)
admin.site.register(addstudent)
admin.site.register(crud)
