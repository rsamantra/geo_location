from django.core.management.base import BaseCommand

from core.models import *


class Command(BaseCommand):
    """
    Update Location with some default values
    """
    help = 'Update Location with some default values'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Inserting data for Location model'))
        l1 = Location.objects.create(state="san mateo", latitude=37.554169,longitude=-122.313057)
        l2 = Location.objects.create(state="berkely", latitude=37.871666,longitude=-122.272781)
        l3 = Location.objects.create(state="columbia", latitude=38.951561,longitude=-92.328636)
        l4 = Location.objects.create(state="athens", latitude=33.950001,longitude=-83.383331)
        l5 = Location.objects.create(state="pasadena", latitude=34.156113,longitude=-118.131943)
        self.stdout.write(self.style.SUCCESS('Its done'))
