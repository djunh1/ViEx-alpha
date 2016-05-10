from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.core.mail import send_mail
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#email
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

#Custom
from yahoo_finance import Share
from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from valueFact.forms import EmailPostForm, CommentForm, StockForm, ContactForm
from valueFact.models import ValueFactPost, Symbol, Comment
from valueFact.controller import mySQLdb_query, stat_cleaner, yahoo_cleaner



def home_page(request):
    form = StockForm()
    if request.method == 'GET':
        form = StockForm(data=request.GET)
        if form.is_valid():
            ticker = form.cleaned_data['text']
            return HttpResponseRedirect('companies:view_stock' % ticker)
    return render(request, 'main_page/home.html', {"form": form})


def search_home(request):
    form = StockForm()
    return render(request, 'search/search_home.html', {"form": form})


def get_posts(request, ticker):
    posts = ValueFactPost.objects.all()
    return render(request, 'search/stock_data.html', {"posts": posts})


#helper function
def get_data(request, form, ticker):
    try:
        stocksymbol = Symbol.objects.filter(ticker=ticker)[0]
    except IndexError:
        messages.error(request, 'We could not find %s in our database!  Please try again' % ticker)
        return render(request, 'search/search_start.html', {"form": form})
    else:
        stockShare = Share(yahoo_cleaner(ticker))
        #Data from Yahoo Finance API
        stockPrice = stockShare.get_price()
        stockPriceChange = stockShare.get_change()
        try:
            spcPercent = 100.0*float(stockPriceChange)/float(stockPrice)
        except ZeroDivisionError:
            spcPercent = 0
        EBITDA = stockShare.get_ebitda()
        try:
            PE = float(stockPrice)/float(stockShare.get_earnings_share())
        except ZeroDivisionError:
            PE = 0
        exchange = stockShare.get_stock_exchange()
        mktcap = stockShare.get_market_cap()
        dividend = stockShare.get_dividend_share()
        dividendYield = stockShare.get_dividend_yield()
        plow = stockShare.get_year_low()
        phigh = stockShare.get_year_high()
        epsRecent = stockShare.get_earnings_share()


        #Data from the DB
        stockQueryDb = mySQLdb_query(ticker)
        epsData = stockQueryDb.get_statement_data(stockQueryDb.eps)
        revenue = stockQueryDb.get_statement_data(stockQueryDb.revenue)[0][1]
        EBIT = stockQueryDb.get_statement_data(stockQueryDb.EBIT)[0][1]
        fcfData = stockQueryDb.get_free_cash_flow()
        stockQueryDb.get_netnet_value()
        ncavData = stockQueryDb.get_NCAV()[1]


        #Combined DB and Yahoo API
        try:
            stockMktCap = stat_cleaner(stockShare.get_market_cap())
        except TypeError:
            stockMktCap = 0.0
        netnetData =stockQueryDb.get_netnet_value()[1]
        try:
            fcfYield = 100*float(fcfData[0])/float(stockPrice)
        except ZeroDivisionError:
            fcfYield = 0

        EV = stockQueryDb.get_EV(stockMktCap)
        evEBITDA = EV / stat_cleaner(EBITDA)
        evREV = EV / float(revenue)
        evEBIT = EV / float(EBIT)


        #Gets posts.   this function is getting too large
        qs = ValueFactPost.objects.all()
        posts = qs.filter(stock=stocksymbol)


        return render(request, 'search/stock_data.html', {'price': stockPrice,'change': stockPriceChange,
                                                          'changepercent': spcPercent, 'fcfYield': fcfYield,
                                                          'EV': EV, 'evEBITDA': evEBITDA,'evREV': evREV,
                                                          'evEBIT': evEBIT, 'PE': PE, 'exchange': exchange,
                                                          'mktcap': mktcap, 'dividend': dividend, 'dividendYield':dividendYield,
                                                          'plow': plow, 'phigh': phigh, 'epsRecent': epsRecent,
                                                          'eps': epsData, 'fcf': fcfData,
                                                         'ncav': ncavData, 'netnet': netnetData,
                                                         "form": form, 'stock': stocksymbol,
                                                          "posts": posts})


def view_stock(request, symbol):
    form = StockForm()
    # dry!!
    if request.method == 'POST':
        form = StockForm(data=request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['text']
            return get_data(request, form, ticker)
    else:
        ticker = str(symbol)
        return get_data(request, form, ticker)
    return render(request, 'main_page/home.html', {"form": form})


class valueFactListView(ListView):
    model = ValueFactPost
    template_name = 'posts/manage/post/list.html'

    def get_queryset(self):
        qs = super(valueFactListView, self).get_queryset()
        return qs.filter(author=self.request.user)


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(author=self.request.user)


class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(OwnerEditMixin, self).form_valid(form)


class OwnerPostMixin(OwnerMixin, LoginRequiredMixin):
    model = ValueFactPost


class OwnerPostEditMixin(OwnerPostMixin, OwnerEditMixin):
    fields = ['category', 'title', 'body']

    def form_valid(self, form):

        form.instance.status = 'published'
        form.instance.slug = form.instance.title.replace(" ", "_")
        print(form.instance.slug)
        ticker = self.kwargs['symbol']
        symbolObject = Symbol.objects.filter(ticker=ticker)[0]
        form.instance.stock = symbolObject
        form.instance.stockTicker = symbolObject.ticker
        return super(OwnerPostEditMixin, self).form_valid(form)

    success_url = reverse_lazy('companies:manage_post_list')
    template_name = 'posts/manage/post/form.html'


class ManagePostListView(OwnerPostMixin, ListView):
    template_name = 'posts/manage/post/list.html'


class PostCreateView(PermissionRequiredMixin, OwnerPostEditMixin, CreateView):
    permission_required = 'posts.add_post'


class PostUpdateView(PermissionRequiredMixin, OwnerPostEditMixin, UpdateView):
    permission_required = 'posts.change_post'


class PostDeleteView(PermissionRequiredMixin, OwnerPostMixin, DeleteView):
    template_name = 'posts/manage/post/delete.html'
    success_url = reverse_lazy('companies:manage_post_list')
    permission_required = 'posts.delete_post'


def valuefact_detail(request, stockticker, year, post):
    post = get_object_or_404(ValueFactPost, stockTicker=stockticker, slug=post, status='published', publish__year=year)

    #Fetches comments (Uses related name to get them)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'companies/valuefact/detail.html', {'post': post,
                                                               'comments': comments,
                                                               'comment_form': comment_form})


def valuefact_share(request, fact_id):
    valueFact = get_object_or_404(ValueFactPost, id=fact_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(valueFact.get_absolute_url())
            subject = '{} ({}) Recommends you to check out their contribution "{}"'.format(cd['name'],
                                                                                            cd['email'],
                                                                                            valueFact.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(valueFact.title,
                                                                     post_url,
                                                                     cd['name'],
                                                                     cd['comments'])
            send_mail(subject, message, 'valueinvestingexchange@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'companies/valueFact/share.html', {'post': valueFact,
                                                              'form': form,
                                                              'sent': sent})


def contact(request):
    form_class = ContactForm
    sent = False
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            template = get_template('contact/contact_template.txt')

            subject = '{} at ({}) has sent an email from the Value Investing Exchange'.format(cd['contact_name'],
                                                                                              cd['contact_email'])

            message = 'The message sent was \n\n {}'.format(cd['content'])

            send_mail(subject, message, cd['contact_email'], ['djunh1@gmail.com'], fail_silently=False)
            sent = True
    return render(request, 'contact/contact.html', {"form": form_class, "sent": sent})
