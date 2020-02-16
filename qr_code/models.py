from django.db import models
from django.contrib.auth.models import User

def productFile(instance, filename):
    return '/'.join(['photos', filename])

# Create your models here.
class LinksMetadata(models.Model):
    user = models.ForeignKey('auth.User', related_name='links', on_delete=models.CASCADE)
    lastUpdatedTime = models.DateTimeField(auto_now_add=True)
    facebook_link = models.URLField(max_length=200, null=True)
    linkedin_link = models.URLField(max_length=200, null=True)
    resume_link = models.URLField(max_length=200, null=True)
    github_link = models.URLField(max_length=200, null=True)
    twitter_link = models.URLField(max_length=200, null=True)
    pinterest_link = models.URLField(max_length=200, null=True)
    portfolio_link = models.URLField(max_length=200, null=True)
    instagram_link = models.URLField(max_length=200, null=True)
    phone_number = models.TextField(max_length=200, null=True)
    email_address = models.TextField(max_length=200, null=True)

class SecondaryLinksMetadata(models.Model):
    user = models.ForeignKey('auth.User', related_name='secondarylinks', on_delete=models.CASCADE)
    lastUpdatedTime = models.DateTimeField(auto_now_add=True)
    facebook_link = models.URLField(max_length=200, null=True)
    linkedin_link = models.URLField(max_length=200, null=True)
    resume_link = models.URLField(max_length=200, null=True)
    github_link = models.URLField(max_length=200, null=True)
    twitter_link = models.URLField(max_length=200, null=True)
    pinterest_link = models.URLField(max_length=200, null=True)
    portfolio_link = models.URLField(max_length=200, null=True)
    instagram_link = models.URLField(max_length=200, null=True)
    phone_number = models.TextField(max_length=200, null=True)
    email_address = models.TextField(max_length=200, null=True)

class QrcodeImage(models.Model):
    lastUpdatedTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='qrcode', on_delete=models.CASCADE)
    image = models.ImageField(
            max_length=254, blank=True, null=True
        )

class InteractionNotes(models.Model):
    lastUpdatedTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='interactionnotes', on_delete=models.CASCADE)
    other_user = models.TextField(max_length=200, null=True)
    interaction_notes = models.TextField(null=True)

class LinksDatabaseChoice(models.Model):
    lastUpdatedTime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='linkschoice', on_delete=models.CASCADE)
    links_choice = models.IntegerField(default=1)