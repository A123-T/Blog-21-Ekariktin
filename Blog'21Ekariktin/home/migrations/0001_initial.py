# Generated by Django 3.2.4 on 2021-07-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('query', models.TextField(max_length=255)),
            ],
        ),
    ]
