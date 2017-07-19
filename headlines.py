import feedparser

from flask import Flask, render_template, request
app = Flask(__name__)

RSS_FEED = {'zee': 'http://zeenews.india.com/rss/technology-news.xml',
			'news18': 'http://www.news18.com/rss/india.xml',
			'toi': 'http://timesofindia.indiatimes.com/rssfeeds/4719161.cms',
			}

@app.route('/')
def get_news():
	query = request.args.get("publication")
	if not query or query.lower() not in RSS_FEED: 
		publication = "zee"
	else:
		publication = query.lower()
	feed = feedparser.parse(RSS_FEED[publication])
	return render_template("home.html", articles=feed['entries'])

if __name__=='__main__':
	app.run(debug=True)