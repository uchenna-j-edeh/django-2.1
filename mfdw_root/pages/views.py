from django.shortcuts import render

# from django.http import HttpResponse

def index(request):
#    return HttpResponse("<h1>The Edeh Bookstore Homepage</h1>")
    return render(request, 'pages/page.html')
