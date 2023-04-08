# Generated by Django 4.1.7 on 2023-04-07 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_employee_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservation_archive',
            fields=[
                ('reservation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.reservation')),
            ],
            options={
                'managed': False,
            },
            bases=('app.reservation',),
        ),
    ]