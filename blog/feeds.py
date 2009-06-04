from django.contrib.syndication.feeds import Feed
from django.contrib.comments.feeds import LatestCommentFeed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed

from blog.models import Entry

class LatestEntries(Feed):

	title = "Stefan Jenkner (Artikel)"
	author_name = "Stefan Jenkner"
	author_email = "stefan@jenkner.org"
	description = "Neues im Blog von Stefan Jenkner"
	description_template = 'feeds/description.html'
	link = '/'

	def items(self):
		return Entry.objects.filter(is_public=True).order_by('-date')[:5]

	def item_pubdate(self, obj):
		return obj.date

class LatestComments(LatestCommentFeed):

	title = "Stefan Jenkner (Kommentare)" 
	author_name = LatestEntries.author_name
	author_email = LatestEntries.author_email
	description = "Kommentare im Blog von Stefan Jenkner"
	link = LatestEntries.link

class Rss2Feed(Rss201rev2Feed):

	def rss_attributes(self):
		attrs = super(Rss2Feed, self).rss_attributes()
		attrs['xmlns:atom'] = 'http://www.w3.org/2005/Atom'
		return attrs

	def add_root_elements(self, handler):
		super(Rss2Feed, self).add_root_elements(handler)
		handler.addQuickElement('atom:link', None, {u"rel": u"self", u"href": self.feed['feed_url']} )

class LatestEntriesRss(LatestEntries):
	feed_type = Rss2Feed

class LatestEntriesAtom(LatestEntries):
	feed_type = Atom1Feed
	subtitle = LatestEntries.description

class LatestCommentsRss(LatestComments):
	feed_type = Rss2Feed

class LatestCommentsAtom(LatestComments):
	feed_type = Atom1Feed
	subtitle = LatestComments.description
