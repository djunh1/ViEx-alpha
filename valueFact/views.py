from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.core.mail import send_mail
from django.contrib import messages
import smtplib

from valueFact.forms import EmailPostForm, CommentForm, StockForm
from valueFact.models import ValueFactPost, Symbol, Comment
from valueFact.controller import mySQLdb_query


def home_page(request):
    form = StockForm()
    if request.method == 'GET':
        form = StockForm(request.GET)
        if form.is_valid():
            ticker = form.cleaned_data['text']
            return HttpResponseRedirect('companies:view_stock' % ticker)
    return render(request, 'main_page/home.html', {"form": form})


def search_home(request):
    form = StockForm()
    return render(request, 'search/search_home.html', {'form': form})


def view_stock(request, symbol):
    form = StockForm()
    # Not dry

    if request.method == 'POST':
        form = StockForm(data=request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['text']
            try:
                stocksymbol = Symbol.objects.filter(ticker=ticker)[0]
            except IndexError:
                messages.error(request, 'We could not find %s in our database!  Please try again' % ticker)
                render(request, 'search/stock_data.html', {"form": form})

            else:
                stockQueryDb = mySQLdb_query(ticker)
                #Returns EPS data
                epsData = stockQueryDb.get_statement_data(stockQueryDb.eps)
                fcfData = stockQueryDb.get_free_cash_flow()
                stockQueryDb.get_netnet_value()
                ncavData = stockQueryDb.get_NCAV()[1]
                netnetData =stockQueryDb.get_netnet_value()[1]
                return render(request, 'search/stock_data.html', {'eps': epsData, 'fcf': fcfData,
                                                         'ncav': ncavData, 'netnet':netnetData,
                                                         "form": form, 'stock': stocksymbol})
    else:
        ticker = symbol
        stockQueryDb = mySQLdb_query(ticker)
        try:
            stocksymbol = Symbol.objects.filter(ticker=ticker)[0]
        except IndexError:
            messages.error(request, 'We could not find %s in our database!  Please try again' % ticker)
            render(request, 'search/stock_data.html', {"form": form})
        else:
            #Returns EPS data
            epsData=stockQueryDb.get_statement_data(stockQueryDb.eps)
            fcfData=stockQueryDb.get_free_cash_flow()
            stockQueryDb.get_netnet_value()
            ncavData=stockQueryDb.get_NCAV()[1]
            netnetData=stockQueryDb.get_netnet_value()[1]
            return render(request, 'search/stock_data.html', {'eps': epsData, 'fcf': fcfData,
                                                         'ncav': ncavData, 'netnet': netnetData,
                                                         "form": form, 'stock': stocksymbol})
    return render(request, 'search/stock_data.html', {"form": form})


def stock_data_search_display(request, symbol):
    form = StockForm()

    if request.method == 'POST':
        form = StockForm(data=request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['text']
            stockQueryDb = mySQLdb_query(ticker)
            if stockQueryDb.get_statement_data(stockQueryDb.eps)==():
                return render(request, 'search/search_results.html', {'form': StockForm()})
            else:
                #Returns EPS data
                epsData=stockQueryDb.get_statement_data(stockQueryDb.eps)
                fcfData=stockQueryDb.get_free_cash_flow()
                stockQueryDb.get_netnet_value()
                ncavData=stockQueryDb.get_NCAV()[1]
                netnetData=stockQueryDb.get_netnet_value()[1]
                return render(request, 'search/stock_data.html', {'eps': epsData, 'fcf': fcfData,
                                                         'ncav': ncavData, 'netnet':netnetData,
                                                         "form": form , "ticker": ticker,
                                                                  'symbol': symbol})
    return render(request, 'search/search_results.html', {"form": form})


def valuefact_detail(request, year, post):
    post = get_object_or_404(ValueFactPost, slug=post, status='published', publish__year=year)

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

