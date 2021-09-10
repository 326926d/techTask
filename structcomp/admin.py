from django.contrib import admin
from .models import Employee



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status', 'date_acceptance', 'salary', 'department')

admin.site.register(Employee, EmployeeAdmin)
# Register your models here.
