# Generated by Django 3.1.1 on 2020-10-22 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userType',
            field=models.CharField(choices=[('AD', 'admin'), ('AN', 'analyst')], max_length=50),
        ),
    ]
