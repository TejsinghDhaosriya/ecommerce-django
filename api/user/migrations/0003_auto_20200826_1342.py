# Generated by Django 3.0.3 on 2020-08-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200826_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='session_token',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]