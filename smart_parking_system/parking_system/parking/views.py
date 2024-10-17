from django.shortcuts import render, HttpResponseRedirect
from .models import Vehicle
from .number_plate_detection import extract_number_plate

TOTAL_SLOTS = 100  # Total parking slots

def index(request):
    # Count the number of vehicles currently parked
    parked_count = Vehicle.objects.count()
    available_slots = TOTAL_SLOTS - parked_count
    return render(request, 'parking/index.html', {'available_slots': available_slots})

def vehicle_entry(request):
    if request.method == 'POST':
        # Detect vehicle number from the entry video
        vehicle_number = extract_number_plate('parking/media/entry_video.mp4')

        # Add vehicle to the database if it isn't already parked
        if not Vehicle.objects.filter(vehicle_number=vehicle_number).exists():
            Vehicle.objects.create(vehicle_number=vehicle_number)
        return HttpResponseRedirect('/')

def vehicle_exit(request):
    if request.method == 'POST':
        # Detect vehicle number from the exit video
        vehicle_number = extract_number_plate('parking/media/entry_video.mp4')

        # Find and delete the vehicle from the database
        vehicle = Vehicle.objects.filter(vehicle_number=vehicle_number).first()
        if vehicle:
            vehicle.delete()
        else:
            print(f"Vehicle with number {vehicle_number} not found")

        return HttpResponseRedirect('/')
