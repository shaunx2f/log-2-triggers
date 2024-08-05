import uuid


# New Pull

def new_trigger_file_start(file_name: str):
    return """<?xml version="1.0"?>
<TriggernometryExport Version="1">
  <ExportedFolder Id="random_uuid" Name="Log2Triggers - file_name" Enabled="true">
    <Folders>

""".replace("random_uuid", str(uuid.uuid4())).replace("file_name", file_name)


def new_trigger_file_end():
    return """
    </Folders>
    <Triggers />
  </ExportedFolder>
</TriggernometryExport>
"""


def new_pull_folder(timestamp, pull_time, instance_name):
    return """                  
        <Folder Id="random_uuid" Name="timestamp - pull_time - instance_name_template" Enabled="false">
            <Folders>
""".replace("random_uuid", str(uuid.uuid4())).replace("pull_time", pull_time).replace("instance_name_template", instance_name).replace("timestamp", timestamp)


def end_pull_folder():
    return """
            </Folders>
            <Triggers />
        </Folder>
"""


# End Pull

# Cast Folder within Pull
def new_casts_folder():
    return """
                <Folder Id="random_uuid" Name="Casts" Enabled="true">
                    <Folders />
                    <Triggers>
""".replace("random_uuid", str(uuid.uuid4()))


def new_cast_trigger(cast_start_time, boss_name, cast_name, cast_id, target_role, cast_length):
    return ("""
                        <Trigger Enabled="true" Source="FFXIVNetwork" Name="pull_time_template - Source: boss_name_template - Cast: trigger_name_template - cast_id Target: target_role_template Duration: cast_time_template" Id="random_uuid" RegularExpression="^20\\|[^|]*\\|[^|]*\\|[^|]*\\|cast_id\\|">
                            <Actions>
                                <Action OrderNumber="1" UseTTSTextExpression="trigger_name_template" ActionType="UseTTS">
                                    <Condition Enabled="false" Grouping="Or" />
                                </Action>
                            </Actions>
                            <Condition Enabled="false" Grouping="Or" />
                            <Conditions />
                        </Trigger>
""".replace("random_uuid", str(uuid.uuid4()))
            .replace("pull_time_template", cast_start_time)
            .replace("boss_name_template", boss_name)
            .replace("trigger_name_template", cast_name)
            .replace("cast_id", cast_id)
            .replace("target_role_template", target_role)
            .replace("cast_time_template", cast_length))


def end_casts_folder():
    return """
                    </Triggers>
                </Folder>
"""


# End Cast Folder within Pull

# Coordinate Cast Folder within Pull
def new_casts_folder_with_coordinates():
    return ''


def new_cast_trigger_with_coordinates():
    return ''


def end_casts_folder_with_coordinates():
    return ''


# End Coordinate Cast Folder within Pull

# Ability Folder within Pull
def new_abilities_folder():
    return """
                <Folder Id="random_uuid" Name="Abilities" Enabled="true">
                    <Folders />
                    <Triggers>
""".replace("random_uuid", str(uuid.uuid4()))


def new_ability_trigger(ability_start_time, source_name, target_name, ability_name, ability_id):
    return """
                        <Trigger Enabled="true" Source="FFXIVNetwork" Name="pull_time_template - Source: source_name_template Target: target_name_template Ability: ability_name_template - ability_id" Id="random_uuid" RegularExpression="^(?&lt;type&gt;2[12])\\|(?&lt;timestamp&gt;[^|]*)\\|(?&lt;sourceId&gt;[^|]*)\\|(?&lt;source&gt;[^|]*)\\|ability_id\\|ability_name_template\\|(?&lt;targetId&gt;[^|]*)\\|(?&lt;target&gt;[^|]*)\\|" PeriodRefire="Deny" RefirePeriodExpression="500">
                            <Actions>
                                <Action OrderNumber="1" UseTTSTextExpression="ability_name_template" ActionType="UseTTS">
                                    <Condition Enabled="false" Grouping="Or" />
                                </Action>
                            </Actions>
                            <Conditions />
                        </Trigger>
""".replace("random_uuid", str(uuid.uuid4())).replace("pull_time_template", ability_start_time).replace("source_name_template", source_name).replace("target_name_template", target_name).replace("ability_name_template", ability_name).replace("ability_id", ability_id)


def end_abilities_folder():
    return """
                    </Triggers>
                </Folder>
"""


# End Ability Folder within Pull

# Coordinate Abilities Folder within Pull
def new_abilities_folder_with_coordinates():
    return ''


def new_ability_trigger_with_coordinates():
    return ''


def end_abilities_folder_with_coordinates():
    return ''


# End Coordinate Abilities Folder within Pull

# Tether Folder within Pull

def new_tethers_folder():
    return """
                <Folder Id="random_uuid" Name="Tethers" Enabled="true">
                    <Folders />
                    <Triggers>
""".replace("random_uuid", str(uuid.uuid4()))


def new_tether_trigger(cast_time_template, source_name_template, target_name_template, tether_id):
    return ("""
                        <Trigger Enabled="true" Source="FFXIVNetwork" Name="cast_time_template - source_name_template &lt;-&gt; target_name_template - tether_id" Id="random_uuid" RegularExpression="^35\\|(?&lt;timestamp&gt;[^|]*)\\|(?&lt;sourceId&gt;[^|]*)\\|(?&lt;source&gt;[^|]*)\\|(?&lt;targetId&gt;[^|]*)\\|(?&lt;target&gt;[^|]*)\\|(?:[^|]*\\|){2}tether_id\\|" PeriodRefire="Deny" RefirePeriodExpression="500">
                            <Actions>
                                <Action OrderNumber="1" UseTTSTextExpression="tether" ActionType="UseTTS">
                                    <Condition Enabled="false" Grouping="Or" />
                                </Action>
                            </Actions>
                            <Condition Enabled="true" Grouping="Or">
                              <ConditionSingle Enabled="true" ExpressionL="${source}" ExpressionTypeL="String" ExpressionR="${_ffxivplayer}" ExpressionTypeR="String" ConditionType="StringEqualNocase" />
                              <ConditionSingle Enabled="true" ExpressionL="${target}" ExpressionTypeL="String" ExpressionR="${_ffxivplayer}" ExpressionTypeR="String" ConditionType="StringEqualNocase" />
                            </Condition>
                            <Conditions />
                      </Trigger>
""".replace("random_uuid", str(uuid.uuid4()))
            .replace("cast_time_template", cast_time_template)
            .replace("source_name_template", source_name_template)
            .replace("target_name_template", target_name_template)
            .replace("tether_id", tether_id))


def end_tethers_folder():
    return """
                    </Triggers>
                </Folder>
"""


# End Tether Folder within Pull

# Start Debuff Folder within Pull

def new_debuff_folder():
    return """
                <Folder Id="random_uuid" Name="Debuffs" Enabled="true">
                    <Folders />
                    <Triggers>
""".replace("random_uuid", str(uuid.uuid4()))


def new_debuff_trigger(cast_time_template, source_name_template, trigger_name_template, debuff_id, duration_template, count_template, target_name, role_template):
    return ("""
                        <Trigger Enabled="true" Source="FFXIVNetwork" Name="cast_time_template - source_name_template - trigger_name_template - debuff_id - duration_template - count_template - target_name - role_template" Id="random_uuid" RegularExpression="^26\\|[^|]*\\|debuff_id\\|[^|]*\\|duration_template\\|[^|]*\\|[^|]*\\|[^|]*\\|(?&lt;name&gt;[^|]*)\\|(?&lt;count&gt;[^|]*)\\|" PeriodRefire="Deny" RefirePeriodExpression="500">
                            <Actions>
                                <Action OrderNumber="1" UseTTSTextExpression="trigger_name_template" ActionType="UseTTS">
                                    <Condition Enabled="false" Grouping="Or" />
                                </Action>
                            </Actions>
                            <Condition Enabled="true" Grouping="Or">
                              <ConditionSingle Enabled="true" ExpressionL="${name}" ExpressionTypeL="String" ExpressionR="${_ffxivplayer}" ExpressionTypeR="String" ConditionType="StringEqualNocase" />
                            </Condition>
                            <Conditions />
                      </Trigger>
""".replace("random_uuid", str(uuid.uuid4()))
            .replace("cast_time_template", cast_time_template)
            .replace("source_name_template", source_name_template)
            .replace("trigger_name_template", trigger_name_template)
            .replace("debuff_id", debuff_id)
            .replace("duration_template", duration_template)
            .replace("count_template", count_template)
            .replace("target_name", target_name)
            .replace("role_template", role_template))


def end_debuff_folder():
    return """
                    </Triggers>
                </Folder>
"""

# Headmarker Folder within Pull

def new_headmarker_folder():
    return """
                <Folder Id="random_uuid" Name="Headmarkers" Enabled="true">
                    <Folders />
                    <Triggers>
""".replace("random_uuid", str(uuid.uuid4()))


def new_headmarker_trigger(cast_time_template, target_name_template, headmarker_id, role_name_template):
    return """
                        <Trigger Enabled="true" Source="FFXIVNetwork" Name="cast_time_template - target_name_template - headmarker_id - role_name_template" Id="random_uuid" RegularExpression="^27\\|(?&lt;timestamp&gt;[^|]*)\\|(?&lt;targetId&gt;[^|]*)\\|(?&lt;target&gt;[^|]*)\\|(?:[^|]*\\|){2}headmarker_id\\|" PeriodRefire="Deny" RefirePeriodExpression="500">
                            <Actions>
                                <Action OrderNumber="1" UseTTSTextExpression="headmarker" ActionType="UseTTS">
                                    <Condition Enabled="false" Grouping="Or" />
                                </Action>
                            </Actions>
                            <Condition Enabled="true" Grouping="Or">
                              <ConditionSingle Enabled="true" ExpressionL="${target}" ExpressionTypeL="String" ExpressionR="${_ffxivplayer}" ExpressionTypeR="String" ConditionType="StringEqualNocase" />
                            </Condition>
                            <Conditions />
                      </Trigger>
""".replace("random_uuid", str(uuid.uuid4())).replace("cast_time_template", cast_time_template).replace("target_name_template", target_name_template).replace("headmarker_id", headmarker_id).replace("role_name_template", role_name_template)


def end_headmarker_folder():
    return """
                    </Triggers>
                </Folder>
"""

# End Headmarker Folder within Pull
