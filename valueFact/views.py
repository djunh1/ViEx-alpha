from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


from valueFact.forms import EmailPostForm
from valueFact.models import ValueFactPost, Symbol


class valueFactListView(ListView):
    queryset = ValueFactPost.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'companies/valueFact/list.html'


def valuefact_detail(request, year, post):
    post = get_object_or_404(ValueFactPost, slug=post, status='published',publish__year=year)
    return render(request, 'companies/valuefact/detail.html', {'post': post})





def view_stock(request,slug):
    stock = get_object_or_404(Symbol, slug=slug)
    return render_to_response('companies/valueFact/stockData.html',{
        'name' :name,
        'ticker':ticker
    })


def valueFact_share(request,valueFact_id):
    valueFact = get_object_or_404(ValueFactPost, id=valueFact_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_Data

    else:
        form = EmailPostForm()

    return render(request, 'companies/valueFact/share.html', {'valueFact': valueFact, 'form': form, 'sent': sent} )

