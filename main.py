#!/usr/bin/python3
import csv
import json
import sys


def generate_entries(file_name: str):
    entries = []

    # Open the basic docker-compose file and create new final file
    with (open(file_name, 'r', newline='') as csv_input):
        # Initiate CSV reader
        data_reader = csv.DictReader(csv_input, delimiter=';')
        for line_input in data_reader:

            # Read input values :
            title = line_input['title']
            raw_actions = line_input['action']  # action values must be : 1 / 2 / 3 / free / reaction
            level = line_input['level']
            raw_traits_common = line_input['trait_common']
            raw_traits_uncommon = line_input['trait_uncommon']
            domains = line_input['domains']
            cast = line_input['cast']
            area = line_input['area']
            spell_range = line_input['range']
            target = line_input['target']
            saving_throw = line_input['saving_throw']
            trigger = line_input['trigger']
            duration = line_input['duration']
            requirement = line_input['requirement']
            defense = line_input['defense']
            text = line_input['text']
            activity_name = line_input['activity_name']
            activity_action = line_input['activity_action']
            activity_text = line_input['activity_text']
            critical_success = line_input['critical_success']
            success = line_input['success']
            failure = line_input['failure']
            critical_failure = line_input['critical_failure']
            heightened1 = line_input['heightened1']
            heightened2 = line_input['heightened2']
            heightened3 = line_input['heightened3']
            heightened4 = line_input['heightened4']
            heightened5 = line_input['heightened5']
            heightened6 = line_input['heightened6']
            heightened7 = line_input['heightened7']
            heightened8 = line_input['heightened8']
            heightened9 = line_input['heightened9']
            custom_color = line_input['custom_color']
            back_icon = line_input['back_icon']

            # Create properties map with simple properties
            # custom icons : magic-shield, portal, dwennimmen, scroll-quill --> https://game-icons.net/
            json_properties = {'count': '1', 'title_size': '13', 'card_font_size': '10', 'tags': [],
                               'color': custom_color,
                               'icon_back': back_icon,
                               'title': title}

            # icons on card top right corner for spell level and action cost
            level_icon = ''
            if level:
                level_icon = f'white-book-{level}'

            action_icon = ''
            if raw_actions:
                for action in raw_actions.split(','):
                    if action == 'reaction':
                        action_icon = f'{action_icon} p2e-{action}'
                    elif action == '1' or action == 'free':
                        action_icon = f'{action_icon} p2e-{action}-action'
                    else:
                        action_icon = f'{action_icon} p2e-{action}-actions'

            json_properties['icon'] = f'{level_icon} {action_icon}'

            # create content array
            contents = []

            contents.append('p2e_start_trait_section')
            if raw_traits_common:
                for trait_com in raw_traits_common.split(','):
                    contents.append(f'p2e_trait | common | {trait_com.strip()}')
            if raw_traits_uncommon:
                for trait_uncom in raw_traits_uncommon.split(','):
                    contents.append(f'p2e_trait | uncommon | {trait_uncom.strip()}')
            contents.append('p2e_end_trait_section')

            contents.append('ruler')

            if domains:
                contents.append(f'property | Domain | {domains}')
            if cast:
                contents.append(f'property | Cast | {cast}')
            if area:
                contents.append(f'property | Area | {area}')
            if target:
                contents.append(f'property | Target | {target}')
            if spell_range:
                contents.append(f'property | Spell Range | {spell_range}')
            if saving_throw:
                contents.append(f'property | Saving Throw | {saving_throw}')
            if duration:
                contents.append(f'property | Duration | {duration}')

            if cast or area or target or spell_range or saving_throw or duration:
                contents.append('ruler')

            if trigger:
                contents.append(f'property | Trigger | {trigger}')

            if requirement:
                contents.append(f'property | Requirement | {requirement}')

            if defense:
                contents.append(f'property | Defence | {defense}')

            if trigger or requirement or defense:
                contents.append('ruler')

            if activity_name:
                contents.append(f'p2e_activity | {activity_name} | {activity_action} | {activity_text}')
                contents.append('ruler')

            contents.append(f'text | {text}')
            contents.append(f'fill | 1')

            if critical_success or success or failure or critical_failure or heightened1 or heightened2 or heightened3 \
                    or heightened4 or heightened5 or heightened6 or heightened7 or heightened8 or heightened9:
                contents.append('ruler')

            if critical_success:
                contents.append(f'property | Critical Success | {critical_success}')
            if success:
                contents.append(f'property | Success | {success}')
            if failure:
                contents.append(f'property | Failure | {failure}')
            if critical_success:
                contents.append(f'property | Critical Failure | {critical_failure}')

            if (critical_success or success or failure or critical_failure) \
                    and (
                    heightened1 or heightened2 or heightened3 or heightened4 or heightened5 or heightened6 or heightened7 or heightened8 or heightened9):
                contents.append('p2e_ruler')

            if heightened1:
                contents.append(f'property | Heightened (1) |  {heightened1}')
            if heightened2:
                contents.append(f'property | Heightened (2) |  {heightened2}')
            if heightened3:
                contents.append(f'property | Heightened (3) |  {heightened3}')
            if heightened4:
                contents.append(f'property | Heightened (4) |  {heightened4}')
            if heightened5:
                contents.append(f'property | Heightened (5) |  {heightened5}')
            if heightened6:
                contents.append(f'property | Heightened (6) |  {heightened6}')
            if heightened7:
                contents.append(f'property | Heightened (7) |  {heightened7}')
            if heightened8:
                contents.append(f'property | Heightened (8) |  {heightened8}')
            if heightened9:
                contents.append(f'property | Heightened (9) |  {heightened9}')
            json_properties['contents'] = contents

            entries.append(json_properties)

    return entries


def main():
    #  Retrieve input file name or set a default :
    try:
        file_name = sys.argv[1]
    except IndexError as index_error:
        print('File name was not provided : defaulting to expl/init_data.csv.')
        file_name = 'expl/init_data.csv'

    json_entries = generate_entries(file_name)
    with open('expl/result.json', 'w') as result_file:
        json.dump(json_entries, result_file)


if __name__ == '__main__':
    # Start logger
    print('====> Begin cards.py execution')
    try:
        # Execute the script
        main()
        print('====> End cards.py execution')
    except Exception as error:
        print(f'====> An error occurred : {error.__class__} : {error}')
        sys.exit(1)
