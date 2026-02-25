import matplotlib.pyplot as plt
from cleaning_messy import clean_get_data
import pandas as pd

file_path =  r"C:\\Users\\apues\\Downloads\\PATH\\messy_customers_dataset.csv"
df = clean_get_data(file_path)

if df is None:
    print("Data failed to load")
    exit()


def top_5_country(df):
    try:
        top5 = df.groupby('Location')['Salary'].sum().sort_values(ascending=False).head(5)
        print("Top 5 countries: \n", top5)

        
        plt.figure(figsize=(8,5))
        top5.plot(kind='bar', color='skyblue')
        plt.title("Top 5 Countries by Salary")
        plt.xlabel("Country")
        plt.ylabel("Total Salary")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return top5

    except KeyError as e:
        print(f"Error found in {e}")
        return None
    except Exception as e:
        print(f"Error found in {e}")
        return None

def bday(df):
    try:
        df['Birthday'] = pd.to_datetime(df['Birthday'], errors='coerce')
        month_counts = df['Birthday'].dt.month_name().value_counts().reindex([
            "January","February","March","April","May","June","July","August",
            "September","October","November","December"], fill_value=0)

        print("Birthday Distribution by Month:\n", month_counts)

        plt.figure(figsize=(10,5))
        month_counts.plot(kind='bar', color='violet')
        plt.title("Birthday Distribution by Month")
        plt.xlabel("Month")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return month_counts

    except Exception as e:
        print(f"Error found: {e}")
        return None


def marital_status_analysis(df):
    try:
        counts = df['Status'].value_counts(dropna=False)
        print("Marital Status: \n", counts)

        plt.figure(figsize=(6,6))
        counts.plot(kind='pie', autopct='%1.1f%%', startangle=90,
                 colors=['lightgreen','lightcoral','lightblue'])
        plt.title("Marital Status Distribution")
        plt.ylabel("")
        plt.show()

        return counts

    except KeyError as e:
        print(f"Error found: {e}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None
         
def course_count(df):
    try:
        course_count = df['Course'].value_counts(dropna=False)
        print("Course Count: \n", course_count)

        plt.figure(figsize=(10,5))
        course_count.plot(kind='bar', color='green')
        plt.title("Course Count")
        plt.xlabel("Course")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return course_count

    except KeyError as e:
        print(f"Error found: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

    

def location_count(df):
    try:
        location_count = df['Location'].value_counts(dropna=False)
        print("Population per location: \n", location_count)

        plt.figure(figsize=(10,5))
        location_count.plot(kind='bar', color='purple')
        plt.title("Population per Location")
        plt.xlabel("Location")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return location_count

    except KeyError as e:
        print(f"Error found: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def person_with_highest_salary(df):
    try:
        salary = df.groupby('Name')['Salary'].sum().sort_values(ascending=False).head(5)
        print("Top 5 Earners : \n", salary)

        import matplotlib.pyplot as plt
        plt.figure(figsize=(8,5))
        salary.plot(kind='line', color='skyblue')
        plt.title("Top 5 Earners")
        plt.xlabel("Name")
        plt.ylabel("Salary")
        plt.xticks(rotation=40)
        plt.tight_layout()
        plt.show()    

        return salary

    except Exception as e:
        print("Error found in {e}")
        return None
    


if __name__ == "__main__":
    top_5_country(df)
    bday(df)
    marital_status_analysis(df)
    course_count(df)
    location_count(df)
    person_with_highest_salary(df)



