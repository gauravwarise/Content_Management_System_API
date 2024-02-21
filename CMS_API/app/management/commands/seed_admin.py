from django.core.management.base import BaseCommand
from app.models import User

class Command(BaseCommand):
    help = 'Seed admin user'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin',pincode=12456)
            self.stdout.write(self.style.SUCCESS('Successfully seeded admin user'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))
