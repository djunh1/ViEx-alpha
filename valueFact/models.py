from django.db import models
from django.utils import timezone
from accounts.models import User

'''
TO DO-

1- Write Units tests
2- Each of these must tie into a stock symbol.
3- Design the posts for this site.  For now, generic post to get the point..
'''

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
    '''A fact'''
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300,unique_for_date='publish')
    author = models.ForeignKey(User, related_name='valueFact_posts')
    publish = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #Add Foreign Key for stock when stock model is created

    #Status of post

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICE,
                              default='draft')

    category = models.CharField(max_length=25,
                                choices=value_fact_category,
                                default='overall_business')


    points = models.IntegerField(default=0, db_column='score')
    vote_up_count = models.IntegerField(default=0)
    vote_down_count = models.IntegerField(default=0)

    comment_count = models.PositiveIntegerField(default=0)

    #Endorses value Facts

    endorsed = models.BooleanField(default=False, db_index=True)
    endorsed_by = models.ForeignKey(User, null=True, blank=True, related_name='endorsed_posts')
    endorsed_at = models.DateTimeField(null=True, blank=True)


    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title
