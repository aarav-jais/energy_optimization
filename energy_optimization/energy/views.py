from django.shortcuts import render
from energy.models import EnergyConsumption, EnergyOptimization
from datetime import datetime

# Create objects only if not already created or use Django shell for this task
def dashboard(request):
    # Fetch energy consumption and optimization suggestions from the DB
    energy_data = EnergyConsumption.objects.all()
    optimization_suggestions = EnergyOptimization.objects.all()

    # Collecting device names and energy values for the chart
    device_names = [entry.device_name for entry in energy_data]
    energy_values = [entry.energy_used for entry in energy_data]

    context = {
        'energy_data': energy_data,
        'optimization_suggestions': optimization_suggestions,
        'device_names': device_names,
        'energy_values': energy_values,
    }
    
    return render(request, 'energy/dashboard.html', context)

from .models import EnergyConsumption, EnergyBenchmark

def benchmark_view(request):
    benchmarks = EnergyBenchmark.objects.all()
    consumptions = EnergyConsumption.objects.all()

    comparison_data = []
    for benchmark in benchmarks:
        consumption = consumptions.filter(device_name=benchmark.device_name).last()
        if consumption:
            comparison_data.append({
                'device_name': benchmark.device_name,
                'benchmark': benchmark.benchmark_value,
                'actual': consumption.energy_used,
                'status': 'Overused' if consumption.energy_used > benchmark.benchmark_value else 'Optimized'
            })

    context = {
        'comparison_data': comparison_data
    }
    return render(request, 'energy/benchmark.html', context)



from django.shortcuts import render
from .models import UtilityBill

def utility_bill_view(request):
    bills = UtilityBill.objects.all().order_by('-billing_month')
    return render(request, 'energy/utility_bills.html', {'bills': bills})



from django.shortcuts import render
from .models import EnergyRecommendations



def energy_recommendations_view(request):
    recommendations = EnergyRecommendations.objects.all().order_by('-recommendation_date')
    return render(request, 'energy/recommendations.html', {'recommendations': recommendations})



from django.shortcuts import render, redirect
from .models import RenewableEnergyGeneration
from .forms import RenewableEnergyGenerationForm

def renewable_energy_view(request):
    if request.method == 'POST':
        form = RenewableEnergyGenerationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('renewable-energy')
    else:
        form = RenewableEnergyGenerationForm()
    data = RenewableEnergyGeneration.objects.select_related('source').order_by('-timestamp')
    return render(request, 'energy/renewable_energy.html', {'form': form, 'data': data})


from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import UserProfile
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Create profile
            UserProfile.objects.create(
                user=user,
                role=form.cleaned_data['role'],
                department=form.cleaned_data['department']
            )
            return redirect('login')  # redirect to login page after registration
    else:
        form = UserRegistrationForm()
    return render(request, 'energy/register.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # ya koi bhi home page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    return render(request, 'energy/login.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # 'login' should be the name of your login URL


from django.shortcuts import render

def energy_analysis_view(request):
    return render(request, 'energy/energy_analysis.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home_view(request):
    return render(request, 'energy/home.html')




# Create your views here.
