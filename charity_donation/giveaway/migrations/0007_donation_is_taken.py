# Generated by Django 4.1.5 on 2023-02-05 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('giveaway', '0006_alter_donation_institution'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='is_taken',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
