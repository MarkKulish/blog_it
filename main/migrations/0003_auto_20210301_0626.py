# Generated by Django 3.1 on 2021-03-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='', upload_to='post'),
            preserve_default=False,
        ),
    ]
