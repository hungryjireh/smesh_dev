from rest_framework import serializers  
from django.contrib.auth.models import User
from qr_code.models import LinksMetadata, QrcodeImage, InteractionNotes, SecondaryLinksMetadata, LinksDatabaseChoice

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only = True,
    )
    confirm_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only = True,
    )
    date_joined = serializers.DateTimeField(read_only=True ,format="%Y-%m-%d %H:%M:%S")
    last_login = serializers.DateTimeField(read_only=True ,format="%Y-%m-%d %H:%M:%S")
    url = serializers.HyperlinkedIdentityField(view_name='users-detail', read_only=True)
    email_sent=True
    class Meta:
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'url': {'view_name': 'user-detail'},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
            'username': {'required': True},
        }
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'last_login', 'date_joined', 'username', 'url')

class LinksMetadataSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='links-detail', read_only=True)
    lastUpdatedTime = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = LinksMetadata
        ordering = ['-lastUpdatedTime']
        fields = ('lastUpdatedTime', 'user', 'facebook_link', 'linkedin_link', 'resume_link', 'github_link', 'twitter_link', 'pinterest_link', 'portfolio_link', 'instagram_link', 'phone_number', 'email_address', 'url')

class SecondaryLinksMetadataSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='secondarylinks-detail', read_only=True)
    lastUpdatedTime = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = SecondaryLinksMetadata
        ordering = ['-lastUpdatedTime']
        fields = ('lastUpdatedTime', 'user', 'facebook_link', 'linkedin_link', 'resume_link', 'github_link', 'twitter_link', 'pinterest_link', 'portfolio_link', 'instagram_link', 'phone_number', 'email_address', 'url')

class QrcodeImageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='qrcodeimage-detail', read_only=True)
    lastUpdatedTime = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = QrcodeImage
        ordering = ['-lastUpdatedTime']
        fields = ('lastUpdatedTime', 'user', 'image', 'url')

class InteractionNotesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='interactionnotes-detail', read_only=True)
    lastUpdatedTime = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = InteractionNotes
        ordering = ['-lastUpdatedTime']
        fields = ('lastUpdatedTime', 'user', 'other_user', 'interaction_notes', 'url')

class LinksDatabaseChoiceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='linksdbchoice-detail', read_only=True)
    lastUpdatedTime = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = LinksDatabaseChoice
        ordering = ['-lastUpdatedTime']
        fields = ('lastUpdatedTime', 'user', 'links_choice', 'url')