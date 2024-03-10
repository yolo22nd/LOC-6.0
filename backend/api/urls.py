from django.urls import path, include
from .views import *

urlpatterns = [
    path('api/', include('api.api.urls')),
    path('fetchall/', FetchAllData.as_view(), name='fetch_all'),
    path('fetchfiltered/', FetchFilteredData.as_view(), name='fetch_filtered'),
    path('compare/', ProductComparison.as_view(), name='compare_products'),
    path('compare/previous', PreviousComparisons.as_view({'get' : 'list'}), name='previous_comparisons'),
    path('compare/all', AllComparisons.as_view({'get' : 'list'}), name='compare_all'),
    path('wishlist/add/', WishlistAdd.as_view(), name='wishlist-add'),
    path('wishlist/view/', WishlistView.as_view({'get': 'list'}), name='wishlist-view'),
    path('searchhistory/', SearchHistoryView.as_view(), name='search_history'),
    path('searchhistory/user', UserSearchHistory.as_view({'get': 'list'}), name='user_search_history'),
]