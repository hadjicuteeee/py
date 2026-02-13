import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['jIhAd', 'ANNA ', '  muhamMAD', None, 'sAra'],
    'age': ['20', '-5', 'unknown', '30', None],
    'salary': ['50000', 'not disclosed', '45000', None, '60000'],
    'join_date': ['2023-01-15', '15/02/2022', 'March 5 2021', None, '2024-07-01'],
    'department': ['IT', 'HR', None, 'Finance', 'it']
})

def cleaned_name(df):
     df['name'] = (
        df['name'].fillna('Unknown')
        .str.lower().str.title()
     )
     return df

def cleaned_age(df):
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['age'] = df['age'].apply(lambda x: int(x) if pd.notna(x) and x >= 0 else 'No Age')

    return df

    
def cleaned_salary(df):
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    median_salary = df['salary'].median()
    df['salary'] = df['salary'].fillna(median_salary).astype(int)

    #FOR COMMA ONLY
    #df['salary'] = df['salary'].apply(lambda x: f"{x:,}")
    return df


def cleaned_department(df):
    df['department'] = df['department'].fillna('Unassigned').str.upper()
    
    return df

def cleaned_date(df):
    df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
    df['join_date'] = df['join_date'].apply(lambda x: x.year if pd.notna(x) else 'No Date')
    df.rename(columns={'join_date': 'join_year'}, inplace=True)
    return df

def seniority_lvl(df):
    def level(age):
        if age == 'No Age':
            return 'Unknown'
        elif age >= 30:
            return 'Senior'
        elif age >= 20:
            return 'Junior'
        else:
            return 'Too young buddy'
    df['seniority_lvl'] = df['age'].apply(level)
    
    return df
           
def data_clean(df):
    df = cleaned_name(df)
    df = cleaned_age(df)
    df = cleaned_salary(df)
    df = cleaned_department(df)
    df = cleaned_date(df)
    df = seniority_lvl(df)
    return df

clean = data_clean(df)
print(clean)


   

