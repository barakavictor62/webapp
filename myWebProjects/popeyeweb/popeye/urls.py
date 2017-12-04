from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from popeye import views
from popeye.forms import SignupForm


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^pricing', views.pricing, name='pricing'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^myProfile', views.myProfile, name='myProfile'),
    url(r'^edit_profile', views.edit_profile, name='edit_profile'),
    url(r'^web', views.web, name='web'),
    url(r'^articles/$', views.articles, name='articles'),
    url(r'^articles_request/$', views.articles_request, name='articles_request'),
    url(r'^mywallet', views.mywallet, name='wallet'),
    url(r'^test', views.tests, name='test'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.edit_request, name='edit_request')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
