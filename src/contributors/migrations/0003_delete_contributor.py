# Generated by Django 4.0 on 2022-02-20 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0002_permission_role_alter_contributor_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contributor',
        ),
    ]
