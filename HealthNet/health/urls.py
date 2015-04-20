from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from . import views

# Make sure to end each URL pattern with '/?$' to make sure the end of the url
# properly handles omitting the trailing slash.
urlpatterns = patterns('',
    url(r'login/?$', views.login_view, name='login'),
    url(r'logout/?$', views.logout_view, name='logout'),
    url(r'schedule/?$', views.schedule, name='schedule'),
    url(r'prescriptions/?$', views.prescriptions, name='prescriptions'),
    url(r'messages/?$', views.messages, name='messages'),
    url(r'delete_prescription/(\d+)/?$', views.delete_prescription, name='delete_prescription'),
    url(r'edit_prescription/(\d+)?/?$', views.prescription_form, name='edit_prescription'),
    url(r'add_prescription/?$', views.add_prescription_form, name='add_prescription'),
    url(r'users/(\d+)/?$', views.medical_information, name='medical_information'),
    url(r'users/me/?$', views.my_medical_information, name='my_medical_information'),
    url(r'signup/?$', views.signup, name='signup'),
    url(r'logs/?$', views.logs, name='logs'),
    url(r'^/?$', views.home, name='home'),
)