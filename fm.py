import pandas as pd
from io import StringIO
import os
from positions_list import positions
from personalities_list import personalities

def calculate_personality_score(row):
    personality = row["Personality"]
    if personality in personalities:
        trait_values = personalities[personality]

        print(trait_values)
        num_traits = len(trait_values)
        print(num_traits)
        

        trait_score = sum(trait_values.values())
        print(trait_score)

        # Avoid division by zero if no traits are found
        if num_traits > 0:
            personality_score = (trait_score / num_traits) - (8 - num_traits)
            print(personality_score)
            return round(personality_score, 1)
        else:
            return 0.0
    else:
        return 0.0


def calculate_position_score(row, position_attributes, personality_score):
    key_score = sum(row[attr] for attr in position_attributes["key"])
    green_score = sum(row[attr] for attr in position_attributes["green"])
    blue_score = sum(row[attr] for attr in position_attributes["blue"])
    
    total_key_score = key_score + personality_score  # Adding personality score
    total_attributes = len(position_attributes["key"]) * 5 + len(position_attributes["green"]) * 3 + len(position_attributes["blue"]) + 5

    total_score = (total_key_score * 5 + green_score * 3 + blue_score) / total_attributes
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

    for column in df.columns:
        if df[column].dtype == object:
            df[column].fillna('', inplace=True)
        else:
            df[column].fillna(0.0, inplace=True)

    # Calculate personality scores once and store in the DataFrame
    df['Personality Score'] = df.apply(calculate_personality_score, axis=1)

    # Calculate scores for each position using the pre-calculated personality score
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

# Then, in your HTML template, you will replace {{table_placeholder}} with this 'html_table'


    # Read the HTML template
    with open('table_template.html', 'r') as file:
        html_template = file.read()

    # Insert the actual table data into the template
    final_html = html_template.replace('{{table_placeholder}}', html_table)

    # Write the final HTML to a file
    with open('output/enhanced_output_table.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
