# Generated by Django 3.2.11 on 2022-02-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='im',
            field=models.ImageField(default='dd', upload_to='imag'),
            preserve_default=False,
        ),
    ]
