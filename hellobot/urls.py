from django.conf.urls import patterns, include, url
from django.contrib import admin

from chatbot.views import MyChatBotView, index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index),
    #url(r'', 'chatbot.views.index'),
    url(r'^facebook_auth/?$', MyChatBotView.as_view()),
)