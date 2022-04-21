# Generated by Django 4.0.3 on 2022-04-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_done', '-created_at']},
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
