# Generated by Django 2.2.2 on 2020-04-03 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_inspector_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoiceinfo',
            old_name='logo',
            new_name='logoComp',
        ),
    ]