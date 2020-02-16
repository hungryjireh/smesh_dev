# Generated by Django 2.2.6 on 2019-10-10 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LinksMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastUpdatedTime', models.DateTimeField(auto_now_add=True)),
                ('facebook_link', models.TextField(max_length=200, null=True)),
                ('linkedin_link', models.TextField(max_length=200, null=True)),
                ('resume_link', models.TextField(max_length=200, null=True)),
                ('github_link', models.TextField(max_length=200, null=True)),
                ('twitter_link', models.TextField(max_length=200, null=True)),
                ('pinterest_link', models.TextField(max_length=200, null=True)),
                ('portfolio_link', models.TextField(max_length=200, null=True)),
                ('instagram_link', models.TextField(max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
