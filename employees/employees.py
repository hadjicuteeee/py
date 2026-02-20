import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\apues\Downloads\archive (34)\employee.csv")


#INFORMATION
#info = df.info()
#print(info)

#NO DUPLICATE FOUND
#duplicate = df.duplicated().sum()
#print(duplicate)

#PHONE DUPLICATED NONE
#phone = df.duplicated(subset=['Phone']).sum()
#print(phone)


#3 UNIQUE CATEGORY
#unique = df['Status'].unique()
#print(unique)

#4 UNIQUE CATEGORY
#unique = df['Performance_Score'].unique()
#print(unique)

def apply_phone(df):

   
    number = str(df['Phone'])
    if len(number) == 10:
        return "+1" + number
    elif len(number) == 11 and number.startswith("-"):
        return "+" + number
    else:
        return None
    

def rename(df):
    df['Phone_formatted'] = df['Phone_formatted'].str.replace("-", '', regex=False)

    return df

def drop_columns(df):
    return df.drop(columns=['Phone'], errors='ignore')

def salary_format(df):

    df['Salary_Formatted'] = df['Salary'].apply(lambda x : f"USD {x:,.2f}" if not pd.isna(x) else 'No Salary')

    return df

def age_format(df):
    
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df['Age_Formatted'] = df['Age'].fillna(df['Age'].median()).astype('Int64')
    return df 

def original_age(df):

    df['Age'] = df['Age'].apply(lambda x : str(int(x))  if not pd.isna(x) else 'Missing')

    return df

def email_format(df):                       #old       #new
    df['Email'] = df['Email'].str.replace('example', 'gmail', regex=False)
    df['Remote_Work'] = df['Remote_Work'].astype(str)
    df['Remote_Work'] = df['Remote_Work'].replace({"True":'T', "False":'F', pd.NA: "Missing", np.nan:"Missing"}, regex=False)  

    return df

def department_format(df):

    df[['Role', 'Department']] = df['Department_Region'].str.split('-', expand=True)
    
    return df

def date_format(df):

    df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')
    df['Join_Date'] = df['Join_Date'].dt.strftime("'%Y-%m-%d'")
    df['Join_Date'] = df['Join_Date'].fillna('No Date')
    return df


def cleaned_columns(df):
    df['Phone_formatted'] = df.apply(apply_phone, axis=1)
    df = rename(df)
    df = drop_columns(df)
    df = salary_format(df)
    df = age_format(df)
    df = original_age(df)
    df = email_format(df)
    df = department_format(df)
    df = date_format(df)

    return df

clean_data = cleaned_columns(df)
print(clean_data)


clean_data.to_csv(r"C:\Users\apues\Downloads\PATH\employees.cleaned.csv", index=False)
