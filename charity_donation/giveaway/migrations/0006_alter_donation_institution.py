# Generated by Django 4.1.5 on 2023-01-22 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0005_alter_donation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giveaway.institution'),
        ),
    ]
