# Generated by Django 4.1.7 on 2023-05-01 07:31

import django.core.validators
from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('code', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(9, message='Code must be exactly nine digits')])),
                ('region', models.CharField(max_length=9, validators=[web.models.validate_nonzero])),
                ('parish', models.CharField(choices=[('Acadia', 'Acadia'), ('Allen', 'Allen'), ('Ascension', 'Ascension'), ('Assumption', 'Assumption'), ('Avoyelles', 'Avoyelles'), ('Beauregard', 'Beauregard'), ('Bienville', 'Bienville'), ('Bossier', 'Bossier'), ('Caddo', 'Caddo'), ('Calcasieu', 'Calcasieu'), ('Caldwell', 'Caldwell'), ('Cameron', 'Cameron'), ('Catahoula', 'Catahoula'), ('Claiborne', 'Claiborne'), ('Concordia', 'Concordia'), ('De Soto', 'De Soto'), ('East Baton Rouge', 'East Baton Rouge'), ('East Carroll', 'East Carroll'), ('East Feliciana', 'East Feliciana'), ('Evangeline', 'Evangeline'), ('Franklin', 'Franklin'), ('Grant', 'Grant'), ('Iberia', 'Iberia'), ('Iberville', 'Iberville'), ('Jackson', 'Jackson'), ('Jefferson', 'Jefferson'), ('Jefferson Davis', 'Jefferson Davis'), ('Lafayette', 'Lafayette'), ('Lafourche', 'Lafourche'), ('LaSalle', 'LaSalle'), ('Lincoln', 'Lincoln'), ('Livingston', 'Livingston'), ('Madison', 'Madison'), ('Morehouse', 'Morehouse'), ('Natchitoches', 'Natchitoches'), ('Orleans', 'Orleans'), ('Ouachita', 'Ouachita'), ('Plaquemines', 'Plaquemines'), ('Pointe Coupee', 'Pointe Coupee'), ('Rapides', 'Rapides'), ('Red River', 'Red River'), ('Richland', 'Richland'), ('Sabine', 'Sabine'), ('St. Bernard', 'St. Bernard'), ('St. Charles', 'St. Charles'), ('St. Helena', 'St. Helena'), ('St. James', 'St. James'), ('St. John the Baptist', 'St. John the Baptist'), ('St. Landry', 'St. Landry'), ('St. Martin', 'St. Martin'), ('St. Mary', 'St. Mary'), ('St. Tammany', 'St. Tammany'), ('Tangipahoa', 'Tangipahoa'), ('Tensas', 'Tensas'), ('Terrebonne', 'Terrebonne'), ('Union', 'Union'), ('Vermilion', 'Vermilion'), ('Vernon', 'Vernon'), ('Washington', 'Washington'), ('Webster', 'Webster'), ('West Baton Rouge', 'West Baton Rouge'), ('West Carroll', 'West Carroll'), ('West Feliciana', 'West Feliciana'), ('Winn', 'Winn')], max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('approval_from_RMD', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('vaccines_offered', models.CharField(choices=[('COVID', 'COVID'), ('FLU', 'FLU'), ('M POX', 'M POX')], max_length=5)),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('working', 'Working'), ('cancelled', 'Cancelled')], max_length=9)),
                ('num_of_doses', models.PositiveIntegerField()),
                ('num_of_doses_administered', models.PositiveIntegerField()),
                ('patient_edu_res_brought', models.PositiveIntegerField()),
                ('patient_edu_res_distributed', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', web.models.CustomeUserManager()),
            ],
        ),
    ]
