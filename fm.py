import pandas as pd
from io import StringIO
import os
from positions_list import positions
from personalities_list import personalities

def calculate_personality_score(row):
    personality = row["Personality"]
    if personality in personalities:
        trait_values = personalities[personality]
        num_traits = len(trait_values)
        trait_score = sum(trait_values.values())

        if num_traits > 0:
            personality_score = (trait_score / num_traits) - (8 - num_traits)
            return round(personality_score, 1)
        else:
            return 0.0
    else:
        return 0.0

def is_valid_position(player_position, valid_positions):
    player_position = player_position.lower()  # Convert to lowercase for comparison
    for pos in valid_positions:
        if pos == 'gk' and 'gk' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True
        elif pos in ['wbl', 'wbr'] and 'wb' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True
        elif pos == 'sc' and 's' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True
        elif pos == 'dmc' and 'dm' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True
        elif pos == 'mc' and 'm' in player_position and 'c' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True
        elif pos == 'amc' and 'am' in player_position and 'c' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True
        elif pos == 'dc' and 'd ' in player_position and 'c' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True
        elif pos == 'dl' and 'd' in player_position and 'l' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True
        elif pos == 'dr' and 'd' in player_position and 'r' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True            
        elif pos == 'ml' and 'm' in player_position and 'l' in player_position :
            print(pos + ' is valid position ' + player_position)
            return True     
        elif pos == 'mr' and 'm' in player_position and 'r' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True                         
        elif pos == 'aml' and 'am' in player_position and 'l' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True
        elif pos == 'amr' and 'am' in player_position and 'r' in player_position:
            print(pos + ' is valid position ' + player_position)
            return True            
    return False

def calculate_position_score(row, position_attributes, personality_score):
    player_position = row['Position'].lower()


    position_matches = is_valid_position(player_position, position_attributes['valid_positions'])

    key_score = sum(row[attr] for attr in position_attributes["key"] if attr in row)
    green_score = sum(row[attr] for attr in position_attributes["green"] if attr in row)
    blue_score = sum(row[attr] for attr in position_attributes["blue"] if attr in row)
    
    total_key_score = key_score + personality_score
    total_attributes = len(position_attributes["key"]) * 5 + len(position_attributes["green"]) * 3 + len(position_attributes["blue"]) + 5

    total_score = (total_key_score * 5 + green_score * 3 + blue_score) / total_attributes

    if not position_matches:
        total_score *= 0.75

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

    df['Personality Score'] = df.apply(calculate_personality_score, axis=1)

    for position, attributes in positions.items():
        column_name = abbreviate_position_name(position)
        df[column_name] = df.apply(lambda row: calculate_position_score(row, attributes, row['Personality Score']), axis=1)

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
