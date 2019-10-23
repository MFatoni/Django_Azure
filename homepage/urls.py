from django.urls import re_path
from django.conf.urls.static import static
from homepage import views as homepage

urlpatterns=[
	re_path(r'^$',homepage.index,name='index'),
	re_path(r'^DataPost',homepage.form_post, name='submit'),
	re_path(r'^DataGet',homepage.data_get, name='data'),
]