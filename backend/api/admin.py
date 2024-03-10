from django.contrib import admin
from .models import *

# Register your models here.

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'timestamp') 

class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'query', 'timestamp') 

class ComparisonAdmin(admin.ModelAdmin):
    list_display = ('user', 'product1', 'product2', 'timestamp') 


admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(SearchHistory, SearchHistoryAdmin)
admin.site.register(Comparison, ComparisonAdmin)