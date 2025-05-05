'''
    Delete completed tasks older than 90 days
'''

from datetime import timedelta
from django.utils import timezone
from django.core.management.base import BaseCommand
from background_task.models import CompletedTask

class Command(BaseCommand):
    help = 'Delete completed tasks older than 90 days'

    def handle(self, *args, **kwargs):
        # Get all completed tasks older than 90 days
        CompletedTask.objects.filter(run_at__lt=timezone.now() - timedelta(days=90)).delete()