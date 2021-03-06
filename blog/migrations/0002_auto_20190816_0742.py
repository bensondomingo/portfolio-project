# Generated by Django 2.2.4 on 2019-08-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='post_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='post_body',
        ),
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default='Blog post body', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
