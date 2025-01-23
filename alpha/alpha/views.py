from django.shortcuts import render

def admin_dashboard(request):
    return render(request, 'admindash.html')

def doctor_dashboard(request):
    return render(request, 'doctor.html')
