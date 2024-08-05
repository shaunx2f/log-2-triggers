# Line 20 (0x14): NetworkStartsCasting
# Regex: ^(?<type>00)\|(?<timestamp>[^|]*)\|(?<code>[^|]*)\|(?<name>[^|]*)\|(?<line>[^|]*)\|
#
# These are what this document calls "game log lines".
# Because these are not often used for triggers (other than 0839 and 0044 messages), the full set of LogTypes is not well-documented.

import re
from datetime import datetime, timedelta, timezone


class NetworkStartsCasting:
    class_regex = re.compile(
        r'^(?P<type>20)\|(?P<timestamp>[^|]*)\|(?P<sourceId>[^|]*)\|(?P<source>[^|]*)\|(?P<id>[^|]*)\|(?P<ability>[^|]*)\|(?P<targetId>[^|]*)\|(?P<target>[^|]*)\|(?P<castTime>[^|]*)\|(?P<x>[^|]*)\|(?P<y>[^|]*)\|(?P<z>[^|]*)\|(?P<heading>[^|]*)\|')
    class_friendly_name = "Casts (Unique Mechanics)"

    def __init__(self, log_line):
        if not NetworkStartsCasting.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for NetworkStartsCasting")

        self._log_line = log_line
        group_dict = NetworkStartsCasting.class_regex.search(log_line).groupdict()

        self._timestamp = datetime.fromisoformat(group_dict.get('timestamp')).astimezone(timezone.utc)
        self._source_id = group_dict.get('sourceId')
        self._source = group_dict.get('source')
        self._id = group_dict.get('id')
        self._ability = group_dict.get('ability')
        self._target_id = group_dict.get('targetId')
        self._target = group_dict.get('target')
        self._cast_time = group_dict.get('castTime')
        self._x = group_dict.get('x')
        self._y = group_dict.get('y')
        self._z = group_dict.get('z')
        self._heading = group_dict.get('heading')

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
    def id(self):
        return self._id

    @property
    def ability(self):
        return self._ability

    @property
    def target_id(self):
        return self._target_id

    @property
    def target(self):
        return self._target

    @property
    def cast_time(self):
        return self._cast_time

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def heading(self):
        return self._heading

    def __str__(self):
        return ("NetworkStartsCasting["
                + str(self.timestamp) + "|"
                + str(self.source_id) + "|"
                + str(self.source) + "|"
                + str(self.id) + "|"
                + str(self.ability) + "|"
                + str(self.target_id) + "|"
                + str(self.target) + "|"
                + str(self.cast_time) + "|"
                + str(self.x) + "|"
                + str(self.y) + "|"
                + str(self.z) + "|"
                + str(self.heading)
                + "]")

    def __repr__(self):
        return ("NetworkStartsCasting["
                + str(self.timestamp) + "|"
                + str(self.source_id) + "|"
                + str(self.source) + "|"
                + str(self.id) + "|"
                + str(self.ability) + "|"
                + str(self.target_id) + "|"
                + str(self.target) + "|"
                + str(self.cast_time) + "|"
                + str(self.x) + "|"
                + str(self.y) + "|"
                + str(self.z) + "|"
                + str(self.heading)
                + "]")