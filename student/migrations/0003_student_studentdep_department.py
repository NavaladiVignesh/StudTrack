# Generated by Django 4.2.2 on 2023-07-04 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_studentcontact_alter_student_studentid'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentdep',
            field=models.CharField(default='NULL', max_length=4),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentdep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]