import feedparser

feed_links = {
    "https://openai.com/news/rss.xml": "OpenAI",
    "https://huggingface.co/blog/feed.xml": "Hugging Face",
    "https://developer.nvidia.com/blog/feed": "NVIDIA",
    "https://github.blog/feed/": "GitHub Blog",
    "https://feeds.feedburner.com/TheHackersNews": "The Hacker News",
    "https://aws.amazon.com/blogs/aws/feed/": "AWS",
    "https://cloud.google.com/blog/products/rss/": "Google Cloud",
    "https://kubernetes.io/feed.xml": "Kubernetes",
    "https://stackoverflow.blog/feed/": "Stack Overflow Blog",
    "https://martinfowler.com/feed.atom": "Martin Fowler"
}

def fetch_news():
    articles = []
        #   (x,y)
    for feed_url, source in feed_links.items():
        feed = feedparser.parse(feed_url)
        # print(feed)

        for entry in feed.entries[:5]:
            article = {
                "title": entry.get("title", "nahi mila Title"),
                "source": source,
                "description": entry.get("summary", "nahi mila Description"),
                "published_date": entry.get("published", "nahi mili date"),
                "link": entry.get("link", ""),
                "summary": None
            }
            # print(article)
            # print(article["title"])
            # print("\n")

            articles.append(article)
    return articles

# fetch_news()