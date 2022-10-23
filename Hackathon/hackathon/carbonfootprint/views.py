from django.shortcuts import render
from django.http import HttpResponse
from .models import calculation_of_carbon_footprint, treek, device, users
from .serializers import UsersSerializer, DeviceSerializer, Carbon_footprintSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    return HttpResponse("This works!")
    


#@csrf_exempt
def carbonfootprint_calculation(request):
    if request.method == "GET":
      
        return HttpResponse("your carbon footprint is %d metric tonnes" )#% round(output))






