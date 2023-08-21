import os
import requests
import pandas as pd
import psycopg2

# Download the Excel file from the internet
def download_excel(url, download_path):
    response = requests.get(url)
    with open(download_path, 'wb') as f:
        f.write(response.content)

# Process Excel data and insert into PostgreSQL
def process_and_insert_excel(excel_path, db_connection):
    # Load Excel data into a DataFrame
    
    df = pd.read_excel(excel_url, sheet_name=1)
    df = df.drop(0)

    # Database connection
    conn = psycopg2.connect(**db_connection)
    cursor = conn.cursor()

    # Iterate through the DataFrame and insert into PostgreSQL
    for index, row in df.iterrows():
        # Customize this INSERT query based on your table structure
        insert_query = f"INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"
        values = (row['Company name'], row['Company Status Text'])
        cursor.execute(insert_query, values)
        # don't forget to delete this!!
        if index > 10:
            break

    conn.commit()
    conn.close()

if __name__ == '__main__':
    excel_url = 'https://sciencebasedtargets.org/resources/files/SBTiProgressReport2021AppendixData.xlsx'
    download_path = 'downloaded_excel.xlsx'
    
    db_connection = {
        'host': 'localhost',
        'database': 'sbti',
        'user': 'your_username',
        'password': 'your_password'
    }
    # port is 5432
    # Download the Excel file
    download_excel(excel_url, download_path)

    # Process and insert into PostgreSQL
    process_and_insert_excel(download_path, db_connection)

    # Clean up downloaded file
    os.remove(download_path)
