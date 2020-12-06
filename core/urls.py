from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # re_path(r'^phone_login/', include('phone_login.urls', name='phone_login'),),
]
