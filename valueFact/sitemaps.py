from django.contrib.sitemaps import Sitemap
from valueFact.models import ValueFactPost

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ValueFactPost.published.all()

    def lastmod(self, obj):
        return obj.publish