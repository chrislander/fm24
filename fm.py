import pandas as pd
from io import StringIO
import os
from positions_list import positions

def squad_html_to_dataframe(html_content):
    # Use StringIO to create a file-like object from the HTML string
    html_stream = StringIO(html_content)
    
    tables = pd.read_html(html_stream)

    df = tables[0]

    # Apply fillna based on column data type
    for column in df.columns:
        if df[column].dtype == object:  # For object type columns, fill with empty string
            df[column].fillna('', inplace=True)
        else:
            df[column].fillna(0.0, inplace=True)  # For numeric type columns, fill with 0.0

    return df    

# Function to get the most recent file in a directory
def get_latest_file(directory, file_extension):
    # List all files in the directory with the specified extension
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(file_extension)]
    # Sort files by modification time, latest first
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

# Use the function to get the latest .html file
latest_file_path = get_latest_file('exports/', '.html')

# Read the content from the latest file
with open(latest_file_path, 'r', encoding='UTF-8') as file:
    html_content = file.read()

# Existing code remains the same for processing the HTML content
df = squad_html_to_dataframe(html_content)
print(df)

for column in df.columns:
    print(column)

number_of_positions = len(positions)

print("Total number of positions:", number_of_positions)


'''

for position, attributes in positions.items():
    key_score = sum(squad_rawdata[attr] for attr in attributes["key"])
    green_score = sum(squad_rawdata[attr] for attr in attributes["green"])
    blue_score = sum(squad_rawdata[attr] for attr in attributes["blue"])
    total_score = (key_score * 5 + green_score * 3 + blue_score) / <appropriate divisor>
    squad_rawdata[f'{position.replace(" ", "_").lower()}_score'] = total_score.round(1)
'''

