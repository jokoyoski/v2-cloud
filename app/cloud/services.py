# services/vm_service.py

from .models import Vm

class VmService:
    @staticmethod
    def get_all_vms():
        return Vm.objects.all()