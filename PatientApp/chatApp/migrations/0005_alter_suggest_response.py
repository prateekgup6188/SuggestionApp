# Generated by Django 3.2.4 on 2021-06-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0004_alter_suggest_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggest',
            name='response',
            field=models.TextField(),
        ),
    ]