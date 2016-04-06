from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from valueFact.models import ValueFactPost


class LatestPostsFeed(Feed):
    title = "Contributions from members"
    link = "/companies/"
    description = "New Contributions by members"

    def items(self):
        return ValueFactPost.objects.order_by('-publish')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)