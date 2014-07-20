from django.conf.urls import patterns,include,url
from django.views.generic import ListView,DetailView
from dps.views import *
from dps.models import Orders,Users,DeliverClient
urlpatterns =patterns('',
						 url(r'^$',ListView.as_view(
												 queryset = Users.objects.all().order_by("username")[:20],
												 template_name="dps.html")),
						url(r'^(?P<pk>\d+)$',DetailView.as_view(
												model = Users,
												template_name="post.html")),
						url(r'^userdetail/$',ListView.as_view(
												queryset = Users.objects.all().order_by("-id"),
												template_name="latestnews.html")),
						url(r'^orderdetail/$',ListView.as_view(
												queryset = Orders.objects.all().order_by("customer")[:5],
												template_name="posttitleslist.html")),
						# url(r'^login/$',ListView.as_view(
												# queryset = Users.objects.all().order_by("id")[:3],
												# template_name="login.html")),
						url(r'^login/$',login),
						url(r'^form/$',TakeForm ),
						url(r'^signup/$',signup ),
						url(r'^home/$',my_view),
						# url(r'^form/$',ListView.as_view(
												# queryset = Users.objects.all().order_by("username")[:5],
												# template_name="form.html")),
						#url(r'^form/$', 'dps.views.TakeForm'),



	)
