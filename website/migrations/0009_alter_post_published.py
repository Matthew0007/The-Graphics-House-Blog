# Generated by Django 3.2.3 on 2021-06-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_usersession_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]