# Generated by Django 5.0.3 on 2024-03-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_vendor_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='service_type',
            field=models.CharField(choices=[('Photographer', 'Photographer'), ('Venue', 'Venue'), ('Caterer', 'Caterer'), ('Decorator', 'Decorator'), ('Makeup', 'Makeup'), ('Mehndi', 'Mehndi'), ('Pandit', 'Pandit'), ('Transport', 'Transport'), ('DJ', 'DJ'), ('Wedding planner', 'Wedding planner')], default=None, max_length=100),
        ),
    ]
