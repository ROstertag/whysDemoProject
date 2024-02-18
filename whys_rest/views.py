from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DataModel

class DataImportView(APIView):
    def post(self, request):
        data = request.data
        try:
            if DataModel.objects.exists():
                DataModel.objects.all().delete()
            for item in data:
                for model_name, model_data in item.items():
                    model_id = model_data['id']
                    DataModel.objects.get_or_create(model_id=model_id, type=model_name, defaults={"columns": item})

            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DataDetailView(APIView):
    def get(self, request, model_name, model_id=None):
        try:
            if not model_id:
                data = DataModel.objects.filter(type=model_name).values_list('columns', flat=True)
            else:
                data = DataModel.objects.filter(type=model_name, model_id=model_id).values_list('columns', flat=True)
            return Response(data)
        except DataModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
