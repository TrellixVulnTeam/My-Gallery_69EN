# Generated by Django 3.1.5 on 2021-01-11 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_remove_image_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
