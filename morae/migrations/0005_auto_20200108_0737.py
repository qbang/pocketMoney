# Generated by Django 2.2.4 on 2020-01-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morae', '0004_auto_20200108_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='gphoto',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='family',
            name='tphoto',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
