# Generated by Django 3.2.7 on 2021-09-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zonakista', '0014_alter_sense_wordclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The name of the link as it will appear in the homepage.', max_length=128, unique=True)),
                ('summary', models.CharField(blank=True, help_text="A small description of the link, which will appear below the link's title.", max_length=255)),
                ('url', models.CharField(help_text='The name of the view to which the link should point.', max_length=128)),
                ('slug', models.CharField(blank=True, help_text='The slug, if any, that should be used for reverse-generating the link.', max_length=255)),
            ],
        ),
    ]
