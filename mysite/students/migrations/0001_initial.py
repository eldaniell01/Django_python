# Generated by Django 4.2.7 on 2023-12-03 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('curse', models.CharField(max_length=50)),
                ('gpa', models.FloatField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
