from django.shortcuts import render
from rest_framework.views import APIView
import logging
from .serializers import DepartmentSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Departments
log = logging.getLogger(__name__)
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_500_INTERNAL_SERVER_ERROR)

# Create your views here.
class DepartmentView(APIView):
    try:
        def get(self, request):
            departments: Departments = Departments.objects.all()
            # departments: Departments = Departments.objects.filter(DepartmentId =1)
            departments_serializer=DepartmentSerializer(departments,many=True)
            return Response(departments_serializer.data, status=HTTP_200_OK)
    except Exception as e:
        print(e)
        log.exception(e)
        
    try:
        def post(self, request):
            department_data = request.data.get('DepartmentName')
            department = Departments()
            department.DepartmentName = department_data
            department.save()
            # departments_serializer=DepartmentSerializer(data=department_data)
            return JsonResponse("success",safe=False)
    except Exception as e:
        print(e)
        log.exception(e)
        
    try:
        def put(self, request,id):
            print(request.data)
            department_data = request.data.get('DepartmentName')
            department = Departments.objects.get(DepartmentId = id)
            department.DepartmentName = department_data
            department.save()
            return JsonResponse("updated",safe=False)
    except Exception as e:
        print(e)
        log.exception(e)
    
    try:
        def delete(self, request,id):
            department=Departments.objects.get(DepartmentId=id)
            department.delete()
            return JsonResponse("Deleted Successfully",safe=False)
    except Exception as e:
        print(e)
        log.exception(e)