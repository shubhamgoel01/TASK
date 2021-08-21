from django.shortcuts import render
from api.models import  Customer , MobileCompany
from api.serializers import CustomerSerializer, MobileCompanySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class CustomerListView(APIView):

    def get(self, request):
        stu = Customer.objects.all()       
        serializer = CustomerSerializer(stu,many=True)
        # print(stu.id)
        # print(serializer)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailView(APIView):
    
    def get(self, request, pk):
        try:
            customers = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'Error':'customer Not Found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = CustomerSerializer(customers)  
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            customers  = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'Error':'customers  Not Found'},status=status.HTTP_400_BAD_REQUEST) 
        serializer = CustomerSerializer(customers ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            customers  = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return Response({'Error':'Customer Not Found'},status=status.HTTP_400_BAD_REQUEST)  
        customers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)               

class MobileCompanyListView(APIView):

    def get(self, request):
        stu = MobileCompany.objects.all()  
        serializer = MobileCompanySerializer(stu,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MobileCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MobileCompanyDetailView(APIView):
    
    def get(self, request, pk):
        try:
            comp = MobileCompany.objects.get(pk=pk)
        except MobileCompany.DoesNotExist:
            return Response({'Error':'MobileCompany Not Found'},status=status.HTTP_400_BAD_REQUEST)
        serializer = MobileCompanySerializer(comp)  
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            comp = MobileCompany.objects.get(pk=pk)
        except MobileCompany.DoesNotExist:
            return Response({'Error':'MobileCompany  Not Found'},status=status.HTTP_400_BAD_REQUEST) 
        serializer = MobileCompanySerializer(comp ,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            comp  = MobileCompany.objects.get(pk=pk)
        except MobileCompany.DoesNotExist:
            return Response({'Error':'MobileCompany Not Found'},status=status.HTTP_400_BAD_REQUEST)  
        comp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)               

