# Generated by Django 4.0 on 2021-12-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_updated',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='payment_due',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_updated',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
    ]