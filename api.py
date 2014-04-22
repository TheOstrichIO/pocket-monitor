"""Pocket-monitor API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.

Author: ItamarO, 04/2014
"""

import endpoints
from protorpc import messages
from protorpc import remote

import pocketmon as pm
from google.appengine.api import users

package = 'PocketMon'

class StatsRequest(messages.Message):
    ""
    timestamp = messages.FloatField(1)

class Stats(messages.Message):
    ""
    unread_items = messages.IntegerField(1)
    unread_words = messages.IntegerField(2)
    added_items_delta = messages.IntegerField(3)
    added_words_delta = messages.IntegerField(4)
    read_items_delta = messages.IntegerField(5)
    read_words_delta = messages.IntegerField(6)

@endpoints.api(name='pocketmon', version='v1')
class PocketMonApi(remote.Service):
    """Pocket-monitor API v1."""

    @endpoints.method(StatsRequest, Stats,
                      path='stats', http_method='GET',
                      name='stats.get')
    def get_stats(self, request):
        current_user = users.get_current_user()
        if current_user is None:
            raise endpoints.ForbiddenException()
        stats = pm.PocketItem.getAllStats(current_user.email(),
                                          request.timestamp)
        return Stats(**stats)

app = endpoints.api_server([PocketMonApi])
