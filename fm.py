import pandas as pd
from io import StringIO

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

with open('exports/squad.html', 'r', encoding='UTF-8') as file:
    html_content = file.read()

df = squad_html_to_dataframe(html_content)

print(df)

for column in df.columns:
    print(column)
