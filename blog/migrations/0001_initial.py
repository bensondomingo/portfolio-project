# Generated by Django 2.2.4 on 2019-08-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('publication_date', models.DateField()),
                ('post_body', models.TextField(max_length=100)),
                ('post_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]