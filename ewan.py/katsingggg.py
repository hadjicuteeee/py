import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\\Users\\apues\\Downloads\\archive (33)\\person.csv")

#print(df.columns.tolist())

#DROP COLUMNSS
def drop_columns(df):
    return df.drop(columns=['All Time Peak', 'Peak', 'Ref.' ], errors='ignore')
#RENAME COLUMNS
def rename_columns(df):
    return df.rename(columns={"Actual\xa0gross": "Actual Gross", 
    "Adjusted\xa0gross (in 2022 dollars)": "Adjusted Gross 2022"})


#VALIDATION 
"""
def validation_concurrency_column(df, column):
    pattern =  r'^-?\$?\d{1,3}(,\d{3})*(\.\d+)?$'
    mask = df[column].astype(str).str.match(pattern, na=False)
    invalid_rows = df[~mask]
    if not invalid_rows.empty:
        print(f"Warning {len(invalid_rows)} invalid rows detected in '{column}' : ")
        print(invalid_rows[[column]])       
    return mask
"""

def convert_numeric(df):
    
    df = df.copy()

    money_cols = ['Actual Gross', 'Adjusted Gross 2022', 'Average gross']

    for col in money_cols:
        df[col] = pd.to_numeric(
            df[col].astype(str).str.replace(r'[^0-9.-]', '', regex=True),
            errors='coerce'
        )

    df['Actual Gross'] = df['Actual Gross'].fillna(df['Actual Gross'].median()).astype('Int64')

    df['Year(s)'] = df['Year(s)'].str.replace(r'[^\d,-]', '-', regex=True)
        
    df['Tour title'] =(
           df['Tour title']
            .str.replace(r'‡?\[[^\]]*\]', '', regex=True)
            .str.replace('†', '', regex=True)
            .str.strip()
        )     
        
    return df   

def data_clean(df):
    df = drop_columns(df)
    df = rename_columns(df)
    df = convert_numeric(df)

    return df
clean = data_clean(df)
print(clean)

clean.to_csv(r"C:\Users\apues\Downloads\PATH\clean_person.csv", index=False)
