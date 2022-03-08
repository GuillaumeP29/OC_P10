# Generated by Django 4.0 on 2022-02-24 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_contributor_delete_test_project_contributors_and_more'),
        ('issues', '0004_issue_assignee_alter_issue_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignee', to='core.customuser'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='author', to='core.customuser'),
        ),
    ]
