# Generated by Django 2.1.5 on 2019-02-09 14:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FoodSwarm', '0002_auto_20190209_2231'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='FoodStalls',
            new_name='FoodStall',
        ),
    ]
