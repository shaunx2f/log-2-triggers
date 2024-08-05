import glob
import urllib.request
import urllib.parse
import json
import copy
import os

from classes.Helpers import InputFileReader
from classes.Helpers.LogTypeHelper import LogTypeHelper

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

from classes.Party.PartyMember import PartyMember
from classes.Party.Party import Party

from classes.Pull.Pull import Pull

from classes.Templates import TriggerTemplates

# SHARED GLOBAL VARIABLES
party = Party()
pull = Pull()
in_instance = None
current_zone = None
pull_in_progress = None
# GLOBAL VARIABLES FOR STATE


def format_datetime(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")


def format_timedelta(time_delta):
    return str(time_delta).split(".")[0]


def construct_active_party_list(full_party_list: FullPartyList):
    global party
    global in_instance

    print("Updating Party List")
    party = Party()
    party_list = [
        PartyMember(full_party_list.id1, None, None),
        PartyMember(full_party_list.id2, None, None),
        PartyMember(full_party_list.id3, None, None),
        PartyMember(full_party_list.id4, None, None),
        PartyMember(full_party_list.id5, None, None),
        PartyMember(full_party_list.id6, None, None),
        PartyMember(full_party_list.id7, None, None),
        PartyMember(full_party_list.id8, None, None)
    ]
    party.update_party(party_list)
    in_instance = True


def construct_active_alliance_list(alliance_party_list: AllianceParty):
    global party
    global in_instance

    print("Updating Alliance List")
    party = Party()
    party_list = [
        PartyMember(alliance_party_list.id1, None, None),
        PartyMember(alliance_party_list.id2, None, None),
        PartyMember(alliance_party_list.id3, None, None),
        PartyMember(alliance_party_list.id4, None, None),
        PartyMember(alliance_party_list.id5, None, None),
        PartyMember(alliance_party_list.id6, None, None),
        PartyMember(alliance_party_list.id7, None, None),
        PartyMember(alliance_party_list.id8, None, None),
        PartyMember(alliance_party_list.id9, None, None),
        PartyMember(alliance_party_list.id10, None, None),
        PartyMember(alliance_party_list.id11, None, None),
        PartyMember(alliance_party_list.id12, None, None),
        PartyMember(alliance_party_list.id13, None, None),
        PartyMember(alliance_party_list.id14, None, None),
        PartyMember(alliance_party_list.id15, None, None),
        PartyMember(alliance_party_list.id16, None, None),
        PartyMember(alliance_party_list.id17, None, None),
        PartyMember(alliance_party_list.id18, None, None),
        PartyMember(alliance_party_list.id19, None, None),
        PartyMember(alliance_party_list.id20, None, None),
        PartyMember(alliance_party_list.id21, None, None),
        PartyMember(alliance_party_list.id22, None, None),
        PartyMember(alliance_party_list.id23, None, None),
        PartyMember(alliance_party_list.id24, None, None)
    ]
    party.update_party(party_list)
    in_instance = True


def change_zone(zone_change: ZoneChange):
    global current_zone
    current_zone = log_event.name
    print("Changed Zone to " + current_zone)


def get_xiv_api_job(action_hex):
    request = urllib.request.Request(
        "https://xivapi.com/Action/" + str(int(action_hex, 16)) + "?columns=ClassJobCategory.Name")
    request.add_header('User-Agent', '&lt;User-Agent&gt;')

    # These look like Food/Pots so don't call XIV API on them
    if int(action_hex, 16) > 30000000:
        return None
    try:
        data = json.loads(urllib.request.urlopen(request).read())
    except Exception:
        print("Exception calling XIVAPI for Job Details: " + request.get_full_url())
        return None
    return data


def guess_party_jobs(network_ability: NetworkAbility):
    global party

    if party is None:
        return

    if len(party.get_party()) != 4 and len(party.get_party()) != 8 and len(party.get_party()) != 24:
        return

    if network_ability.ability == 'attack':
        return

    if party.in_party(network_ability.source_id) and party.get_party_member(network_ability.source_id).job is None:
        xiv_api_response = get_xiv_api_job(network_ability.id)
        if xiv_api_response is None:
            return

        xiv_api_response = str(xiv_api_response['ClassJobCategory']['Name'])

        if " " in xiv_api_response:
            # Too many options (Shared Action like Arm's Length)
            return
        party.update_party_member(network_ability.source_id, network_ability.source, xiv_api_response)


def should_encounter_start(network_ability: NetworkAbility):
    global pull_in_progress
    global in_instance
    global pull
    global current_zone
    if pull_in_progress:
        return

    if network_ability.ability == 'attack' and in_instance:
        print("Encounter Started @ " + format_datetime(network_ability.timestamp))
        pull = Pull()
        pull.set_start_time(network_ability.timestamp)
        pull.set_zone_name(current_zone)

        pull_in_progress = True


def make_new_trigger_file(output_trigger_file: str):
    print("Writing Triggers to " + output_trigger_file)
    with open(output_trigger_file, "w", encoding="utf-8") as f:
        f.write(TriggerTemplates.new_trigger_file_start(os.path.basename(f.name)).replace(".xml", ""))


def add_pull_to_current_trigger_file(output_trigger_file: str, current_pull: Pull):
    with open(output_trigger_file, "a", encoding="utf-8") as f:
        f.write(TriggerTemplates.new_pull_folder(format_datetime(current_pull.start_time()),
                                                 format_timedelta(current_pull.end_time() - current_pull.start_time()),
                                                 pull.zone_name()))
        # Casts to Triggers
        if len(pull.casts()) > 0:
            f.write(TriggerTemplates.new_casts_folder())

            for time, cast in pull.casts():

                # In case of disconnection memes, double check that party member abilities are skipped
                if pull.party_members().in_party(cast.source_id):
                    continue

                target_role = "Fight"
                if pull.party_members().in_party(cast.target_id):
                    target_role = pull.party_members().get_party_member(cast.target_id).role

                f.write(TriggerTemplates.new_cast_trigger(format_timedelta(cast.timestamp - current_pull.start_time()),
                                                          cast.source,
                                                          cast.ability, cast.id, target_role, cast.cast_time))

            f.write(TriggerTemplates.end_casts_folder())

        if len(pull.abilities()) > 0:
            f.write(TriggerTemplates.new_abilities_folder())

            for time, ability in pull.abilities():

                # In case of disconnection memes, double check that party member abilities are skipped
                if pull.party_members().in_party(ability.source_id):
                    continue

                # Target should be boss name or id if name is empty
                target_role = ability.target
                if not target_role:
                    target_role = ability.target_id

                if pull.party_members().in_party(ability.target_id):
                    target_role = pull.party_members().get_party_member(ability.target_id).role

                f.write(TriggerTemplates.new_ability_trigger(
                    format_timedelta(ability.timestamp - current_pull.start_time()),
                    ability.source,
                    target_role, ability.ability, ability.id))

            f.write(TriggerTemplates.end_abilities_folder())

        if len(pull.tethers()) > 0:
            f.write(TriggerTemplates.new_tethers_folder())

            for time, tether in pull.tethers():

                source_role = tether.source
                if pull.party_members().in_party(tether.source_id):
                    source_role = source_role + " (" + pull.party_members().get_party_member(
                        tether.source_id).role + ")"
                else:
                    source_role = source_role + " (Fight)"

                target_role = tether.target
                if pull.party_members().in_party(tether.target_id):
                    target_role = target_role + " (" + pull.party_members().get_party_member(
                        tether.target_id).role + ")"
                else:
                    target_role = target_role + " (Fight)"
                f.write(
                    TriggerTemplates.new_tether_trigger(format_timedelta(tether.timestamp - current_pull.start_time()),
                                                        source_role,
                                                        target_role, tether.id))

            f.write(TriggerTemplates.end_tethers_folder())

        if len(pull.headmarkers()) > 0:
            f.write(TriggerTemplates.new_headmarker_folder())

            for time, headmarker in pull.headmarkers():

                target_role = "Fight"
                target_name = headmarker.target
                if not target_name:
                    target_name = headmarker.target_id
                if pull.party_members().in_party(headmarker.target_id):
                    target_role = pull.party_members().get_party_member(headmarker.target_id).role

                f.write(TriggerTemplates.new_headmarker_trigger(
                    format_timedelta(headmarker.timestamp - current_pull.start_time()),
                    target_name,
                    headmarker.id,
                    target_role))

            f.write(TriggerTemplates.end_headmarker_folder())

        if len(pull.debuffs()) > 0:
            f.write(TriggerTemplates.new_debuff_folder())

            for time, debuff in pull.debuffs():

                # Skip Debuffs applied by party/alliance members
                if pull.party_members().in_party(debuff.source_id):
                    continue

                target_role = "Fight"
                source = debuff.source

                if not source:
                    source = debuff.source_id

                if pull.party_members().in_party(debuff.target_id):
                    target_role = pull.party_members().get_party_member(debuff.target_id).role

                f.write(
                    TriggerTemplates.new_debuff_trigger(format_timedelta(debuff.timestamp - current_pull.start_time()),
                                                        source,
                                                        debuff.effect,
                                                        debuff.effect_id,
                                                        debuff.duration,
                                                        debuff.count,
                                                        debuff.target,
                                                        target_role
                                                        ))

            f.write(TriggerTemplates.end_debuff_folder())

        f.write(TriggerTemplates.end_pull_folder())


def end_trigger_file(output_trigger_file: str):
    print(output_trigger_file + " Completed")
    with open(output_trigger_file, "a", encoding="utf-8") as f:
        f.write(TriggerTemplates.new_trigger_file_end())


def should_encounter_end(pull_ended: PullEnded, output_trigger_file: str):
    global pull_in_progress
    global in_instance
    global pull
    global party
    if pull_in_progress and in_instance:
        pull_in_progress = False
        pull.set_end_time(pull_ended.timestamp)
        pull.set_party_members(copy.deepcopy(party))
        print("Encounter Ended @ " + format_datetime(pull_ended.timestamp))
        print(str(pull))
        print(pull.zone_name())
        print("Casts: " + str(len(pull.casts())))
        print("Debuffs: " + str(len(pull.debuffs())))
        print("Headmarker: " + str(len(pull.headmarkers())))
        print("Tethers: " + str(len(pull.tethers())))
        print("Abilities: " + str(len(pull.abilities())))

        print(str(pull.party_members()))
        if len(pull.events()) > 0:
            add_pull_to_current_trigger_file(output_trigger_file, pull)

        print("\n\n\n\n")


def add_ability_to_pull(network_ability: NetworkAbility):
    global party
    global pull_in_progress
    global pull

    if not pull_in_progress:
        return

    if not party.in_party(network_ability.source_id):
        pull.add_event(network_ability.timestamp, network_ability)
        pull.add_ability(network_ability.timestamp, network_ability)


def add_cast_to_pull(network_cast: NetworkStartsCasting):
    global party
    global pull_in_progress
    global pull

    if not pull_in_progress:
        return

    if not party.in_party(network_cast.source_id):
        pull.add_event(network_cast.timestamp, network_cast)
        pull.add_cast(network_cast.timestamp, network_cast)


def add_debuff_to_pull(network_debuff: NetworkBuff):
    global party
    global pull_in_progress
    global pull

    if not pull_in_progress:
        return

    if not party.in_party(network_debuff.source_id):
        pull.add_event(network_debuff.timestamp, network_debuff)
        pull.add_debuff(network_debuff.timestamp, network_debuff)


def add_tether_to_pull(network_tether: NetworkTether):
    global party
    global pull_in_progress
    global pull

    if not pull_in_progress:
        return

    pull.add_event(network_tether.timestamp, network_tether)
    pull.add_tethers(network_tether.timestamp, network_tether)


def add_headmarker_to_pull(network_headmarker: NetworkTargetIcon):
    global party
    global pull_in_progress
    global pull

    if not pull_in_progress:
        return

    pull.add_event(network_headmarker.timestamp, network_headmarker)
    pull.add_headmarker(network_headmarker.timestamp, network_headmarker)


def should_clear_party_list(log_line: LogLine):
    global party
    global in_instance
    if " has ended." in log_line.line or " wurde beendet." in log_line.line or " prend fin." in log_line.line or "の攻略を終了した。" in log_line.line:
        print("Left Instance! Clearing active party list!")
        party.clear_party()
        party = Party()
        in_instance = False


# File and Pull Maker
log_file_list = glob.glob('input/*.log')

if len(log_file_list) == 0:
    print("Could not locate any log files for parsing :(\n1. Are there any log files in the folder?\n2. Are you running the script INSIDE the log2trigger folder?")

for log_file in log_file_list:

    print("Reading logs from " + log_file)
    output_file_name = ".\\" + log_file.replace(".log", ".xml").replace("input", "output")
    make_new_trigger_file(output_file_name)

    for log_line in InputFileReader.read_log_lines_from_file(log_file_list[0]):
        log_event = LogTypeHelper(log_line[:-1]).get_log_type()

        if isinstance(log_event, PullEnded):
            should_encounter_end(log_event, output_file_name)

        if isinstance(log_event, ZoneChange):
            change_zone(log_event)

        if isinstance(log_event, AllianceParty):
            construct_active_alliance_list(log_event)

        if isinstance(log_event, FullPartyList):
            construct_active_party_list(log_event)

        if isinstance(log_event, NetworkAbility):
            guess_party_jobs(log_event)
            add_ability_to_pull(log_event)

        if isinstance(log_event, LogLine):
            should_clear_party_list(log_event)

        if isinstance(log_event, NetworkAbility):
            should_encounter_start(log_event)

        if isinstance(log_event, NetworkStartsCasting):
            add_cast_to_pull(log_event)

        if isinstance(log_event, NetworkBuff):
            add_debuff_to_pull(log_event)

        if isinstance(log_event, NetworkTether):
            add_tether_to_pull(log_event)

        if isinstance(log_event, NetworkTargetIcon):
            add_headmarker_to_pull(log_event)

    end_trigger_file(output_file_name)
