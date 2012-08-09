from django.conf import settings
from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
from django.shortcuts import redirect
from django.views.decorators.cache import cache_page
from django.views.i18n import javascript_catalog

import amo
from apps.users.views import logout
from apps.users.urls import (detail_patterns as user_detail_patterns,
                             users_patterns as users_users_patterns)
from mkt.account.urls import (purchases_patterns, settings_patterns,
                              users_patterns as mkt_users_patterns)
from mkt.purchase.urls import bluevia_services_patterns
from mkt.themes.urls import theme_patterns
from mkt.developers.views import login

admin.autodiscover()

handler404 = 'mkt.site.views.handler404'
handler500 = 'mkt.site.views.handler500'

ADDON_ID = r"""(?P<addon_id>[^/<>"']+)"""

urlpatterns = patterns('',
    # Home.
    # NOTICE: This is just a placeholder until the carrier stores middleware
    # goes live with regional stores.
    url('^(?:telefonica/)?$', 'mkt.home.views.home', name='home'),

    # App Detail pages.
    ('^app/%s/' % amo.APP_SLUG, include('mkt.detail.urls')),

    # Browse pages.
    ('^apps/', include('mkt.browse.urls')),

    # Dev Ecosystem
    ('^developers/', include('mkt.ecosystem.urls')),
    ('^ecosystem/', lambda r: redirect('ecosystem.landing', permanent=True)),

    # Theme detail pages.
    ('^theme/%s/' % ADDON_ID, include('mkt.themes.urls')),

    # Theme browse pages.
    ('^themes/', include(theme_patterns)),

    # Replace the "old" Developer Hub with the "new" Marketplace one.
    ('^developers/', include('mkt.developers.urls')),

    # Submission.
    ('^developers/submit/app/', include('mkt.submit.urls')),

    # In-app payments.
    ('^inapp-pay/', include('mkt.inapp_pay.urls')),

    # Site events data.
    url('^statistics/events-(?P<start>\d{8})-(?P<end>\d{8}).json$',
        'stats.views.site_events', name='amo.site_events'),

    # Site statistics that we are going to catch, the rest will fall through.
    url('^statistics/', include('stats.urls')),

    # Fall through for any URLs not matched above stats dashboard.
    url('^statistics/', lambda r: redirect('/'), name='statistics.dashboard'),

    # Support (e.g., refunds, FAQs).
    ('^support/', include('mkt.support.urls')),

    # Users (Legacy).
    ('^user/(?P<user_id>\d+)/', include(user_detail_patterns)),
    ('^users/', include(users_users_patterns)),

    # Account info (e.g., purchases, settings).
    ('^users/', include(mkt_users_patterns)),
    ('^purchases/', include(purchases_patterns)),
    ('^settings', include(settings_patterns)),

    # Site Search.
    ('^search/', include('mkt.search.urls')),

    # Reviewer tools.
    ('^reviewers/', include('mkt.reviewers.urls')),

    # Account lookup.
    ('^lookup/', include('mkt.lookup.urls')),

    # Javascript translations.
    url('^jsi18n.js$', cache_page(60 * 60 * 24 * 365)(javascript_catalog),
        {'domain': 'javascript', 'packages': ['zamboni']}, name='jsi18n'),

    # BlueVia / nav.pay() services.
    ('^services/bluevia/', include(bluevia_services_patterns)),

    # Paypal, needed for IPNs only.
    ('^services/', include('paypal.urls')),

    # AMO admin (not django admin).
    ('^admin/', include('zadmin.urls')),

    # AMO Marketplace admin (not django admin).
    ('^admin/', include('mkt.zadmin.urls')),

    # Accept extra junk at the end for a cache-busting build id.
    url('^addons/buttons.js(?:/.+)?$', 'addons.buttons.js'),

    # Developer Registration Login.
    url('^login$', login, name='users.login'),
    url('^logout$', logout, name='users.logout'),

    url('^api/', include('mkt.api.urls')),

    url('^appcache/', include('django_appcache.urls')),

    # Try and keep urls without a prefix at the bottom of the list for
    # minor performance reasons.

    # Misc pages.
    ('', include('mkt.site.urls')),

    # Services.
    ('', include('apps.amo.urls')),
)

if settings.TEMPLATE_DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )


if settings.SERVE_TMP_PATH and settings.DEBUG:
    # Serves any URL like /tmp/* from your local ./tmp/ dir
    urlpatterns += patterns('',
        (r'^tmp/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.TMP_PATH}),
    )
