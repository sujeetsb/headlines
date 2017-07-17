import feedparser

from flask import Flask 
app = Flask(__name__)

RSS_FEED = {'zee': 'http://zeenews.india.com/rss/technology-news.xml',
			'news18': 'http://www.news18.com/rss/india.xml',
			'toi': 'http://timesofindia.indiatimes.com/rssfeeds/4719161.cms',
			}

@app.route('/')
@app.route("/<publication>")
def get_news(publication="zee"):
	feed = feedparser.parse(RSS_FEED[publication])
	first_article = feed['entries'][0]
	return """<html>
		<body>
			<h1> Headlines </h1>
			<b>{0}</b> <br/>
			<i>{1}</i> <br/>
			<p>{2}</p> </br>
		</body>
	</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))


if __name__=='__main__':
	app.run(debug=True)