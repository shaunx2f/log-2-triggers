from classes.LogEvents.NetworkBuff import NetworkBuff
from classes.LogEvents.NetworkAbility import NetworkAbility
from classes.LogEvents.NetworkStartsCasting import NetworkStartsCasting
from classes.LogEvents.FullPartyList import FullPartyList
from classes.LogEvents.NetworkTether import NetworkTether
from classes.LogEvents.NetworkTargetIcon import NetworkTargetIcon
from classes.LogEvents.PullEnded import PullEnded
from classes.LogEvents.ZoneChange import ZoneChange
from classes.LogEvents.LogLine import LogLine
from classes.LogEvents.AllianceParty import AllianceParty


def buff_exclusion(name):
    if name in ('Fire Resistance Down II', 'Lightning Resistance Down II', 'Physical Vulnerability Up', 'Magic Vulnerability Up', 'Vulnerability Up', 'Bleeding', 'Weakness', 'Transcendent', 'Brink of Death', 'Damage Down'):
        return True
    else:
        return False


def pets_exclusion(name):
    if name in ("Esteem", "Bunshin", "Solar Bahamut", "Ruby Carbuncle", "Topaz Carbuncle", "Emerald Carbuncle", "Liturgic Bell", "Rook Autoturret", "Automaton Queen", "Demi-Bahamut", "Demi-Phoenix", "Carbuncle", "Earthly Star", "Selene", "Eos", "Seraph", "Titan-Egi", "Garuda-Egi", "Ifrit-Egi", "Ruby Ifrit", "Topaz Titan", "Emerald Garuda"):
        return True
    else:
        return False


class LogTypeHelper:

    def __init__(self, log_line):
        self._log_line = log_line

    def get_log_type(self):
        if PullEnded.class_regex.match(self._log_line):
            return PullEnded(self._log_line)

        if ZoneChange.class_regex.match(self._log_line):
            return ZoneChange(self._log_line)

        if LogLine.class_regex.match(self._log_line):
            return LogLine(self._log_line)

        if NetworkBuff.class_regex.match(self._log_line):
            network_buff = NetworkBuff(self._log_line)
            if not pets_exclusion(network_buff.source) and not pets_exclusion(network_buff.target) and not buff_exclusion(network_buff.effect):
                return network_buff

        if NetworkAbility.class_regex.match(self._log_line):
            network_ability = NetworkAbility(self._log_line)
            if not pets_exclusion(network_ability.source) and not pets_exclusion(network_ability.target):
                return network_ability

        if NetworkStartsCasting.class_regex.match(self._log_line):
            return NetworkStartsCasting(self._log_line)

        if AllianceParty.class_regex.match(self._log_line):
            return AllianceParty(self._log_line)
        elif FullPartyList.class_regex.match(self._log_line):
            return FullPartyList(self._log_line)

        if NetworkTether.class_regex.match(self._log_line):
            return NetworkTether(self._log_line)

        if NetworkTargetIcon.class_regex.match(self._log_line):
            return NetworkTargetIcon(self._log_line)
