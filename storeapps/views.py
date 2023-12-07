from django.shortcuts import render , redirect ,HttpResponse
from django.http import JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    departments = Department.objects.all()
    return render(request, 'index.html' , {'departments': departments})

def cousre_Detail(request,):
    # Retrieve departments

    return render(request, 'coursedetail.html', )


def orderForm(request):
    order_form = OrderForm()

    # if request.method == 'GET':
    #     department_id = request.GET.get('department_id')
    #     courses = Course.objects.filter(department=department_id).values('id', 'name')
    #     return JsonResponse(list(courses), safe=False)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('order_Confirmed')

    return render(request, 'courseform.html', {'order_form': order_form})

def get_courses(request, department_id):
    courses = Course.objects.filter(department_id=department_id).values('id', 'name')
    return JsonResponse(list(courses), safe=False)


def order_Confirmed(request):
    return render(request, 'order.html')

# def courseForm(request):
#     departments = Department.objects.all()
#     course = Course.objects.all()
#     materials = Material.objects.all()
#     order = Order
    
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         dob = request.POST.get('dob')
#         age = request.POST.get('age')
#         gender = request.POST.get('gender')
#         phone_Number = request.POST.get('phone_number')
#         mail = request.POST.get('mail_id')
#         adress = request.POST.get('address')

#         dep_id = request.POST.get('department')
#         department = Department.objects.get(id=dep_id)

#         course_id = request.POST.get('course')
#         course_instance = Course.objects.get(id=course_id)

       
#         purpose = request.POST.get('purpose')
#         material_ids = request.POST.getlist('materials_provide')
#         materials_provide = Material.objects.filter(id__in=material_ids)
#         order=Order(name=name,dob=dob,age=age,gender=gender,phone_number=phone_Number,
#                     department=department,course=course_instance,purpose=purpose,mail_id=mail,address=adress)
#         order.save()

#         order.materials_provide.set(materials_provide)

#         message="submited successfully"

        

#         return render(request, 'courseform.html' , {'departments': departments ,'course': course,'message': message})
        


#     return render(request, 'courseform.html' , {'departments': departments ,'course': course,'materials': materials, 'order': order})







