# Generated by Django 4.0.5 on 2022-06-23 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.student')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.teacher')),
            ],
        ),
    ]
