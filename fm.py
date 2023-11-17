import pandas as pd


def squad_html_to_dataframe(html_file):

    tables = pd.read_html(html_file)

    df = tables[0]

    return df

html_file = 'exports/squad.html'
df = squad_html_to_dataframe(html_file)

print(df)
