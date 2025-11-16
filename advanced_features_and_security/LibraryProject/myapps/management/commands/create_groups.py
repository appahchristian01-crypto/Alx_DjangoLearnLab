from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps

class Command(BaseCommand):
    help = "Create default groups (Editors, Viewers, Admins) and assign model permissions."

    def handle(self, *args, **options):
        # Replace 'myapp' with your app label if different
        app_label = 'myapp'
        model_name = 'article'  # lowercase model name

        # Permission codenames we added in models.Meta.permissions
        p_codenames = ['can_view', 'can_create', 'can_edit', 'can_delete']

        # Fetch Permission objects
        permissions = []
        for codename in p_codenames:
            try:
                perm = Permission.objects.get(content_type__app_label=app_label, codename=codename)
                permissions.append(perm)
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Permission {codename} not found. Did you run migrate?"))
                return

        # Create groups
        groups = {
            'Viewers': ['can_view'],
            'Editors': ['can_view', 'can_create', 'can_edit'],
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
        }

        for group_name, codenames in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.clear()
            for code in codenames:
                perm = Permission.objects.get(content_type__app_label=app_label, codename=code)
                group.permissions.add(perm)
            group.save()
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' setup with permissions: {codenames}"))
