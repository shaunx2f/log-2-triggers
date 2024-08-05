# Line 35 (0x23): NetworkTether
# Regex: ^(?<type>35)\|(?<timestamp>[^|]*)\|(?<sourceId>[^|]*)\|(?<source>[^|]*)\|(?<targetId>[^|]*)\|(?<target>[^|]*)\|(?:[^|]*\|){2}(?<id>[^|]*)\|
#
# This log line is for tethers between enemies or enemies and players. This does not appear to be used for player to player skill tethers like dragonsight or cover.
# (It can be used for enemy-inflicted player to player tethers such as burning chains in Shinryu N/EX.)

import re
from datetime import datetime, timedelta, timezone


class NetworkTether:
    class_regex = re.compile(
        r'^(?P<type>35)\|(?P<timestamp>[^|]*)\|(?P<sourceId>[^|]*)\|(?P<source>[^|]*)\|(?P<targetId>[^|]*)\|(?P<target>[^|]*)\|(?:[^|]*\|){2}(?P<id>[^|]*)\|')
    class_friendly_name = "Tethers"

    def __init__(self, log_line):
        if not NetworkTether.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for NetworkTether")

        self._log_line = log_line
        group_dict = NetworkTether.class_regex.search(log_line).groupdict()

        self._timestamp = datetime.fromisoformat(group_dict.get('timestamp')).astimezone(timezone.utc)
        self._source_id = group_dict.get('sourceId')
        self._source = group_dict.get('source')
        self._target_id = group_dict.get('targetId')
        self._target = group_dict.get('target')
        self._id = group_dict.get('id')

    @property
    def log_line(self):
        return self._log_line

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def source_id(self):
        return self._source_id

    @property
    def source(self):
        return self._source

    @property
    def target_id(self):
        return self._target_id

    @property
    def target(self):
        return self._target

    @property
    def id(self):
        return self._id

    def __str__(self):
        return ("NetworkTether["
                + str(self.timestamp) + "|"
                + str(self.source_id) + "|"
                + str(self.source) + "|"
                + str(self.target_id) + "|"
                + str(self.target) + "|"
                + str(self.id)
                + "]")

    def __repr__(self):
        return ("NetworkTether["
                + str(self.timestamp) + "|"
                + str(self.source_id) + "|"
                + str(self.source) + "|"
                + str(self.target_id) + "|"
                + str(self.target) + "|"
                + str(self.id)
                + "]")