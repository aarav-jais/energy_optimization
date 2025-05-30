from django.contrib import admin
from .models import EnergyConsumption, EnergyOptimization, EnergyBenchmark
from .models import UtilityBill
from .models import EnergyRecommendations
from .models import RenewableEnergySource, RenewableEnergyGeneration




admin.site.register(EnergyConsumption)
admin.site.register(EnergyOptimization)
admin.site.register(EnergyBenchmark)
admin.site.register(UtilityBill)
admin.site.register(EnergyRecommendations)
admin.site.register(RenewableEnergySource)
admin.site.register(RenewableEnergyGeneration)








# Register your models here.
