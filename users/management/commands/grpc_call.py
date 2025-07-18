from django.core.management.base import BaseCommand
from grpc_requests.sample_request import make_grpc_call

class Command(BaseCommand):
    help = 'Runs a sample gRPC request'

    def handle(self, *args, **kwargs):
        make_grpc_call()
