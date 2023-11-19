import pandas as pd
from io import StringIO
import os
from positions_list import positions
from personalities_list import personalities

def parse_individual_position(pos):
    individual_positions = []
    if 'AM ' in pos:
        if 'R' in pos:
            individual_positions.append('amr')
        if 'C' in pos:
            individual_positions.append('amc')
        if 'L' in pos:
            individual_positions.append('aml')
    elif 'M ' in pos:
        if 'C' in pos:
            individual_positions.append('mc')
        if 'L' in pos:
            individual_positions.append('ml')
        if 'R' in pos:
            individual_positions.append('mr')            
    if 'D ' in pos:
        if 'C' in pos:
            individual_positions.append('dc')
        if 'L' in pos:
            individual_positions.append('dl')
        if 'R' in pos:
            individual_positions.append('dr')
    if 'ST ' in pos:
        if 'C' in pos:
            individual_positions.append('sc')
    if 'DM' in pos:
        individual_positions.append('dm')
    if 'GK' in pos:
        individual_positions.append('gk')
    if 'WB' in pos:
        if 'L' in pos:
            individual_positions.append('wbl')
        if 'R' in pos:
            individual_positions.append('wbr')
    return individual_positions

def parse_position_string(pos_string):
    position_groups = pos_string.split(',')
    parsed_positions = []

    for group in position_groups:
        group = group.strip()

        # Handle each group that may contain slashes
        if '/' in group:
            parts = group.split('/')
            # The attributes are only associated with the last part
            attributes = parts[-1].split(' ')[-1]

            # Process each part with the attributes
            for part_index, part in enumerate(parts):
                if part_index < len(parts) - 1:
                    # For all but the last part, append the attributes
                    full_part = f"{part.strip()} {attributes}"
                else:
                    # The last part already includes the attributes
                    full_part = part.strip()

                individual_positions = parse_individual_position(full_part)
                for position in individual_positions:
                    if position not in parsed_positions:
                        parsed_positions.append(position)
        else:
            # If there's no '/', parse the group directly
            individual_positions = parse_individual_position(group)
            for position in individual_positions:
                if position not in parsed_positions:
                    parsed_positions.append(position)

    print(pos_string)
    print(parsed_positions)

    return parsed_positions



def calculate_personality_score(row):
    personality = row["Personality"]
    if personality in personalities:
        trait_values = personalities[personality]
        num_traits = len(trait_values)
        trait_score = sum(trait_values.values())

        if num_traits > 0:
            personality_score = (trait_score / num_traits) - (7 - num_traits)
            return round(personality_score, 1)
        else:
            return 0.0
    else:
        return 0.0

def calculate_position_score(row, position_attributes, personality_score, player_positions):

    #player_name = row['Name']  # Assuming 'Name' is the column with player names
    
    position_matches = any(pos in position_attributes['valid_positions'] for pos in player_positions)

    #print(f"Player: {player_name}, Position String: '{player_position_string}', Parsed Positions: {player_positions}")
    #print(f"Assessing for position: '{position_attributes['valid_positions']}', Matches: {position_matches}")

    print(row['Name'])
    print(position_attributes['valid_positions'])
    print(player_positions)
    print(position_matches)


    key_score = sum(row[attr] for attr in position_attributes["key"] if attr in row)
    green_score = sum(row[attr] for attr in position_attributes["green"] if attr in row)
    blue_score = sum(row[attr] for attr in position_attributes["blue"] if attr in row)
    
    total_key_score = key_score + personality_score
    total_attributes = len(position_attributes["key"]) * 5 + len(position_attributes["green"]) * 3 + len(position_attributes["blue"]) + 5

    total_score = (total_key_score * 5 + green_score * 3 + blue_score) / total_attributes

    #if not position_matches:
    #    total_score *= 0.75

    return round(total_score, 1)

def abbreviate_position_name(position_name):
    if '-' in position_name:
        main, sub = position_name.split(' - ')
        sub_abbreviation = ''.join(word[0].upper() for word in sub.split())
        return f'{main} - {sub_abbreviation}'
    else:
        return position_name

def squad_html_to_dataframe(html_content):
    html_stream = StringIO(html_content)
    tables = pd.read_html(html_stream)
    df = tables[0]

    # Drop 'Reg' and 'Inf' columns if they exist
    if 'Reg' in df.columns:
        df = df.drop('Reg', axis=1)
    if 'Inf' in df.columns:
        df = df.drop('Inf', axis=1)    

    for column in df.columns:
        if df[column].dtype == object:
            df[column].fillna('', inplace=True)
        else:
            df[column].fillna(0.0, inplace=True)


    # Calculate and store player positions
    df['Parsed Positions'] = df['Position'].apply(parse_position_string)

    df['Personality Score'] = df.apply(calculate_personality_score, axis=1)

    #Loops through the imported positions list
    for position, attributes in positions.items():
        column_name = abbreviate_position_name(position)
        # Pass the pre-calculated positions to calculate_position_score
        df[column_name] = df.apply(lambda row: calculate_position_score(row, attributes, row['Personality Score'], row['Parsed Positions']), axis=1)

    return df

def get_latest_file(directory, file_extension):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(file_extension)]
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

if __name__ == "__main__":
    latest_file_path = get_latest_file('fm_exports/', '.html')
    with open(latest_file_path, 'r', encoding='UTF-8') as file:
        html_content = file.read()

    df = squad_html_to_dataframe(html_content)

    html_table = df.to_html(table_id="squadTable", classes="table table-striped table-bordered", border=0, index=False)

    with open('table_template.html', 'r') as file:
        html_template = file.read()

    final_html = html_template.replace('{{table_placeholder}}', html_table)

    with open('output/enhanced_output_table.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    csv_file_path = 'output/squad_data.csv'
    df.to_csv(csv_file_path, index=False, encoding='utf-8')
