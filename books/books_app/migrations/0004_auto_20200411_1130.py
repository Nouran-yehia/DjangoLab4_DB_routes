# Generated by Django 2.1 on 2020-04-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0003_books_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.FileField(default='img.jpg', max_length=50, upload_to=''),
        ),
    ]