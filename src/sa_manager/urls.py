from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('sa_api',
    url(r'^$',
        views.index_view,
        name='manager_index'),
    url(r'^places/$',
        views.places_view,
        name='manager_place_list'),
    url(r'^places/new/$',
        views.NewPlaceView.as_view(),
        name='manager_place_create'),
    url(r'^places/(?P<pk>\d+)/$',
        views.ExistingPlaceView.as_view(),
        name='manager_place_detail'),
    url(r'^places/(?P<place_id>\d+)/(?P<submission_type>[^/]+)/$',
        views.SubmissionListView.as_view(),
        name='manager_place_submission_list'),
    url(r'^places/(?P<place_id>\d+)/(?P<submission_type>[^/]+)/new/$',
        views.NewSubmissionView.as_view(),
        name='manager_place_submission_create'),
    url(r'^places/(?P<place_id>\d+)/(?P<submission_type>[^/]+)/(?P<pk>\d+)/$',
        views.ExistingSubmissionView.as_view(),
        name='manager_place_submission_detail'),
)