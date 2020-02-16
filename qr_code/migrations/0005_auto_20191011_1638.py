# Generated by Django 2.2.6 on 2019-10-11 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qr_code', '0004_qrcodeimage_lastupdatedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linksmetadata',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='qrcodeimage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qrcode', to=settings.AUTH_USER_MODEL),
        ),
    ]
