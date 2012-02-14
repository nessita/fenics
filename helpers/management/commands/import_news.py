# -*- coding: utf-8 -*-
import datetime

import feedparser

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from news.models import News


FEED_URL = getattr(settings, 'FENICS_FEED_URL',
                   'http://www.canchallena.com/herramientas/rss')


class Command(BaseCommand):
    help = 'Import news from feed'

    def handle(self, *args, **options):
        feed = feedparser.parse(FEED_URL)
        counter = 0

        for entry in feed['entries']:
            tags = [t['term'] for t in entry.get('tags', [])]

            if u'Primera División' in tags:

                news_date = datetime.datetime(year=entry.updated_parsed.tm_year,
                                              month=entry.updated_parsed.tm_mon,
                                              day=entry.updated_parsed.tm_mday,
                                              hour=entry.updated_parsed.tm_hour,
                                              minute=entry.updated_parsed.tm_min)
                news_date = news_date - datetime.timedelta(hours=3)

                if not News.objects.filter(title=entry['title'],
                                           published=news_date):
                    news = News.objects.create(title=entry['title'],
                                               published=news_date,
                                               summary=entry['summary'],
                                               link=entry['link'])
                    counter += 1

        self.stdout.write('Successfully imported %d news\n' % counter)
