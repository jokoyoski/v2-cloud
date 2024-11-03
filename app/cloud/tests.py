# cloud/tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vm, Server  # Import your Vm and Server models

class VmViewSetTest(APITestCase):

    def setUp(self):
        self.server = Server.objects.create(
            name='Test Server',
            region='Data Center A'
        )
        
        # Create a test VM instance to be used in the tests
        self.vm = Vm.objects.create(
            name='Test VM',
            cpus=2,
            ram=4,
            server=self.server,
            active=True,
            ssh_key='ssh-rsa example'
        )

    def test_list_vms(self):
        url = reverse('vm-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['ssh_key'], 'ssh-rsa example')
