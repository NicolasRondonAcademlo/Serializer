from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .serializers import CarSerializer
from .models import Car
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser


# Create your views here.
@csrf_exempt
def car_list(request):

    if request.method == "GET":
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = CarSerializer(
            data=data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201 )
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def car_get_info(request, pk):
    try :
        car = Car.objects.get(pk=pk)
    except Car.DoesNoExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = CarSerializer(car)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = CarSerializer(car, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        car.delete()
        return HttpResponse(status=204)





