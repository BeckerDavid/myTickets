# Generated by Django 3.0.2 on 2020-01-11 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTickets', '0002_auto_20200111_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='contributor',
            field=models.ManyToManyField(blank=True, to='myTickets.Person'),
        ),
    ]
