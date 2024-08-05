# Line 26 (0x1A): NetworkBuff
# Regex: ^(?<type>26)\|(?<timestamp>[^|]*)\|(?<effectId>[^|]*)\|(?<effect>[^|]*)\|(?<duration>[^|]*)\|(?<sourceId>[^|]*)\|(?<source>[^|]*)\|(?<targetId>[^|]*)\|(?<target>[^|]*)\|(?<count>[^|]*)\|(?<targetMaxHp>[^|]*)\|(?<sourceMaxHp>[^|]*)\|
#
# This message is the "gains effect" message for players and mobs gaining effects whether they are good or bad.

import re
from datetime import datetime, timedelta, timezone


class NetworkBuff:
    class_regex = re.compile(
    r'^(?P<type>26)\|(?P<timestamp>[^|]*)\|(?P<effectId>[^|]*)\|(?P<effect>[^|]*)\|(?P<duration>[^|]*)\|(?P<sourceId>[^|]*)\|(?P<source>[^|]*)\|(?P<targetId>[^|]*)\|(?P<target>[^|]*)\|(?P<count>[^|]*)\|(?P<targetMaxHp>[^|]*)\|(?P<sourceMaxHp>[^|]*)\|')
    class_friendly_name = "Buffs/Debuffs"

    def __init__(self, log_line):
        if not NetworkBuff.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for NetworkBuff")

        self._log_line = log_line
        group_dict = NetworkBuff.class_regex.search(log_line).groupdict()

        self._timestamp = datetime.fromisoformat(group_dict.get('timestamp')).astimezone(timezone.utc)
        self._effect_id = group_dict.get('effectId')
        self._effect = group_dict.get('effect')
        self._duration = group_dict.get('duration')
        self._source_id = group_dict.get('sourceId')
        self._source = group_dict.get('source')
        self._target_id = group_dict.get('targetId')
        self._target = group_dict.get('target')
        self._count = group_dict.get('count')
        self._target_max_hp = group_dict.get('targetMaxHp')
        self._source_max_hp = group_dict.get('sourceMaxHp')

    @property
    def log_line(self):
        return self._log_line

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def effect_id(self):
        return self._effect_id

    @property
    def effect(self):
        return self._effect

    @property
    def duration(self):
        return self._duration

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
    def count(self):
        return self._count

    @property
    def target_max_hp(self):
        return self._target_max_hp

    @property
    def source_max_hp(self):
        return self._source_max_hp

    def __str__(self):
        return ("NetworkBuff["
                + str(self.timestamp) + "|"
                + str(self.source_id) + "|"
                + str(self.source) + "|"
                + str(self.effect_id) + "|"
                + str(self.effect) + "|"
                + str(self.target_id) + "|"
                + str(self.target) + "|"
                + str(self.duration) + "|"
                + str(self.count) + "|"
                + str(self.target_max_hp) + "|"
                + str(self.source_max_hp)
                + "]")

    def __repr__(self):
        return ("NetworkBuff["
                + str(self.timestamp) + "|"
                + str(self.source_id) + "|"
                + str(self.source) + "|"
                + str(self.effect_id) + "|"
                + str(self.effect) + "|"
                + str(self.target_id) + "|"
                + str(self.target) + "|"
                + str(self.duration) + "|"
                + str(self.count) + "|"
                + str(self.target_max_hp) + "|"
                + str(self.source_max_hp)
                + "]")