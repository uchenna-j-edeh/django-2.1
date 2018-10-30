from django.shortcuts import render, get_object_or_404

from . models import Page
# from django.http import HttpResponse

def index(request, pagename):
#    return HttpResponse("<h1>The Edeh Bookstore Homepage</h1>")
    pagename = '/' + pagename
    #print(pagename)
    #print(pg)
    pg = get_object_or_404(Page, permalink=pagename)

#    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all()
    }
    # assert False
#    print(context)
    return render(request, 'pages/page.html', context)
