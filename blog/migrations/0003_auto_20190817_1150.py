# Generated by Django 2.2.4 on 2019-08-17 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190816_0742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='publication_date',
            new_name='pub_date',
        ),
    ]