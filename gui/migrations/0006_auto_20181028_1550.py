# Generated by Django 2.1.1 on 2018-10-28 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0005_auto_20181027_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textmessage',
            options={'ordering': ['talktime']},
        ),
        migrations.AlterField(
            model_name='textmessage',
            name='talktime',
            field=models.DateField(),
        ),
    ]