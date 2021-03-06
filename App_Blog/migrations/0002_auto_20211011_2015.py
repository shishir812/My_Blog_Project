# Generated by Django 3.0.5 on 2021-10-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-publish_date',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',)},
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=264, unique=True),
        ),
    ]
