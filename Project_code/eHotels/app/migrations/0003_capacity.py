# Generated by Django 4.1.7 on 2023-04-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_hotel_numberofrooms_hotel_chain_numberofhotels'),
    ]

    operations = [
        migrations.CreateModel(
            name='capacity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('capacity', models.CharField(max_length=50)),
            ],
        ),
    ]