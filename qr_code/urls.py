from django.urls import include, path
from qr_code import views
from django.conf.urls import url
from rest_framework import routers
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import TemplateView # new
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='users')
router.register(r'links', views.LinksMetadataView, base_name='links')
router.register(r'secondary-links', views.SecondaryLinksMetadataView, base_name='secondarylinks')
router.register(r'qrcode', views.QrcodeImageView, base_name='qrcode')
router.register(r'interaction-notes', views.InteractionNotesView, base_name='interactionnotes')
router.register(r'links-choice', views.LinksDatabaseChoiceView, base_name='linkschoice')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('admin-home/', include(router.urls)),
    path('', TemplateView.as_view(template_name='navigationguide.html'), name='home'),
    path('signup/', views.register_user, name='signup'),
    path('admin-home/users/<int:pk>/', views.UserDetail.as_view(), name='users-detail'),
    path('admin-home/links/<int:pk>/', views.LinksMetadataDetail.as_view(), name='links-detail'),
    path('admin-home/secondary-links/<int:pk>/', views.SecondaryLinksMetadataDetail.as_view(), name='secondarylinks-detail'),
    path('admin-home/qrcode/<int:pk>/', views.QrcodeImageDetail.as_view(), name='qrcodeimage-detail'),
    path('admin-home/interaction-notes/<int:pk>/', views.InteractionNotesDetail.as_view(), name='interactionnotes-detail'),
    path('admin-home/links-choice/<int:pk>/', views.LinksDatabaseChoiceDetail.as_view(), name='linksdbchoice-detail'),
    url('users/(?P<username>[^/]+)/$', views.index, name="user"),
    url('interaction-notes/(?P<username>[^/]+)/$', views.interaction_notes, name="interaction-notes"),
    path('links/', views.links_form, name='links'),
    path('qrcode/', views.generate_qrcode, name='qrcode'),
    path('connections/', views.all_friends, name='connections'),
    path('manage-connections/', views.friends_management, name='manage-connections'),
    path('json-user', views.json_user, name="json-user"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)