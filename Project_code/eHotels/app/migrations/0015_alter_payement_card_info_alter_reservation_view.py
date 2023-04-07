# Generated by Django 4.1.7 on 2023-04-04 18:40

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_room_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payement',
            name='card_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.card'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='view',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, null=True), blank=True, null=True, size=None),
        ),
    ]
