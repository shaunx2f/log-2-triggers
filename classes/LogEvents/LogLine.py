# Line 00 (0x00): LogLine
# Regex: ^(?<type>00)\|(?<timestamp>[^|]*)\|(?<code>[^|]*)\|(?<name>[^|]*)\|(?<line>[^|]*)\|
#
# These are what this document calls "game log lines".
# Because these are not often used for triggers (other than 0839 and 0044 messages), the full set of LogTypes is not well-documented.

import re
from datetime import datetime, timedelta, timezone


class LogLine:
    class_regex = re.compile(
        r'^(?P<type>00)\|(?P<timestamp>[^|]*)\|(?P<code>[^|]*)\|(?P<name>[^|]*)\|(?P<line>[^|]*)\|')
    class_friendly_name = "Chat Log Lines"

    def __init__(self, log_line):
        if not LogLine.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for LogLine")

        self._log_line = log_line
        group_dict = LogLine.class_regex.search(log_line).groupdict()
        self._timestamp = datetime.fromisoformat(group_dict.get('timestamp')).astimezone(timezone.utc)
        self._code = group_dict.get('code')
        self._name = group_dict.get('name')
        self._line = group_dict.get('line')

    @property
    def log_line(self):
        return self._log_line

    @property
    def line(self):
        return self._line

    @property
    def code(self):
        return self._code

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def name(self):
        return self._name

    @property
    def log_line(self):
        return self._log_line

    def __str__(self):
        return ("LogLine["
                + str(self.timestamp) + "|"
                + str(self.name) + "|"
                + str(self.code) + "|"
                + str(self.line)
                + "]")

    def __repr__(self):
        return ("LogLine["
                + str(self.timestamp) + "|"
                + str(self.name) + "|"
                + str(self.code) + "|"
                + str(self.line)
                + "]")