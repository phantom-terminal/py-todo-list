# Generated by Django 4.0.3 on 2022-04-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_task_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]