# Generated by Django 4.2.9 on 2024-01-29 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('azs', '0003_alter_imageurls_urls'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalservices',
            old_name='additional_services',
            new_name='services',
        ),
    ]
