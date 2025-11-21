from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    help = 'Promote a user to admin role with superuser privileges'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the user to promote to admin')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        
        try:
            user = User.objects.get(username=username)
            user.role = 'admin'
            user.is_staff = True
            user.is_superuser = True
            user.save()
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully promoted user "{username}" to admin!')
            )
            self.stdout.write(f'Role: {user.role}')
            self.stdout.write(f'Staff: {user.is_staff}')
            self.stdout.write(f'Superuser: {user.is_superuser}')
            
        except User.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'User "{username}" does not exist!')
            )
