# Generated by Django 4.1.7 on 2023-04-07 17:23

import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservation_archive',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_reservation', models.DateField(blank=True)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('client_id', models.CharField(max_length=100)),
                ('hotel_id', models.IntegerField()),
                ('view', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, null=True), blank=True, null=True, size=None)),
                ('capacity_id', models.IntegerField()),
                ('extrabed', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
            options={
                'db_table': 'app_reservation_archive',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='capacity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('capacity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='card',
            fields=[
                ('card_number', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('expiry_date', models.CharField(max_length=8)),
                ('cvv', models.CharField(max_length=4)),
                ('name_on_the_card', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('ssa', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('ssa', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('hotel_id', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=150)),
                ('zone', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50)),
                ('nTelephones', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('email', models.CharField(max_length=150)),
                ('rating', models.IntegerField()),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('numberOfRooms', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='hotel_chain',
            fields=[
                ('chain_id', models.IntegerField(primary_key=True, serialize=False)),
                ('addressArray', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=150), size=None)),
                ('name', models.CharField(max_length=150)),
                ('nTelephones', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('email', models.CharField(max_length=150)),
                ('rating', models.IntegerField()),
                ('image_url', models.URLField(blank=True, max_length=500, null=True)),
                ('numberOfHotels', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='payement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('card_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.card')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
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
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('extrabed', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('view', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, null=True), blank=True, null=True, size=None)),
                ('capacity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.capacity')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
            ],
            options={
                'unique_together': {('room_number', 'hotel_id')},
            },
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_reservation', models.DateField(blank=True)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('view', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, null=True), blank=True, null=True, size=None)),
                ('extrabed', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('capacity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.capacity')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='payement_for',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.payement')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.reservation')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='chain_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hotel_chain'),
        ),
        migrations.CreateModel(
            name='damage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=250)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
            ],
        ),
        migrations.CreateModel(
            name='commodity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
