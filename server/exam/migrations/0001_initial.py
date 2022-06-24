# Generated by Django 4.0.5 on 2022-06-23 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.student')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='subject.subject')),
            ],
        ),
    ]