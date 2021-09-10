from django.shortcuts import render
from . models import Employee

def base(request):
    return render(request, 'structcomp/base.html')

def structure(request):
    return render(request, 'structcomp/structure.html')

def dep1(request):
    return render(request, 'structcomp/dep1.html')

# вывод данных сотрудников по принадлежности к какому-либо подразделению департамента
def dep1_1(request):
    list_employee = Employee.objects.filter(department__contains = ('DEP1_1'))
    return render(request, 'structcomp/dep1_1.html', {'list_employee': list_employee})
def dep2_1(request):
    list_employee = Employee.objects.filter(department__contains = ('DEP1_2'))
    return render(request, 'structcomp/dep2_1.html', {'list_employee': list_employee})
def dep3_1(request):
    list_employee = Employee.objects.filter(department__contains = ('DEP1_3'))
    return render(request, 'structcomp/dep3_1.html', {'list_employee': list_employee})
def dep4_1(request):
    list_employee = Employee.objects.filter(department__contains = ('DEP1_4'))
    return render(request, 'structcomp/dep4_1.html', {'list_employee': list_employee})
def dep5_1(request):
    list_employee = Employee.objects.filter(department__contains = ('DEP1_5'))
    return render(request, 'structcomp/dep5_1.html', {'list_employee': list_employee})
# Create your views here.
