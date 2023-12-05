from django.shortcuts import render , redirect ,HttpResponse
from .models import *

# Create your views here.
def index(request):
    departments = Department.objects.all()
    return render(request, 'index.html' , {'departments': departments})

def cousre_Detail(request,id):
    # Retrieve departments
    
    dep = Department.objects.get(id=id)
    course = Course.objects.filter(department=dep)

    

    departments = Department.objects.all()

    return render(request, 'coursedetail.html', {'departments': departments , 'courses': course})

def courseForm(request):
    departments = Department.objects.all()
    course = Course.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_Number = request.POST.get('phone_number')
        mail = request.POST.get('mail_id')
        adress = request.POST.get('address')

        dep_id = request.POST.get('department')
        department = Department.objects.get(id=dep_id)

        course_id = request.POST.get('course')
        course_instance = Course.objects.get(id=course_id)

       
        purpose = request.POST.get('purpose')
        material_Provide = request.POST.get('materials_provide')
        order=Order(name=name,dob=dob,age=age,gender=gender,phone_number=phone_Number,
                    department=department,course=course_instance,purpose=purpose,materials_provide=material_Provide,mail_id=mail,address=adress)
        order.save()

        message="submited successfully"

        return render(request, 'courseform.html' , {'departments': departments ,'course': course,'message': message})
        


    return render(request, 'courseform.html' , {'departments': departments ,'course': course})
