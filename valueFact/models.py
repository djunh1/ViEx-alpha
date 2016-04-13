from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db.models import permalink
from django.contrib.auth.models import User




'''
TO DO-

1- Write Units tests
2- Each of these must tie into a stock symbol.

'''

# Provides form to search for a stock.
class Stock(models.Model):
    text = models.TextField(default='')


class ValueFactManager(models.Manager):
    def get_queryset(self):
        return super(ValueFactManager, self).get_queryset().filter(status='published')


class ValueFactPost(models.Model):
    value_fact_category = (
        ('overall_business', 'Overall_Business'),
        ('management_assessment', 'Management_Assessment'),
        ('gaap_financials', 'GAAP Financials'),
        ('customer_assessment', 'Customer_Assessment'),
        ('product_assessment', 'Product_Assessment'),
        ('industry_assessment', 'Industry_Assessment'),
        ('future_growth_outlook', 'Future_Growth_Outlook'),
    )
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='valueFact_posts') #possible bug, check name
    publish = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft')
    category = models.CharField(max_length=25,
                                choices=value_fact_category,
                                default='overall_business')
    stockSymbol = models.ForeignKey('Symbol', null=True )
    points = models.IntegerField(default=0, db_column='score')
    vote_up_count = models.IntegerField(default=0)
    vote_down_count = models.IntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)
    endorsed = models.BooleanField(default=False, db_index=True)
    endorsed_by = models.ForeignKey(User, null=True, blank=True, related_name='endorsed_posts')
    endorsed_at = models.DateTimeField(null=True, blank=True)

    objects = models.Manager()
    published = ValueFactManager()

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('companies:valuefact_detail', kwargs={
            'year':self.publish.year,
            'post': self.slug })



class Symbol(models.Model):
    exchange_id = models.IntegerField(blank=True, null=True)
    ticker = models.CharField(max_length=32)
    instrument = models.CharField(max_length=64)
    name = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    currency = models.CharField(max_length=32, blank=True, null=True)
    created_date = models.DateTimeField()
    last_updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'symbol'

    def __str__(self):
        return '%s' %self.name

    def get_absolute_url(self):
        return reverse('companies:view_stock', kwargs={'symbol': self.ticker})


class Comment(models.Model):
    post = models.ForeignKey(ValueFactPost, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return'Contributed by {} on {}'.format(self.name, self.post)