# Line 11 (0x0B): PartyList
# Regex: ^(?<type>11)\|(?<timestamp>[^|]*)\|(?<partyCount>[^|]*)\|
#
# This line represents the players currently in the party, and is sent whenever the party makeup changes.

import re
from datetime import datetime, timedelta, timezone


class AllianceParty:
    class_regex = re.compile(
        r'^(?P<type>11)\|(?P<timestamp>[^|]*)\|(?P<partyCount>[8]*)\|(?P<id1>[^|]*)\|(?P<id2>[^|]*)\|(?P<id3>[^|]*)\|(?P<id4>[^|]*)\|(?P<id5>[^|]*)\|(?P<id6>[^|]*)\|(?P<id7>[^|]*)\|(?P<id8>[^|]*)\|(?P<id9>[^|]*)\|(?P<id10>[^|]*)\|(?P<id11>[^|]*)\|(?P<id12>[^|]*)\|(?P<id13>[^|]*)\|(?P<id14>[^|]*)\|(?P<id15>[^|]*)\|(?P<id16>[^|]*)\|(?P<id17>[^|]*)\|(?P<id18>[^|]*)\|(?P<id19>[^|]*)\|(?P<id20>[^|]*)\|(?P<id21>[^|]*)\|(?P<id22>[^|]*)\|(?P<id23>[^|]*)\|(?P<id24>[^|]*)\|')
    class_friendly_name = "Alliance Party List"

    def __init__(self, log_line):
        if not AllianceParty.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for AllianceParty")

        self._log_line = log_line
        group_dict = AllianceParty.class_regex.search(log_line).groupdict()

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
        self._id9 = group_dict.get('id9')
        self._id10 = group_dict.get('id10')
        self._id11 = group_dict.get('id11')
        self._id12 = group_dict.get('id12')
        self._id13 = group_dict.get('id13')
        self._id14 = group_dict.get('id14')
        self._id15 = group_dict.get('id15')
        self._id16 = group_dict.get('id16')
        self._id17 = group_dict.get('id17')
        self._id18 = group_dict.get('id18')
        self._id19 = group_dict.get('id19')
        self._id20 = group_dict.get('id20')
        self._id21 = group_dict.get('id21')
        self._id22 = group_dict.get('id22')
        self._id23 = group_dict.get('id23')
        self._id24 = group_dict.get('id24')

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

    @property
    def id9(self):
        return self._id9

    @property
    def id10(self):
        return self._id10

    @property
    def id11(self):
        return self._id11

    @property
    def id12(self):
        return self._id12

    @property
    def id13(self):
        return self._id13

    @property
    def id14(self):
        return self._id14

    @property
    def id15(self):
        return self._id15

    @property
    def id16(self):
        return self._id16

    @property
    def id17(self):
        return self._id17

    @property
    def id18(self):
        return self._id18

    @property
    def id19(self):
        return self._id19

    @property
    def id20(self):
        return self._id20

    @property
    def id21(self):
        return self._id21

    @property
    def id22(self):
        return self._id22

    @property
    def id23(self):
        return self._id23

    @property
    def id24(self):
        return self._id24

    def __str__(self):
        return ("AllianceParty["
                + str(self.timestamp) + "|"
                + str(self.party_count) + "|"
                + str(self.id1) + "|"
                + str(self.id2) + "|"
                + str(self.id3) + "|"
                + str(self.id4) + "|"
                + str(self.id5) + "|"
                + str(self.id6) + "|"
                + str(self.id7) + "|"
                + str(self.id8) + "|"
                + str(self.id9) + "|"
                + str(self.id10) + "|"
                + str(self.id11) + "|"
                + str(self.id12) + "|"
                + str(self.id13) + "|"
                + str(self.id14) + "|"
                + str(self.id15) + "|"
                + str(self.id16) + "|"
                + str(self.id17) + "|"
                + str(self.id18) + "|"
                + str(self.id19) + "|"
                + str(self.id20) + "|"
                + str(self.id21) + "|"
                + str(self.id22) + "|"
                + str(self.id23) + "|"
                + str(self.id24) +
                "]")

    def __repr__(self):
        return ("AllianceParty["
                + str(self.timestamp) + "|"
                + str(self.party_count) + "|"
                + str(self.id1) + "|"
                + str(self.id2) + "|"
                + str(self.id3) + "|"
                + str(self.id4) + "|"
                + str(self.id5) + "|"
                + str(self.id6) + "|"
                + str(self.id7) + "|"
                + str(self.id8) + "|"
                + str(self.id9) + "|"
                + str(self.id10) + "|"
                + str(self.id11) + "|"
                + str(self.id12) + "|"
                + str(self.id13) + "|"
                + str(self.id14) + "|"
                + str(self.id15) + "|"
                + str(self.id16) + "|"
                + str(self.id17) + "|"
                + str(self.id18) + "|"
                + str(self.id19) + "|"
                + str(self.id20) + "|"
                + str(self.id21) + "|"
                + str(self.id22) + "|"
                + str(self.id23) + "|"
                + str(self.id24) +
                "]")

