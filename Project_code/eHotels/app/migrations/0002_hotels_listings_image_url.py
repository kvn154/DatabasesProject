# Generated by Django 4.1.7 on 2023-03-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels_listings',
            name='image_url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]