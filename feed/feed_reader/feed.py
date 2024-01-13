import feedparser


feeds_data = []

def feed(url):
    print(f"\n\nShowing Data for url -> {url}\n.............................\n")
    feed = feedparser.parse(url) # https://feeds.bbci.co.uk/news/rss.xml
    if feed['bozo']:
        print("failed to fetch results")
    for entry in feed['entries']:
        description = entry.description[:100]
        single_feed= {'title':entry.title,'description':description,'link':entry.link}
        feeds_data.append(single_feed)

    if not feeds_data:
        return {'error':"Internal server error occured"}
    return feeds_data

