# Generated by Django 2.2.6 on 2019-10-11 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('qr_code', '0003_qrcodeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcodeimage',
            name='lastUpdatedTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]