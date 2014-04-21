"""Pocket-monitor API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.

Author: ItamarO, 04/2014
"""

import endpoints
from protorpc import messages
from protorpc import remote

import pocketmon as pm

package = 'PocketMon'

class StatsRequest(messages.Message):
    ""
    username = messages.StringField(1, required=True)
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
        count, words = pm.PocketItem.getAddedStats(request.username,
                                                   request.timestamp_start,
                                                   request.timestamp_end)
        return Stats(count=count, words=words)

app = endpoints.api_server([PocketMonApi])
