from django.shortcuts import render
from feed.feed_reader.feed import feed

# Create your views here.

def home(request):
    context ={}
    if request.method=='POST':
        rss_link = request.POST.get("rss-link")
        print(rss_link)
        feeds = feed(rss_link)
        context['feeds'] = feeds
        context['rss_link'] = rss_link

        return render(request,"feed/home.html",context)
    return render(request,"feed/home.html")