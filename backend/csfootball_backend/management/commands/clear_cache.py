from django.core.management.base import BaseCommand
from csfootball_backend.cache_utils import CacheUtils


class Command(BaseCommand):
    help = 'Clears the application cache'

    def add_arguments(self, parser):
        parser.add_argument(
            '--model',
            help='Clear cache for specific model',
        )
        parser.add_argument(
            '--id',
            help='Clear cache for specific instance',
        )

    def handle(self, *args, **options):
        if options['model'] and options['id']:
            CacheUtils.clear_instance_cache(options['model'], options['id'])
            self.stdout.write(f"Cleared cache for {
                              options['model']} with id {options['id']}")
        elif options['model']:
            CacheUtils.clear_model_cache(options['model'])
            self.stdout.write(f"Cleared all cache for {options['model']}")
        else:
            CacheUtils.clear_all_cache()
            self.stdout.write("Cleared all cache")
