# Generated by Django 2.1 on 2020-04-11 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_auto_20200411_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='image',
            field=models.CharField(default='img.jpg', max_length=50),
        ),
    ]
