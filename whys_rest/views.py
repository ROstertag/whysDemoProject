from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Model1, Model2
from .serializers import Model1Serializer, Model2Serializer

class ImportDataView(generics.CreateAPIView):
    serializer_class = Model1Serializer  # You can use any model capable of processing input data

class DetailDataView(generics.ListAPIView):
    serializer_class = Model1Serializer  # Use Model1 or Model2 as needed

    def get_queryset(self):
        model_name = self.kwargs['model_name']
        if model_name == 'model1':
            return Model1.objects.all()
        elif model_name == 'model2':
            return Model2.objects.all()
        else:
            return []

class DetailRecordView(generics.RetrieveAPIView):
    queryset = Model1.objects.all()  # Use Model1 or Model2 as needed
    serializer_class = Model1Serializer
    lookup_field = 'id'  # You can use 'id' or another appropriate identifier to find the record
