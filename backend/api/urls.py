from django.urls import path, include
from .views import *

urlpatterns = [
    path('jwt_auth/', include('api.jwt_auth.urls')),
    path('fetchall/', FetchAllData.as_view(), name='fetch_all'),
    path('fetchfiltered/', FetchFilteredData.as_view(), name='fetch_filtered'),
    path('compare/', ProductComparison.as_view(), name='compare_products'),
    path('wishlist/add/', WishlistAdd.as_view(), name='wishlist-add'),
    path('wishlist/view/', WishlistView.as_view({'get': 'list'}), name='wishlist-view'),
]