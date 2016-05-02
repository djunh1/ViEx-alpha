from django.contrib import admin

from .models import ValueFactPost, Symbol, Comment


class StockAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'instrument', 'name', 'sector')
    list_filter = ('name', 'ticker', 'instrument')
    search_fields = ('ticker', 'name')
    ordering = ['ticker', 'name']

class ValueFactAdmin(admin.ModelAdmin):
    list_display = ('stock','stockTicker',  'title', 'category', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

admin.site.register(Comment, CommentAdmin)
admin.site.register(ValueFactPost, ValueFactAdmin)
admin.site.register(Symbol, StockAdmin)
