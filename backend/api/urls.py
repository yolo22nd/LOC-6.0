from django.urls import path
from .views import *

urlpatterns = [
    path('fetchall/', FetchAllData.as_view(), name='fetch_all'),
    path('fetchfiltered/', FetchFilteredData.as_view(), name='fetch_filtered')
]