import pandas as pd
import numpy as np


#We have 50 duplicated datas here
#drop = df.duplicated().sum()
#print(drop)

#Datatypes
#info = df.info()
#print(info)
#null : names : 0 , birthday: 0 , location: 59, status: 42, course: 125, salary: 661
#name = df.isnull().sum()
#print(name)

#Dropping duplicates data
#data = df.drop_duplicates(inplace=True)


def file_load(path):
    try:
        df = pd.read_csv(path)
        print("Successss")
        return df
    except FileNotFoundError:
        print("No file has found", path)
        return None
    except Exception as e:
        print("Unexpected Error has hound", e)
        return None


file_path = r"C:\Users\apues\Downloads\PATH\messy_customers_dataset.csv"

df = file_load(file_path)

def rename_columns(df):

    df.rename(columns={'name': 'Name',
                       'birthday': 'Birthday',
                       'location': 'Location',
                       'status': 'Status',
                       'course': 'Course',
                       'salary': 'Salary'                                               
                        }, inplace=True)
    return df

def rename_names(df):
    try:
        df['Name'] = (
            df['Name']
            .fillna('No Name')
            .str.lower()
            .str.title()
            .str.strip()
        )
        
    except KeyError as e:
        return f"No column found : {e}"
    except Exception as e:
        return f"Error found : {e}"
    
    try:
        df['Location'] = (
            df['Location'].fillna('No location')
            .str.lower()
            .str.title()
            .str.strip()
        )
    except KeyError as e:
        return "No column found {e}"
    except Exception as e:
        return "Errors detect {e}"

    try:
        df['Salary'] = df['Salary'].fillna(df['Salary'].median())
        #df['Salary'] = df['Salary'].apply(lambda x : f"{x:,.2f}")
    except KeyError as E:
        return "No column found {e}"
    except Exception as e:
        return "Error detect {e}"
    df['Status'] = df['Status'].fillna('No Gender').str.capitalize()

    df['Course'] = df['Course'].fillna('No Course')


    return df
    


def clean_get_data(path):
    df = file_load(path)

    if df is None:
        return None

    df = rename_columns(df)
    df = rename_names(df)

    return df

if __name__ == "__main__":
    file_path = r"C:\\Users\\apues\\Downloads\\PATH\\messy_customers_dataset.csv"
    df = clean_get_data(file_path)
    print(df.head(10))



