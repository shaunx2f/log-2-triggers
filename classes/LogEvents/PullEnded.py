import re
from datetime import datetime, timedelta, timezone


class PullEnded:
    class_regex = re.compile(r'^33\|(?P<timestamp>[^|]*)\|[A-F0-9]{8}\|4000000[3F]\|')
    class_friendly_name = "Pull Ended"

    def __init__(self, log_line):
        if not PullEnded.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for PullEnded")

        group_dict = PullEnded.class_regex.search(log_line).groupdict()

        self._timestamp = datetime.fromisoformat(group_dict.get('timestamp')).astimezone(timezone.utc)

    @property
    def timestamp(self):
        return self._timestamp
