# Generated by Django 4.0.6 on 2022-07-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rake', '0002_state_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
