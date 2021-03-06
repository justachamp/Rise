from django.core.management.base import BaseCommand
import redis
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **options):
        r = redis.from_url(settings.REDIS_URL)
        r.flushall()

