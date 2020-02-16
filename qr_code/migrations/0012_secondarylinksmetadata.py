# Generated by Django 2.2.6 on 2019-10-21 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qr_code', '0011_interactionnotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondaryLinksMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastUpdatedTime', models.DateTimeField(auto_now_add=True)),
                ('facebook_link', models.URLField(null=True)),
                ('linkedin_link', models.URLField(null=True)),
                ('resume_link', models.URLField(null=True)),
                ('github_link', models.URLField(null=True)),
                ('twitter_link', models.URLField(null=True)),
                ('pinterest_link', models.URLField(null=True)),
                ('portfolio_link', models.URLField(null=True)),
                ('instagram_link', models.URLField(null=True)),
                ('phone_number', models.TextField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secondarylinks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
