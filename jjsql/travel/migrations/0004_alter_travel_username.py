# Generated by Django 3.2.5 on 2021-07-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_remove_travel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]