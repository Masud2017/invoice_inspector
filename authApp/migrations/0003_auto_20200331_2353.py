# Generated by Django 2.2.2 on 2020-03-31 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authApp', '0002_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profilePic',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.TextField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp', models.TextField(blank=True, max_length=50)),
                ('logo', models.TextField(blank=True)),
                ('emailComp', models.TextField(blank=True)),
                ('addressComp', models.TextField(blank=True)),
                ('phoneNum', models.IntegerField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
