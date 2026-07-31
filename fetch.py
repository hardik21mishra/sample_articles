import feedparser

feed_links = {
    # ===== Tier 1 - Must Have =====
    "https://www.infoq.com/feed/": "InfoQ",
    "https://martinfowler.com/feed.atom": "Martin Fowler",
    "https://queue.acm.org/rss/": "ACM Queue",
    "https://lwn.net/headlines/rss": "LWN.net",
    "https://netflixtechblog.com/feed": "Netflix TechBlog",
    "https://blog.cloudflare.com/rss/": "Cloudflare Blog",
    "https://code.fb.com/feed/": "Meta Engineering",
    "https://github.blog/feed/": "GitHub Blog",
    "https://aws.amazon.com/blogs/aws/feed/": "AWS",
    "https://cloud.google.com/blog/products/rss/": "Google Cloud",

    # ===== Tier 2 - Infrastructure =====
    "https://www.cncf.io/feed/": "CNCF",
    "https://kubernetes.io/feed.xml": "Kubernetes",
    "https://istio.io/latest/feed.xml": "Istio",
    "https://www.hashicorp.com/blog/feed.xml": "HashiCorp",
    "https://grafana.com/blog/rss/": "Grafana Labs",
    "https://prometheus.io/feed.xml": "Prometheus",
    "https://www.elastic.co/blog/feed": "Elastic",
    "https://helm.sh/feed.xml": "Helm",
    "https://developer.nvidia.com/blog/feed": "NVIDIA",
    "https://thenewstack.io/feed/": "The New Stack",

    # ===== Tier 3 - AI / ML =====
    "https://openai.com/news/rss.xml": "OpenAI",
    "https://huggingface.co/blog/feed.xml": "Hugging Face",
    "https://research.google/blog/rss/": "Google Research",
    "https://blogs.microsoft.com/ai/feed/": "Microsoft AI",
    "https://www.anthropic.com/news/rss.xml": "Anthropic",
    "https://pytorch.org/feed.xml": "PyTorch",
    "https://www.tensorflow.org/feed.xml": "TensorFlow",
    "https://engineering.fb.com/category/ai/feed/": "Meta AI Engineering",

    # ===== Tier 4 - Databases =====
    "https://www.cockroachlabs.com/blog/rss.xml": "CockroachDB",
    "https://www.timescale.com/blog/rss/": "TimescaleDB",
    "https://planet.postgresql.org/rss20.xml": "Planet PostgreSQL",
    "https://redis.com/feed/": "Redis",
    "https://www.mongodb.com/blog/rss": "MongoDB",

    # ===== Tier 5 - Security =====
    "https://googleprojectzero.blogspot.com/feeds/posts/default": "Google Project Zero",
    "https://feeds.feedburner.com/TheHackersNews": "The Hacker News",
    "https://unit42.paloaltonetworks.com/feed/": "Palo Alto Unit 42",
    "https://blog.talosintelligence.com/feeds/posts/default": "Cisco Talos",
    "https://www.schneier.com/feed/atom/": "Schneier on Security",

    # ===== Tier 6 - Programming =====
    "https://go.dev/blog/feed.atom": "Go Blog",
    "https://blog.rust-lang.org/feed.xml": "Rust Blog",
    "https://v8.dev/blog.atom": "V8 JavaScript Engine",
    "https://developer.chrome.com/feed.xml": "Chrome Developers",
    "https://webkit.org/feed/": "WebKit",
    "https://blog.jetbrains.com/feed/": "JetBrains Blog",
    "https://planet.kernel.org/rss20.xml": "Planet Kernel",
    "https://planet.python.org/rss20.xml": "Planet Python",

    # ===== Tier 7 - Engineering Blogs =====
    "https://engineering.linkedin.com/blog.rss.html": "LinkedIn Engineering",
    "https://dropbox.tech/feed": "Dropbox Tech",
    "https://stripe.com/blog/feed.rss": "Stripe Engineering",
    "https://engineering.atspotify.com/feed/": "Spotify Engineering",
    "https://www.datadoghq.com/blog/rss/": "Datadog Engineering",
    "https://engineering.salesforce.com/feed/": "Salesforce Engineering",
    "https://www.twilio.com/en-us/blog/rss.xml": "Twilio Engineering",

    # ===== Tier 8 - General Technical News =====
    "https://feeds.arstechnica.com/arstechnica/index": "Ars Technica",
    "https://rss.slashdot.org/Slashdot/slashdotMain": "Slashdot",
}

# Lower priority / redundant / less technical

# "https://www.theverge.com/rss/index.xml": "The Verge",
# "https://techcrunch.com/feed/": "TechCrunch",
# "https://www.zdnet.com/news/rss.xml": "ZDNet",
# "https://feeds.feedburner.com/oreilly/radar": "O'Reilly Radar",   # mostly inactive
# "https://stackoverflow.blog/feed/": "Stack Overflow Blog",
# "https://highscalability.com/rss/": "High Scalability",           # infrequent
# "https://www.infoq.com/architecture-design/feed/": "InfoQ Architecture",  # overlaps InfoQ
# "https://www.cockroachlabs.com/blog/tags/distributed-systems/rss.xml": "Distributed Systems (CockroachDB)",
# "https://blog.cloudflare.com/tag/workers/rss/": "Cloudflare Workers",      # overlaps Cloudflare
# "https://containerjournal.com/feed/": "Container Journal",
# "https://discord.com/blog/rss.xml": "Discord Engineering",
# "https://blog.bytebytego.com/feed": "ByteByteGo",
# "https://blog.jetbrains.com/kotlin/feed/": "JetBrains Kotlin",
# "https://kotlinlang.org/feed.xml": "Kotlin",
# "https://blog.scala-lang.org/feed.xml": "Scala",
# "https://planet.mozilla.org/rss20.xml": "Planet Mozilla",
# "https://www.phoronix.com/rss.php": "Phoronix",
# "https://cacm.acm.org/feed/": "Communications of the ACM",

def fetch_news():
    articles = []
        #   (x,y)
    for feed_url, source in feed_links.items():
        feed = feedparser.parse(feed_url)
        # print(feed)

        for entry in feed.entries[:1]:
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