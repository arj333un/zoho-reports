# Generated by Django 4.1.7 on 2023-10-20 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0012_customer_saddress1_customer_saddress2_customer_scity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='accountCode',
        ),
    ]
