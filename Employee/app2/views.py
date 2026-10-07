


from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department, Company


# -------------------------------
# DISPLAY EMPLOYEES
# -------------------------------

# Create your views here.
def display(request):
    data=Employee.objects.all()
    return render(request,"empdata.html",{'employeedata': data})


# -------------------------------
# ADD EMPLOYEE
# -------------------------------
def addEmpData(request):

    dep_data = Department.objects.all()
    com_data = Company.objects.all()

    if request.method == "POST":

        name = request.POST.get('nm')
        age = request.POST.get('ag')
        email = request.POST.get('em')
        salary = request.POST.get('sal')
        address = request.POST.get('add')

        department = request.POST.get('dep')
        company = request.POST.get('comp')

        Employee.objects.create(
            name=name,
            age=age,
            email=email,
            salary=salary,
            address=address,
            department_id=department,
            company_id=company
        )

        return redirect('empdata')

    return render(
        request,
        'from.html',
        {
            'dep_data': dep_data,
            'com_data': com_data
        }
    )


# -------------------------------
# EDIT EMPLOYEE
# -------------------------------
def updateEmpData(request, id):

    emp = get_object_or_404(Employee, id=id)

    dep_data = Department.objects.all()
    com_data = Company.objects.all()

    if request.method == "POST":

        emp.name = request.POST.get('nm')
        emp.age = request.POST.get('ag')
        emp.email = request.POST.get('em')
        emp.salary = request.POST.get('sal')
        emp.address = request.POST.get('add')

        # Foreign Keys
        emp.department_id = request.POST.get('dep')
        emp.company_id = request.POST.get('comp')

        emp.save()

        return redirect('empdata')

    return render(
        request,
        'editfrom.html',
        {
            'emp': emp,
            'dep_data': dep_data,
            'com_data': com_data
        }
    )


# -------------------------------
# DELETE EMPLOYEE
# -------------------------------
def deleteEmpData(request, id):

    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('empdata')

    

