from django.urls import path, re_path, include
# from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.search, name='index'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),

    # call search query with optional parameters 
    path('search/<str:query_string>', views.query, kwargs={'disease': 0, 'drug': 0, 'variant': 0, 'gene': 0}, name='query'),
    path('search_details/<str:search_type>/<str:query_id>', views.search_details, name='search_details'),
    path('summary/', views.summary, name='summary'),
    path('resources/', views.resources, name='resources'),
    path('outreach/', views.outreach, name='outreach'),
    path('contact/', views.contact, name='contact'),

    path('agnocomplete/', include('agnocomplete.urls')),
]
