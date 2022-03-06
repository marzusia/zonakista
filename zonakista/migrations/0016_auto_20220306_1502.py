# Generated by Django 3.2.7 on 2022-03-06 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zonakista', '0015_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01', help_text="This citizen's date of birth."),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='citizen',
            name='pseudonym',
            field=models.CharField(blank=True, help_text='Another name by which this citizen may be known, formally or informally.', max_length=128),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='citizenship_start',
            field=models.DateField(help_text='The date upon which this individual became a citizen.'),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='name',
            field=models.CharField(help_text="This citizen's full legal name.", max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='occupation',
            field=models.CharField(blank=True, help_text="This citizen's legal occupation.", max_length=255),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='user',
            field=models.ForeignKey(blank=True, help_text='If this citizen has a corresponding user account, it should be linked here to allow them access to managing their citizenship.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(help_text='The name of the view to which the link should point, or a valid external address beginning with https://', max_length=128),
        ),
    ]
