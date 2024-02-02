from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q 
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
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)

def selfjoins(request):
    EMPMGROBJECTS=Emp.objects.select_related('mgr').all()
    EMPMGROBJECTS=Emp.objects.select_related('mgr').all()[2:5:]
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(hiredate__year=2015)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(hiredate__year=2015,sal__gte=2500)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__sal__gte=2500)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(ename='CLARK')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(job='ANALYST')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(comm__isnull=True)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(deptno=20)
    #emp whose mgr's JOB=PRESIDENT
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__job='PRESIDENT')
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__empno=7698)
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__deptno=10)
    #emp whose mgr's name startswith 'K'
    EMPMGROBJECTS=Emp.objects.select_related('mgr').filter(mgr__ename__startswith='K')

    d={'EMPMGROBJECTS':EMPMGROBJECTS}
    return render(request,'selfjoins.html',d)


def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='ACCOUNTING')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='RESEARCH') | Q(ename='BLAKE'))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='KING', sal__gte=2500)
    emd=Emp.objects.select_related('deptno','mgr').filter(job='ANALYST')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(job='SALESMAN') | Q(deptno__dlocation='DALLAS'))
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2015,mgr__ename='KING')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(mgr__ename__startswith='S') | Q(sal__gte=2500))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__job='ANALYST')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__empno=7698)
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='NEW YORK')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='S',deptno__dname='RESEARCH')
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False,deptno__dlocation='CHICAGO')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename__endswith='S') | Q(deptno__deptno=20))
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gte=3000)
    emd=Emp.objects.select_related('deptno','mgr').filter(sal__lte=1000,deptno__deptno=20)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(sal__lte=1000) | Q(deptno__deptno=20))
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__in=(10,30))
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation='CHICAGO',mgr__ename='BLAKE')
    emd=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__endswith='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__isnull=True)
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(job='SALESMAN') | Q(mgr__ename='BLAKE'))
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation__contains='a')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__contains='a',deptno__dlocation='CHICAGO')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(mgr__ename__contains='a') | Q(deptno__dlocation='CHICAGO'))
    emd=Emp.objects.select_related('deptno','mgr').filter(hiredate__year=2024)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='S',hiredate__year=2024)
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename__contains='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__deptno__dlocation__endswith='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dlocation__contains='S')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename__endswith='N')
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(ename='N') | Q(deptno__dlocation='DALLAS'))



    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)