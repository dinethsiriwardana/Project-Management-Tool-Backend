from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Sample
from .serializers import SampleSerializer

class SampleViewSet(viewsets.ViewSet):
    # List all samples
    def list(self, request):
        samples = Sample.objects.all()
        serializer = SampleSerializer(samples, many=True)
        return Response(serializer.data)

    # Create a new sample
    def create(self, request):
        serializer = SampleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve a specific sample
    def retrieve(self, request, pk=None):
        try:
            sample = Sample.objects.get(pk=pk)
        except Sample.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = SampleSerializer(sample)
        return Response(serializer.data)

    # Update a sample
    def update(self, request, pk=None):
        try:
            sample = Sample.objects.get(pk=pk)
        except Sample.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SampleSerializer(sample, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a sample
    def destroy(self, request, pk=None):
        try:
            sample = Sample.objects.get(pk=pk)
        except Sample.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        sample.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)