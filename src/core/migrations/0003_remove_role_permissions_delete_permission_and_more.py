# Generated by Django 4.0 on 2022-02-20 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0002_permission_role_alter_contributor_role'),
        ('core', '0002_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]