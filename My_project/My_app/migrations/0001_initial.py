# Generated by Django 4.2.16 on 2024-10-13 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('year_of_joining', models.IntegerField()),
                ('rollno', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=15)),
                ('place', models.CharField(max_length=50)),
            ],
        ),
    ]
