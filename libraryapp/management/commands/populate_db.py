from django.core.management.base import BaseCommand

from ... models import add_dummies

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('populate', nargs='+', type=int)

    def handle(self, *args, **options):
        add_dummies()
        self.stdout.write(self.style.SUCCESS('Sucessfully populated the database with some dummy data'))
        