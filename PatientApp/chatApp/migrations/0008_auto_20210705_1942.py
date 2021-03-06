# Generated by Django 2.2.8 on 2021-07-05 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0007_suggest_intent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accuracy_DB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('text', models.TextField()),
                ('intent', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='suggest',
            name='intent',
        ),
        migrations.AddField(
            model_name='suggest',
            name='note_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='suggest',
            name='patient_id',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
