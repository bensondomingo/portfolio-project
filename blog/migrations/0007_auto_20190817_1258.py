# Generated by Django 2.2.4 on 2019-08-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190817_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='_pub_date',
            field=models.DateField(verbose_name='Publication Date'),
        ),
    ]
