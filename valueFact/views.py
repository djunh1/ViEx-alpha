from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import ValueFactPost
from .forms import ValueFactForm

def post_valueFact(request):
    valueFacts = ValueFactPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'valueFact.html',{'valueFacts':valueFacts})

def valueFact_detail(request,pk):
    valuefact=get_object_or_404(ValueFactPost,pk=pk)
    return render(request, 'valueFact_detail.html', {'valuefact':valuefact})

def valueFact_new(request):
    if request.method=="POST":
        form = ValueFactForm(request.POST)
        if form.is_valid():
            valuefact=form.save(commit=False)
            valuefact.author=request.user
            valuefact.published_date=timezone.now()
            valuefact.save()

    else:
        form=ValueFactForm()

    return render(request, 'valueFact_edit.html', {'valueform':form})

def valueFact_edit(request,pk):
    valuefact=get_object_or_404(ValueFactPost,pk=pk)
    if request.method == "POST":
        form=ValueFactForm(request.POST, instance=post)
        if form.is_valid():
            valuefact=form.save(commit=False)
            valuefact.author=request.user
            valuefact.published_date=timezone.now()
            valuefact.save()
            return redirect('valuefact_detail', pk=valuefact.pk)
    else:
        form=ValueFactForm(instance=valuefact)
    return render(request, 'valueFact_edit.html', {'valueform': form})
