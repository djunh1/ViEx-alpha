from django.contrib import admin

from .models import ValueFactPost, Symbol

class StockAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'instrument', 'name', 'sector')
    list_filter = ('name', 'ticker', 'instrument')
    search_fields = ('ticker', 'name')
    ordering = ['ticker', 'name']

class ValueFactAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(ValueFactPost, ValueFactAdmin)
admin.site.register(Symbol, StockAdmin)
