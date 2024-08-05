# Line 21 (0x15): NetworkAbility
# Regex: ^(?<type>2[12])\|(?<timestamp>[^|]*)\|(?<sourceId>[^|]*)\|(?<source>[^|]*)\|(?<id>[^|]*)\|(?<ability>[^|]*)\|(?<targetId>[^|]*)\|(?<target>[^|]*)\|(?<flags>[^|]*)\|(?<damage>[^|]*)\|(?:[^|]*\|){14}(?<targetCurrentHp>[^|]*)\|(?<targetMaxHp>[^|]*)\|(?<targetCurrentMp>[^|]*)\|(?<targetMaxMp>[^|]*)\|(?:[^|]*\|){2}(?<targetX>[^|]*)\|(?<targetY>[^|]*)\|(?<targetZ>[^|]*)\|(?<targetHeading>[^|]*)\|(?<currentHp>[^|]*)\|(?<maxHp>[^|]*)\|(?<currentMp>[^|]*)\|(?<maxMp>[^|]*)\|(?:[^|]*\|){2}(?<x>[^|]*)\|(?<y>[^|]*)\|(?<z>[^|]*)\|(?<heading>[^|]*)\|(?<sequence>[^|]*)\|(?<targetIndex>[^|]*)\|(?<targetCount>[^|]*)\|
#
# This is an ability that ends up hitting a single target (possibly the caster's self).
# The reason this is worded as "ends up hitting" is that some AOE abilities may only hit a single target, in which case they still result in this type

import re
from datetime import datetime, timedelta, timezone


class NetworkAbility:
    class_regex = re.compile(
        r'^(?P<type>2[12])\|(?P<timestamp>[^|]*)\|(?P<sourceId>[^|]*)\|(?P<source>[^|]*)\|(?P<id>[^|]*)\|(?P<ability>[^|]*)\|(?P<targetId>[^|]*)\|(?P<target>[^|]*)\|(?P<flags>[^|]*)\|(?P<damage>[^|]*)\|(?:[^|]*\|){14}(?P<targetCurrentHp>[^|]*)\|(?P<targetMaxHp>[^|]*)\|(?P<targetCurrentMp>[^|]*)\|(?P<targetMaxMp>[^|]*)\|(?:[^|]*\|){2}(?P<targetX>[^|]*)\|(?P<targetY>[^|]*)\|(?P<targetZ>[^|]*)\|(?P<targetHeading>[^|]*)\|(?P<currentHp>[^|]*)\|(?P<maxHp>[^|]*)\|(?P<currentMp>[^|]*)\|(?P<maxMp>[^|]*)\|(?:[^|]*\|){2}(?P<x>[^|]*)\|(?P<y>[^|]*)\|(?P<z>[^|]*)\|(?P<heading>[^|]*)\|(?P<sequence>[^|]*)\|(?P<targetIndex>[^|]*)\|(?P<targetCount>[^|]*)\|')
    class_friendly_name = "Network Ability"

    def __init__(self, log_line):
        if not NetworkAbility.class_regex.match(log_line):
            raise TypeError("Line could not be matched against Regex for NetworkAbility")

        self._log_line = log_line
        group_dict = NetworkAbility.class_regex.search(log_line).groupdict()

        self._timestamp = datetime.fromisoformat(group_dict.get('timestamp')).astimezone(timezone.utc)
        self._source_id = group_dict.get('sourceId')
        self._source = group_dict.get('source')
        self._id = group_dict.get('id')
        self._ability = group_dict.get('ability')
        self._target_id = group_dict.get('targetId')
        self._target = group_dict.get('target')
        self._flags = group_dict.get('flags')
        self._damage = group_dict.get('damage')
        self._target_current_hp = group_dict.get('targetCurrentHp')
        self._target_max_hp = group_dict.get('targetMaxHp')
        self._target_current_mp = group_dict.get('targetCurrentMp')
        self._target_max_mp = group_dict.get('targetMaxMp')
        self._target_x = group_dict.get('targetX')
        self._target_y = group_dict.get('targetY')
        self._target_z = group_dict.get('targetZ')
        self._target_heading = group_dict.get('targetHeading')
        self._current_hp = group_dict.get('currentHp')
        self._max_hp = group_dict.get('maxHp')
        self._current_mp = group_dict.get('currentMp')
        self._max_mp = group_dict.get('maxMp')
        self._x = group_dict.get('x')
        self._y = group_dict.get('y')
        self._z = group_dict.get('z')
        self._heading = group_dict.get('heading')
        self._sequence = group_dict.get('sequence')
        self._target_index = group_dict.get('targetIndex')
        self._target_count = group_dict.get('targetCount')

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
    def flags(self):
        return self._flags

    @property
    def damage(self):
        return self._damage

    @property
    def target_current_hp(self):
        return self._target_current_hp

    @property
    def target_max_hp(self):
        return self._target_max_hp

    @property
    def target_current_mp(self):
        return self._target_current_mp

    @property
    def target_max_mp(self):
        return self._target_max_mp

    @property
    def target_x(self):
        return self._target_x

    @property
    def target_y(self):
        return self._target_y

    @property
    def target_z(self):
        return self._target_z

    @property
    def target_heading(self):
        return self._target_heading

    @property
    def current_hp(self):
        return self._current_hp

    @property
    def max_hp(self):
        return self._max_hp

    @property
    def current_mp(self):
        return self._current_mp

    @property
    def max_mp(self):
        return self._max_mp

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

    @property
    def sequence(self):
        return self._sequence

    @property
    def target_index(self):
        return self._target_index

    @property
    def target_count(self):
        return self._target_count

    def __str__(self):
        return ("NetworkAbility["
                + str(self.timestamp) + "|"
                + str(self.source_id) + "|"
                + str(self.source) + "|"
                + str(self.id) + "|"
                + str(self.ability) + "|"
                + str(self.target_id) + "|"
                + str(self.target) + "|"
                + str(self.flags) + "|"
                + str(self.damage) + "|"
                + str(self.target_current_hp) + "|"
                + str(self.target_max_hp) + "|"
                + str(self.target_current_mp) + "|"
                + str(self.target_max_mp) + "|"
                + str(self.target_x) + "|"
                + str(self.target_y) + "|"
                + str(self.target_z) + "|"
                + str(self.target_heading) + "|"
                + str(self.current_hp) + "|"
                + str(self.max_hp) + "|"
                + str(self.current_mp) + "|"
                + str(self.max_mp) + "|"
                + str(self.x) + "|"
                + str(self.y) + "|"
                + str(self.z) + "|"
                + str(self.heading) + "|"
                + str(self.sequence) + "|"
                + str(self.target_index) + "|"
                + str(self.target_count)
                + "]")

    def __repr__(self):
        return ("NetworkAbility["
                + str(self.timestamp) + "|"
                + str(self.source_id) + "|"
                + str(self.source) + "|"
                + str(self.id) + "|"
                + str(self.ability) + "|"
                + str(self.target_id) + "|"
                + str(self.target) + "|"
                + str(self.flags) + "|"
                + str(self.damage) + "|"
                + str(self.target_current_hp) + "|"
                + str(self.target_max_hp) + "|"
                + str(self.target_current_mp) + "|"
                + str(self.target_max_mp) + "|"
                + str(self.target_x) + "|"
                + str(self.target_y) + "|"
                + str(self.target_z) + "|"
                + str(self.target_heading) + "|"
                + str(self.current_hp) + "|"
                + str(self.max_hp) + "|"
                + str(self.current_mp) + "|"
                + str(self.max_mp) + "|"
                + str(self.x) + "|"
                + str(self.y) + "|"
                + str(self.z) + "|"
                + str(self.heading) + "|"
                + str(self.sequence) + "|"
                + str(self.target_index) + "|"
                + str(self.target_count)
                + "]")