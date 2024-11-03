
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import VmSerializer
from .services import VmService

class VmViewSet(viewsets.ViewSet):
    def list(self, request):
        vms = VmService.get_all_vms()
        serializer = VmSerializer(vms, many=True)
        return Response(serializer.data)