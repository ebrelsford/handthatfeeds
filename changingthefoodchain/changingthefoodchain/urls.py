from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from moderation.helpers import auto_discover as moderation_autodiscover

from news.views import CategoryList, EntryList
from organizations.views import OrganizationList, SectorList, TypeList

admin.autodiscover()
moderation_autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^contact/', include('contact.urls')),
    url(r'^content/', include('content.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^organizations/', include('organizations.urls')),
    url(r'^organizations', OrganizationList.as_view()),

    url(r'^entries/', include('news.entry_urls')),
    url(r'^entries/', EntryList.as_view()),
    url(r'^entries', EntryList.as_view()),
    url(r'^categories$', CategoryList.as_view()),
    url(r'^sectors', SectorList.as_view()),
    url(r'^types', TypeList.as_view()),

    # Django REST Framework
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

    # FeinCMS
    url(r'', include('feincms.urls')),
) + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
    (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)))
