from app.services.RSS import getNews
"""
ARABIA=["https://english.alarabiya.net/feed/rss2/en.xml","https://english.alarabiya.net/feed/rss2/en/News.xml","https://english.alarabiya.net/feed/rss2/en/business.xml","https://english.alarabiya.net/feed/rss2/en/business/energy.xml","https://english.alarabiya.net/feed/rss2/en/life-style.xml","https://english.alarabiya.net/feed/rss2/en/webtv.xml","https://english.alarabiya.net/feed/rss2/en/in-translation.xml","https://english.alarabiya.net/feed/rss2/en/views.xml","https://english.alarabiya.net/feed/rss2/en/coronavirus.xml"]

for title in ARABIA:
    getNews(title)
"""
getNews("https://english.alarabiya.net/feed/rss2/en.xml")