from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views import generic
#from . import views
from blog.models import Article

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', generic.TemplateView.as_view(template_name="index.html"), name="index"),
    #url(r'^articles', views.articles_list, name="articles_list"),
    url(r'^articles/$', generic.ListView.as_view(model=Article), name="article_list"),
    url(r'^markdown/', include( 'django_markdown.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
