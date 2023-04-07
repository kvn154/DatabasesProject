# Generated by Django 4.1.7 on 2023-04-07 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_payement_card_info_alter_reservation_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('ssa', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='works_for',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
            ],
        ),
    ]