# Generated by Django 2.1.1 on 2018-10-27 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0003_auto_20181015_1428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
