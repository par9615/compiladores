from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'setup', views.setup, name='setup'),
	url(r'getRules', views.getRules, name="rules"),
	url(r'setMatrix', views.setMatrix , name="matrix")
]