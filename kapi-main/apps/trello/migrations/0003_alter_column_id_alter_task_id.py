# Generated by Django 4.2.7 on 2023-11-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0002_alter_column_id_alter_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]
