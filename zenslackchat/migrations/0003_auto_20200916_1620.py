# Generated by Django 3.1.1 on 2020-09-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zenslackchat', '0002_auto_20200916_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='zendeskapp',
            name='token_type',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='zendeskapp',
            name='access_type',
            field=models.CharField(default='', max_length=50),
        ),
    ]
