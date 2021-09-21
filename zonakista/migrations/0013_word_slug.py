# Generated by Django 3.2.7 on 2021-09-21 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonakista', '0012_auto_20210921_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='slug',
            field=models.SlugField(blank=True, help_text='How this word will appear in URLs. Leave blank to auto-generate.', max_length=255, unique=True),
        ),
    ]
