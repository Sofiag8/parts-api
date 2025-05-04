from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Part
from .serializers import PartSerializer

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

    @action(detail=False, methods=['post'], url_path='bulk-create')
    def bulk_create(self, request):
        data = request.data
        if not isinstance(data, list):
            return Response({'error': 'Expected a list of parts'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = PartSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['delete'], url_path='bulk-delete')
    def bulk_delete(self, request):
        ids = request.data.get('ids', [])
        if not isinstance(ids, list):
            return Response({'error': 'Expected a list of IDs'}, status=status.HTTP_400_BAD_REQUEST)

        parts_to_delete = Part.objects.filter(id__in=ids)
        deleted_count = parts_to_delete.count()
        parts_to_delete.delete()

        return Response({'message': f'{deleted_count} parts deleted.'}, status=status.HTTP_200_OK)
