# Line 01 (0x01): ChangeZone
# Regex: ^(?<type>01)\|(?<timestamp>[^|]*)\|(?<id>[^|]*)\|(?<name>[^|]*)\|
#
# This message is sent when first logging in and whenever the zone is changed.

import re
from datetime import datetime, timedelta, timezone


class ZoneChange:
    class_regex = re.compile(
        r'^(?P<type>01)\|(?P<timestamp>[^|]*)\|(?P<id>[^|]*)\|(?P<name>[^|]*)\|')
    class_friendly_name = "ZoneChange"

    def __init__(self, log_line):
        if not ZoneChange.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for ZoneChange")

        self._log_line = log_line
        group_dict = ZoneChange.class_regex.search(log_line).groupdict()
        self._timestamp = datetime.fromisoformat(group_dict.get('timestamp')).astimezone(timezone.utc)
        self._id = group_dict.get('id')
        self._name = group_dict.get('name')

    @property
    def log_line(self):
        return self._log_line

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    def __str__(self):
        return ("ZoneChange["
                + str(self.timestamp) + "|"
                + str(self.name) + "|"
                + str(self.id) + "|"
                + "]")

    def __repr__(self):
        return ("ZoneChange["
                + str(self.timestamp) + "|"
                + str(self.name) + "|"
                + str(self.id) + "|"
                + "]")
