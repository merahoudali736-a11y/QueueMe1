from django.shortcuts import render, get_object_or_404
from .models import Clinic,Doctor,Queue

def home(request):
    return render(request, 'home.html')

def clinics(request):
    clinics=Clinic.objects.all()
    return render(request,'clinics.html',{'clinics':clinics})

def clinic_detail(request,id):
    clinic=get_object_or_404(Clinic,id=id)
    doctors = Doctor.objects.filter(clinic=clinic)
    return render(request,'clinic_detail.html',{'clinic':clinic,'doctors':doctors})

def doctor_detail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, 'doctor_detail.html', {'doctor': doctor})

def join_queue(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    last_queue = Queue.objects.filter(doctor=doctor).order_by('-queue_number').first()

    if last_queue:
        queue_number = last_queue.queue_number + 1
    else:
        queue_number = 1

    queue = Queue.objects.create(
        doctor=doctor,
        queue_number=queue_number
    )

    people_before = Queue.objects.filter(
    doctor=doctor,
    queue_number__lt=queue_number
    ).count()
    
    estimated_wait = people_before * 10

    return render(request, 'doctor_detail.html', {
    'doctor': doctor,
    'queue_number': queue_number,
    'people_before': people_before,
    'estimated_wait': estimated_wait,
    'show_popup': True
    }) 
def faq(request):
    return render(request, 'faq.html')