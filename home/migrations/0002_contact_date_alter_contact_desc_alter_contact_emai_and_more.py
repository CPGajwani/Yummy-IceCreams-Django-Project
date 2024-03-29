# Generated by Django 4.2.3 on 2023-07-29 21:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='emai',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=150),
        ),
    ]
