# Generated by Django 4.0.3 on 2022-04-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_task_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tag',
            field=models.ManyToManyField(related_name='tags', to='app.tag'),
        ),
    ]
