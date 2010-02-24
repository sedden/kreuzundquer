from django.contrib.syndication.feeds import Feed
from django.contrib.comments.feeds import LatestCommentFeed
from django.utils.feedgenerator import Atom1Feed

from blog.models import Entry

class LatestEntries(Feed):

	title = "kreuzundquer Blog"
	author_name = "kreuzundquer"
	author_email = "stefan@jenkner.org"
	description = "Neues im kreuzundquer Blog"
	description_template = 'feeds/description.html'
	link = '/'

	def items(self):
		return Entry.objects.filter(is_public=True).order_by('-date')[:5]

	def item_pubdate(self, obj):
		return obj.date

class LatestComments(LatestCommentFeed):

	title = "kreuzundquer Kommentare" 
	author_name = LatestEntries.author_name
	author_email = LatestEntries.author_email
	description = "Kommentare im kreuzundquer Blog"
	description_template = 'feeds/description_markdown.html'
	link = LatestEntries.link

class LatestEntriesAtom(LatestEntries):
	feed_type = Atom1Feed
	subtitle = LatestEntries.description

class LatestCommentsAtom(LatestComments):
	feed_type = Atom1Feed
	subtitle = LatestComments.description
