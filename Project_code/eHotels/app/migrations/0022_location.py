# Generated by Django 4.1.7 on 2023-04-08 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_reservation_archive_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.reservation')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
            ],
        ),
    ]