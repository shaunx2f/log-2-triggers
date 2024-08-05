# Line 11 (0x0B): PartyList
# Regex: ^(?<type>11)\|(?<timestamp>[^|]*)\|(?<partyCount>[^|]*)\|
#
# This line represents the players currently in the party, and is sent whenever the party makeup changes.

import re
from datetime import datetime, timedelta, timezone


class FullPartyList:
    class_regex = re.compile(
        r'^(?P<type>11)\|(?P<timestamp>[^|]*)\|(?P<partyCount>[8]*)\|(?P<id1>[^|]*)\|(?P<id2>[^|]*)\|(?P<id3>[^|]*)\|(?P<id4>[^|]*)\|(?P<id5>[^|]*)\|(?P<id6>[^|]*)\|(?P<id7>[^|]*)\|(?P<id8>[^|]*)\|')
    class_friendly_name = "Party List"

    def __init__(self, log_line):
        if not FullPartyList.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for FullPartyList")

        self._log_line = log_line
        group_dict = FullPartyList.class_regex.search(log_line).groupdict()

        self._timestamp = datetime.fromisoformat(group_dict.get('timestamp')).astimezone(timezone.utc)
        self._party_count = group_dict.get('partyCount')
        self._id1 = group_dict.get('id1')
        self._id2 = group_dict.get('id2')
        self._id3 = group_dict.get('id3')
        self._id4 = group_dict.get('id4')
        self._id5 = group_dict.get('id5')
        self._id6 = group_dict.get('id6')
        self._id7 = group_dict.get('id7')
        self._id8 = group_dict.get('id8')

    @property
    def log_line(self):
        return self._log_line

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def party_count(self):
        return self._party_count

    @property
    def id1(self):
        return self._id1

    @property
    def id2(self):
        return self._id2

    @property
    def id3(self):
        return self._id3

    @property
    def id4(self):
        return self._id4

    @property
    def id5(self):
        return self._id5

    @property
    def id6(self):
        return self._id6

    @property
    def id7(self):
        return self._id7

    @property
    def id8(self):
        return self._id8

    def __str__(self):
        return ("FullPartyList["
                + str(self.timestamp) + "|"
                + str(self.party_count) + "|"
                + str(self.id1) + "|"
                + str(self.id2) + "|"
                + str(self.id3) + "|"
                + str(self.id4) + "|"
                + str(self.id5) + "|"
                + str(self.id6) + "|"
                + str(self.id7) + "|"
                + str(self.id8) +
                "]")

    def __repr__(self):
        return ("FullPartyList["
                + str(self.timestamp) + "|"
                + str(self.party_count) + "|"
                + str(self.id1) + "|"
                + str(self.id2) + "|"
                + str(self.id3) + "|"
                + str(self.id4) + "|"
                + str(self.id5) + "|"
                + str(self.id6) + "|"
                + str(self.id7) + "|"
                + str(self.id8) +
                "]")
