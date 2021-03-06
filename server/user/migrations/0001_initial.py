# Generated by Django 4.0.5 on 2022-06-23 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_phone', models.PositiveIntegerField()),
                ('student_email', models.EmailField(max_length=254)),
                ('student_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=200)),
                ('teacher_phone', models.PositiveIntegerField(blank=True, null=True)),
                ('teacher_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('teacher_address', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parents_name', models.CharField(max_length=200)),
                ('parents_phone', models.PositiveBigIntegerField()),
                ('parents_address', models.CharField(max_length=200)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user.student')),
            ],
        ),
    ]
