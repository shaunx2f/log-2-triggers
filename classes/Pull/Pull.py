from classes.Party.Party import Party


class Pull:

    def __init__(self):
        self._headmarker_offset = None
        self._start_time = None
        self._end_time = None
        self._party_members = Party()
        self._boss_name = None
        self._boss_id = None
        self._zone_name = None

        self._events = []
        self._casts = []
        self._abilities = []
        self._tethers = []
        self._headmarkers = []
        self._debuffs = []
        self._damage = []
        self._deaths = []

    def set_boss_name(self, boss_name):
        self._boss_name = boss_name

    def set_zone_name(self, zone_name):
        self._zone_name = zone_name

    def set_boss_id(self, boss_id):
        self._boss_id = boss_id

    def set_headmarker_offset(self, headmarker_offset):
        self._headmarker_offset = headmarker_offset

    def set_start_time(self, start_time):
        self._start_time = start_time

    def set_end_time(self, end_time):
        self._end_time = end_time

    def set_party_members(self, party_members):
        self._party_members = party_members

    def add_event(self, time, event):
        self._events.append((time, event))

    def add_cast(self, time, cast):
        self._casts.append((time, cast))

    def add_ability(self, time, ability):
        self._abilities.append((time, ability))

    def add_tethers(self, time, tether):
        self._tethers.append((time, tether))

    def add_headmarker(self, time, headmarker):
        self._headmarkers.append((time, headmarker))

    def add_debuff(self, time, debuff):
        self._debuffs.append((time, debuff))

    def add_damage(self, time, damage_event):
        self._damage.append((time, damage_event))

    def add_deaths(self, time, death):
        self._deaths.append((time, death))

    def boss_name(self):
        return self._boss_name

    def zone_name(self):
        return self._zone_name

    def boss_id(self):
        return self._boss_id

    def headmarker_offset(self):
        return self._headmarker_offset

    def start_time(self):
        return self._start_time

    def end_time(self):
        return self._end_time

    def party_members(self):
        return self._party_members

    def events(self):
        return self._events

    def casts(self):
        return self._casts

    def abilities(self):
        return self._abilities

    def headmarkers(self):
        return self._headmarkers

    def tethers(self):
        return self._tethers

    def debuffs(self):
        return self._debuffs

    def damage(self):
        return self._damage

    def deaths(self):
        return self._deaths

    def __repr__(self):
        return "Pull[Zone: " + self.zone_name() + " Party" + str(self.party_members()) + " Start Time: " + str(
            self.start_time()) + " End Time: " + str(self.end_time()) + "]"
