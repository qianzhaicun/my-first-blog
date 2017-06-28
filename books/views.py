from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from books.models import book
from books.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext

def search(request):
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(title__icontains=query)|Q(authors__first_name__icontains=query)|Q(authors__last_name__icontains=query)
            )
        results = book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html",{"results":results,"query":query})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            send_mail('Feedback from your site,topic:%s ' % topic,message,sender,('kaixinbuliao@qq.com',))
            return HttpResponseRedirect("/thanks")
    else:
        form = ContactForm(initial={'sender': 'qianzhaicun@163.com'})
    return render_to_response('books/contact.html', {'form': form})

def thanks(request):
    return render_to_response("books/thank.html",{})
