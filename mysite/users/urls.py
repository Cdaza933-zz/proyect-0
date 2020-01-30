from django.conf.urls import url
from django.urls import path

from users.views import add_user_view, login_view

urlpatterns = [
    url(r'^login', login_view, name='login'),
    url(r'^register', add_user_view, name='register'),
]
