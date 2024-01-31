from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoins(request):
    #joined details of emp and dept table
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    #emp whose hiredate=2015
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2015)
    #emp whose hiredate=2015 and salary greater than 2500
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2015,sal__gt=2500)
    #emp who is working in dept 30
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=30)
    #emp who is working in accounting department
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    #emp whose location is DALLAS
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='DALLAS')
    #emp who don't have manager
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    #emp who is not getting any commition
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    #details of both emp and dept where name=simth
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename='SMITH')
    #ename,dname,dlocation of all employees(select only these in html page)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)