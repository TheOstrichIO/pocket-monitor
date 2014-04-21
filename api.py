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
    timestamp_start = messages.FloatField(2, required=True)
    timestamp_end = messages.FloatField(3, required=True)

class Stats(messages.Message):
    ""
    count = messages.IntegerField(1)
    words = messages.IntegerField(2)

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
        count, words = pm.PocketItem.getAddedStats(
                                           current_user.email(),
                                           request.timestamp_start,
                                           request.timestamp_end)
        return Stats(count=count, words=words)

app = endpoints.api_server([PocketMonApi])
