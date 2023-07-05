# Generated by Django 4.2.2 on 2023-07-03 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=20)),
                ('studentName', models.CharField(max_length=100)),
                ('studentEmail', models.EmailField(max_length=254)),
                ('studentContact', models.CharField(max_length=10)),
            ],
        ),
    ]
