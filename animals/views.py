from ast import Delete
from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView

from animals.models import Animal
from animals.serializers import AnimalSerializer
from rest_framework.response import Response
from urllib.request import Request
from rest_framework import status
from django.shortcuts import get_object_or_404

class AnimalView(APIView):
    def get(self, request):
        animals= Animal.objects.all()
        serialized= AnimalSerializer(animals, many=True)
        return Response(serialized.data,status=status.HTTP_200_OK)
    def post(self, request):
        serializer= AnimalSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED) 

class AnimalViewId(APIView):
    def patch(self,request:Request,animal_id:id)->Response:
        animal = get_object_or_404(Animal, id=animal_id)
        serializer= AnimalSerializer(animal, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except KeyError as err:
            return Response(err.args[0], status=status.HTTP_422_UNPROCESSABLE_ENTITY)    
        
        return Response(serializer.data,status=status.HTTP_200_OK)

    def get(self, request, animal_id):
        try:
            animal=Animal.objects.get(id=animal_id)
            serializeed= AnimalSerializer(animal) 
            return Response(serializeed.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"animal not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,animal_id):
        try:
            animal=Animal.objects.get(id=animal_id)
            animal.delete()
            return Response("", status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error":"animal not found"}, status=status.HTTP_404_NOT_FOUND)



