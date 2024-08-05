# Line 27 (0x1B): NetworkTargetIcon (Head Marker)
# Regex: ^(?<type>27)\|(?<timestamp>[^|]*)\|(?<targetId>[^|]*)\|(?<target>[^|]*)\|(?:[^|]*\|){2}(?<id>[^|]*)\|
#
# The different headmarker IDs (e.g. 0018 or 001A in the examples above) are consistent across fights as far as which marker they visually represent.
# Note: It's unclear when the head markers disappear. Maybe one of these fields is a duration time? It's not clear what either of these unknown values mean.

import re
from datetime import datetime, timedelta, timezone


class NetworkTargetIcon:
    class_regex = re.compile(
        r'^(?P<type>27)\|(?P<timestamp>[^|]*)\|(?P<targetId>[^|]*)\|(?P<target>[^|]*)\|(?:[^|]*\|){2}(?P<id>[^|]*)\|')
    class_friendly_name = "Headmarkers"

    def __init__(self, log_line):
        if not NetworkTargetIcon.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for NetworkTargetIcon")

        self._log_line = log_line
        group_dict = NetworkTargetIcon.class_regex.search(log_line).groupdict()

        self._timestamp = datetime.fromisoformat(group_dict.get('timestamp')).astimezone(timezone.utc)
        self._id = group_dict.get('id')
        self._target_id = group_dict.get('targetId')
        self._target = group_dict.get('target')

    @property
    def log_line(self):
        return self._log_line

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def id(self):
        return self._id

    @property
    def target_id(self):
        return self._target_id

    @property
    def target(self):
        return self._target

    def __str__(self):
        return ("NetworkTargetIcon["
                + str(self.timestamp) + "|"
                + str(self.id) + "|"
                + str(self.target_id) + "|"
                + str(self.target)
                + "]")

    def __repr__(self):
        return ("NetworkTargetIcon["
                + str(self.timestamp) + "|"
                + str(self.id) + "|"
                + str(self.target_id) + "|"
                + str(self.target)
                + "]")