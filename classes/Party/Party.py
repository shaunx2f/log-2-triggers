from classes.Party import PartyMember


class Party:

    def __init__(self):
        self._party = dict()

    def update_party(self, party_list):
        for entry in party_list:
            self._party[entry.user_id] = entry

    def clear_party(self):
        self._party.clear()

    def get_party(self):
        return self._party

    def add_to_party(self, party_member: PartyMember):
        self._party[party_member.user_id] = party_member

    def in_party(self, user_id):
        if self._party.get(user_id):
            return True
        else:
            return False

    def get_party_member(self, user_id):
        return self._party.get(user_id)

    def update_party_member(self, user_id, name, job):
        if not self._party.get(user_id):
            raise Exception("Party Member does not exist")
        party_member = self._party.get(user_id)
        if name:
            party_member.update_name(name)
        if job:
            party_member.update_job(job)

        #print("Updated Party Member Details")
        #print(party_member)


    def __str__(self):
        party_member_tanks = []
        party_member_healers = []
        party_member_dps = []
        for party_member in self._party.values():
            if party_member.role == 'Tank':
                party_member_tanks.append("Tank: " + party_member.name)

            if party_member.role == 'Healer':
                party_member_healers.append("Healer: " + party_member.name)

            if party_member.role == 'DPS':
                party_member_dps.append("DPS: " + party_member.name)

        return ', '.join(map(str, party_member_tanks + party_member_healers + party_member_dps))

    def __repr__(self):
        party_member_tanks = []
        party_member_healers = []
        party_member_dps = []
        for party_member in self._party.values():
            if party_member.role == 'Tank':
                party_member_tanks.append("Tank: " + party_member.name)

            if party_member.role == 'Healer':
                party_member_healers.append("Healer: " + party_member.name)

            if party_member.role == 'DPS':
                party_member_dps.append("DPS: " + party_member.name)

        return ', '.join(map(str, party_member_tanks + party_member_healers + party_member_dps))
