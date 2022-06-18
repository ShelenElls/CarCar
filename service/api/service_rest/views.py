from pyexpat import model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import AutomobileVo, Technician, Appointment

class AutomobileVoEncoder(ModelEncoder):
    model = AutomobileVo
    properties = [
        "vin"
    ]

class TechnicianEncoder(ModelEncoder):
    model = Technician
    properties = [
        "name",
        "employee_number"
    ]

class AppointmentEncoder(ModelEncoder):
    model = Appointment
    properties = [
        "owner_name",
        "date",
        "reason",
    ]
    encoders = {
        "vin": AutomobileVoEncoder(),
        "technician": TechnicianEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_services(request):
    if request.method == "GET":
        service = Appointment.objects.all()
        return JsonResponse(
            {"service": service},
            encoder=AppointmentEncoder,
            safe=False,
        )
    else:
        content = json.loads(request.body)
        # try and except for vins and technicians
        try:
            id = content["vin"]
            vin = AutomobileVoEncoder.objects.get(vin=id)
            content["vin"] = vin
        except AutomobileVoEncoder.DoesNotExist:
            return JsonResponse(
                {"message": "Vin not in database"},
                status=400
            )
        try:
            id = content["technician"]
            num = TechnicianEncoder.objects.get(employee_number=id)
            content["technician"] = num
        except TechnicianEncoder.DoesNotExist:
            return JsonResponse(
                {"message": "Technician not in database"},
                status=400,
            )
        service = Appointment.objects.create(**content)
        return JsonResponse(
            service,
            encoder=AppointmentEncoder,
            safe=False,
        )



@require_http_methods(["GET", "PUT", "DELETE"])
def api_service(request, pk):
    if request.method == "GET":
        service = Appointment.objects.get(id=pk)
        return JsonResponse(
            service,
            encoder=AppointmentEncoder,
            safe=False,
        )
    elif request.method == "PUT":
        content = json.loads(request.body)
        try:
            if "technician" in content:
                technician = Technician.objects.get(employee_number=content["technician"])
                content["technician"] = technician
        except Technician.DoesNotExist:
            return JsonResponse(
                {"message": "invalid employee id"},
                status=400,
            )
        Appointment.objects.filter(id=pk).update(**content)
        service = Appointment.objects.get(id=pk)
        return JsonResponse(
            service,
            encoder=AppointmentEncoder,
            safe=False,
        )
    else:
        count, _ = Appointment.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})


@require_http_methods(["GET", "POST"])
def api_technician(request):
    if request.method == "GET":
        technician = Technician.objects.all()
        return JsonResponse(
            {"technician": technician},
            encoder=TechnicianEncoder,
            safe=False
        )
    else:
        content = json.loads(request.body)
        technician = Technician.objects.create(**content)
        return JsonResponse(
            technician,
            encoder=TechnicianEncoder,
            safe=False,
        )


@require_http_methods(["DELETE"])
def api_tech(request, pk):
    count, _ = Technician.objects.filter(id=pk).delete()
    return JsonResponse({"deleted": count > 0})



# @require_http_methods(["GET", "POST"])
# api_show_appointment = history of appointments? get.filer.vin ? 




# list view for services 
# detail view for services 
# 
# inventoryVO 
# technician post + get - 
# service history - list of apts for specific vin and include details of apts

# class AutomobileVo(models.Model):
#     vin = models.CharField(max_length=17, unique=True)

# class Technician(models.Model):
#     name = models.CharField(max_length=100)
#     employee_number = models.CharField(max_length=100, unique=True)

# class Appointment(models.Model):
#     vin = models.ForeignKey(AutomobileVo, related_name="appointments", on_delete=CASCADE)
#     owner_name = models.CharField(max_length=100)
#     technician = models.ForeignKey(Technician, related_name="appointments", on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     reason = models.TextField()



# api_services, 
# "services/<int:pk>", api_service
# api_show_appointment, 
# api_technician