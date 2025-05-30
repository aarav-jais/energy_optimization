# energy/seed_data.py

from energy.models import EnergyBenchmark, EnergyConsumption

def run():
    # Clear old data (optional)
    EnergyBenchmark.objects.all().delete()
    EnergyConsumption.objects.all().delete()

    # Dummy benchmark data
    benchmarks = [
        {"device_name": "AC", "benchmark_value": 50},
        {"device_name": "Refrigerator", "benchmark_value": 30},
        {"device_name": "Heater", "benchmark_value": 40},
        {"device_name": "Lighting", "benchmark_value": 20},
    ]

    # Dummy consumption data
    consumptions = [
        {"device_name": "AC", "energy_used": 60},
        {"device_name": "Refrigerator", "energy_used": 25},
        {"device_name": "Heater", "energy_used": 50},
        {"device_name": "Lighting", "energy_used": 15},
    ]

    # Insert benchmark data
    for b in benchmarks:
        EnergyBenchmark.objects.create(**b)

    # Insert latest consumption data
    for c in consumptions:
        EnergyConsumption.objects.create(**c)

    print("✅ Sample benchmark & consumption data inserted.")
