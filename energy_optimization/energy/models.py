from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class EnergyConsumption(models.Model):
    device_name = models.CharField(max_length=100)
    energy_used = models.FloatField()  # in kWh
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_name} - {self.energy_used} kWh"

class EnergyOptimization(models.Model):
    device_name = models.CharField(max_length=100)
    optimization_suggestion = models.TextField()
    recommendation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Optimization for {self.device_name}"


# models.py

class EnergyBenchmark(models.Model):
    device_name = models.CharField(max_length=100)
    benchmark_value = models.FloatField(help_text="Standard kWh value for the device")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Benchmark for {self.device_name}: {self.benchmark_value} kWh"
    


# energy/models.py

class UtilityBill(models.Model):
    UTILITY_CHOICES = [
        ('Electricity', 'Electricity'),
        ('Water', 'Water'),
        ('Gas', 'Gas'),
    ]

    utility_type = models.CharField(max_length=20, choices=UTILITY_CHOICES)
    billing_month = models.DateField()
    units_consumed = models.FloatField()
    cost_per_unit = models.FloatField()
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utility_type} - {self.billing_month.strftime('%B %Y')}"
    

class EnergyRecommendations(models.Model):
    device_name = models.CharField(max_length=100)
    issue_identified = models.TextField()
    recommendation = models.TextField()
    recommendation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.device_name

#RenewableEnergySource
from django.db import models

class RenewableEnergySource(models.Model):
    SOURCE_CHOICES = [
       ('Wind', 'Wind'),
        ('Biomass', 'Biomass'),
        ('Hydro', 'Hydro'),
    ]
    name = models.CharField(max_length=100, choices=SOURCE_CHOICES)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class RenewableEnergyGeneration(models.Model):
    source = models.ForeignKey(RenewableEnergySource, on_delete=models.CASCADE)
    amount_generated = models.FloatField(help_text="kWh")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source.name} - {self.amount_generated} kWh on {self.timestamp.date()}"





class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('analyst', 'Analyst'),
        ('viewer', 'Viewer'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    department = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

   



# Create your models here.
