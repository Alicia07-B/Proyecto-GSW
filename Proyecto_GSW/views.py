from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    """Página principal con diseño completo"""
    context = {
        'total_equipos': 386,
        'total_calificaciones': 1254,
        'total_recursos': 58,
        'porcentaje_accesibilidad': 92,
        'total_estudiantes': 1254,
        'total_reportes': 24,
    }
    return render(request, 'home.html', context)

@login_required
def dashboard_view(request):  # ← SE LLAMA dashboard_view
    """Dashboard principal"""
    return render(request, 'dashboard.html')

def login_view(request):
    """Vista para el inicio de sesión"""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')  # ← 'dashboard' debe coincidir con name en urls.py
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    return redirect('login')