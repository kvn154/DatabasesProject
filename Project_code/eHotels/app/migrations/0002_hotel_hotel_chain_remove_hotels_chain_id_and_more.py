# Generated by Django 4.1.7 on 2023-03-27 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('hotel_id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50)),
                ('nTelephone', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
                ('image_url', models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='hotel_chain',
            fields=[
                ('chain_id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('nTelephone', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
                ('image_url', models.URLField(blank=True, max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='chain_ID',
        ),
        migrations.DeleteModel(
            name='hotel_chains',
        ),
        migrations.DeleteModel(
            name='hotels',
        ),
        migrations.AddField(
            model_name='hotel',
            name='chain_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel_chain'),
        ),
    ]