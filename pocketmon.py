import logging
import time
from datetime import datetime as dt

from google.appengine.ext import ndb

logger = logging.getLogger('pocketmon')

class PocketItem(ndb.Model):
    "Models an individual pocket item (article)."
    pocket_id = ndb.StringProperty('pid', required=True)
    time_added = ndb.DateTimeProperty('ta')
    time_read = ndb.DateTimeProperty('tr')
    word_count = ndb.IntegerProperty('wc', required=True, default=0)
    status = ndb.StringProperty('s')
    
    @classmethod
    def queryDir(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key)
    
    @classmethod
    def queryUser(cls, dir_name):
        ancestor_key = ndb.Key('PocketDir', dir_name)
        return cls.queryDir(ancestor_key)
    
    @classmethod
    def getAttrStats(cls, attr_name, dir_name, ts, te):
        assert(attr_name in ('time_added', 'time_read'))
        if not isinstance(ts, dt):
            ts = dt.fromtimestamp(float(ts))
        if not isinstance(te, dt):
            te = dt.fromtimestamp(float(te))
        if ts > te:
            return (0, 0)
        ancestor_key = ndb.Key('PocketDir', dir_name)
        q = cls.queryDir(ancestor_key).filter(
                                  getattr(PocketItem, attr_name) >= ts,
                                  getattr(PocketItem, attr_name) <= te)
        count = 0
        words = 0
        for item in q.fetch():
            count += 1
            words += item.word_count
        return (count, words)
    
    @classmethod
    def getAddedStats(cls, dir_name, ts, te):
        return cls.getAttrStats('time_added', dir_name, ts, te)
    
    @classmethod
    def getReadStats(cls, dir_name, ts, te):
        return cls.getAttrStats('time_read', dir_name, ts, te)
    
    @classmethod
    def getStatsToTimestamp(cls, dir_name, ts):
        added_count, added_words = cls.getAddedStats(dir_name, 0, ts)
        read_count, read_words = cls.getReadStats(dir_name, 1, ts)
        return (added_count - read_count, added_words - read_words)
    
    @classmethod
    def getAllStats(cls, dir_name, ts=None, delta=86400):
        if ts is None:
            ts = time.time()
        pre_ts = ts - delta
        unread_items, unread_words = cls.getStatsToTimestamp(dir_name, ts)
        added_items, added_words = cls.getAddedStats(dir_name, pre_ts, ts)
        read_items, read_words = cls.getReadStats(dir_name, pre_ts, ts)
        return {
            'unread_items': unread_items,
            'unread_words': unread_words,
            'added_items_delta': added_items,
            'added_words_delta': added_words,
            'read_items_delta': read_items,
            'read_words_delta': read_words,
            }

def update_item_from_pocket(pid, new_item, dir_name):
    ancestor_key = ndb.Key('PocketDir', dir_name)
    item = PocketItem.queryDir(ancestor_key)    \
                .filter(PocketItem.pocket_id == pid).get()
    if item:
        # item exists in datastore - update it
        logger.debug('Updating existing item with ID %s', pid)
        if 2 == int(new_item[u'status']):
            # item was deleted
            # treat like it was read now
            item.status = u'2'
            item.time_read = dt.fromtimestamp(time.time())
            item.put()
        else:
            # something was changed
            item.status = new_item[u'status']
            item.word_count = int(new_item[u'word_count'])
            item.time_read = dt.fromtimestamp(float(new_item[u'time_read']))
            item.put()
    else:
        if 2 == int(new_item[u'status']):
            # item removed before we cached it
            logger.debug('Item ID %s was removed before we cached it', pid)
            return
        # no such item - create new one
        logger.debug('Creating new item with ID %s', pid)
        item = PocketItem(
                  parent=ancestor_key,
                  pocket_id=pid,
                  time_added=dt.fromtimestamp(float(new_item[u'time_added'])),
                  time_read=dt.fromtimestamp(float(new_item[u'time_read'])),
                  status=new_item[u'status'],
                  word_count=int(new_item[u'word_count']))
        item.put()

def update_items_from_pocket(items_dict, dir_name):
    for pid, item in items_dict.iteritems():
        update_item_from_pocket(pid, item, dir_name)
