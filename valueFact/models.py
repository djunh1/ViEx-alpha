from django.db import models
from django.utils import timezone

'''
TO DO-

1- Write Units tests
2- Each of these must tie into a stock symbol.
3- Design the posts for this site.  For now, generic post to get the point..
'''

class ValueFactPost(models.Model):
    value_fact_category = (
        (1, u'Overall Business'),
        (2, u'Management Assessment'),
        (3, u'GAAP Financials'),
        (4, u'Customer Assessment'),
        (5, u'Product Assessment'),
        (6, u'Industry Assessment'),
        (7, u'Future Growth Outlook'),
    )
    '''A fact'''
    title = models.CharField(max_length=300)
    author = models.ForeignKey('accounts.User') #Need to tie into a stock Eventually
    published_date = models.DateTimeField(blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    #Status of post

    #Voting data
    score=models.IntegerField(default=0)



    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title
