class PartyMember:

    def __init__(self, user_id, name, job):
        self._user_id = user_id
        self._name = name
        self._job = job
        self._role = None

    def update_job(self, job):
        self._job = job
        if job in ('PLD', 'WAR', 'DRK', 'GNB'):
            self._role = 'Tank'
        elif job in ('WHM', 'AST', 'SCH', 'SGE'):
            self._role = 'Healer'
        else:
            self._role = 'DPS'

    def update_name(self, name):
        self._name = name

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def job(self):
        return self._job

    @property
    def role(self):
        return self._role

    def __str__(self):
        return ("PartyMember["
                + str(self.user_id) + "|"
                + str(self.name) + "|"
                + str(self.job) + "|"
                + str(self.role)
                + "]")

    def __repr__(self):
        return ("PartyMember["
                + str(self.user_id) + "|"
                + str(self.name) + "|"
                + str(self.job) + "|"
                + str(self.role)
                + "]")
