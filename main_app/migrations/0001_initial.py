# Generated by Django 3.0.5 on 2024-03-19 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('userId', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('completed', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ToDoTable',
            },
        ),
    ]
