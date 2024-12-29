from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Patient

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            patient = Patient.objects.get(username=username)
            if check_password(password, patient.password):
                return render(request, 'success.html', {'username': username})
            else:
                return render(request, 'login.html', {'error': 'Invalid password'})
        except Patient.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid username'})

    return render(request, 'login.html')
