# Generated by Django 2.1.5 on 2019-02-08 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(default="I don't know the current status of the Food Stall.", max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FoodStalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(default='N/A')),
                ('location', models.CharField(default='N/A', max_length=50)),
                ('capacity', models.CharField(default='N/A', max_length=15)),
                ('tables', models.CharField(default='N/A', max_length=5)),
                ('chairs', models.CharField(default='N/A', max_length=5)),
                ('operatinghrs', models.CharField(default='N/A', max_length=30)),
                ('peakhrs', models.CharField(default='N/A', max_length=30)),
            ],
        ),
    ]
