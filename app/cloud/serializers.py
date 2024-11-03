# serializers.py

from rest_framework import serializers
from .models import Vm, Server

class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ['region', 'name']
        
class VmSerializer(serializers.ModelSerializer):
    server = ServerSerializer(read_only=True)
    class Meta:
        model = Vm
        fields = [ 'ssh_key', 'cpus', 'ram', 'server', 'active']


