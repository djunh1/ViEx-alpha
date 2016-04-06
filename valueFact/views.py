from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
import smtplib

from valueFact.forms import EmailPostForm, CommentForm
from valueFact.models import ValueFactPost, Symbol, Comment


class valueFactListView(ListView):
    queryset = ValueFactPost.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'companies/valueFact/list.html'


def valuefact_detail(request, year, post):
    post = get_object_or_404(ValueFactPost, slug=post, status='published',publish__year=year)

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





def view_stock(request,slug):
    stock = get_object_or_404(Symbol, slug=slug)
    return render_to_response('companies/valueFact/stockData.html',{
        'name' :name,
        'ticker':ticker
    })


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

