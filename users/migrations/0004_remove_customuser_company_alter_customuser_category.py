# Generated by Django 4.0 on 2021-12-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='company',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='category',
            field=models.CharField(choices=[('Sale', 'SALES_CONTACT'), ('Support', 'SUPPORT_CONTACT')], max_length=32),
        ),
    ]