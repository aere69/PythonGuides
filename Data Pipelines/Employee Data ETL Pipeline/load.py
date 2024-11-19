import sqlite3

# Function to load transformed data into SQLite database
def load_data_to_db(data, db_name='employee_data.db'):
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                salary REAL,
                age INTEGER,
                department TEXT,
                salary_band TEXT,
                age_group TEXT
            )
        ''')

        # Insert data into the employees table
        data.to_sql('employees', conn, if_exists='replace', index=False)

        # Commit and close the connection
        conn.commit()
        print(f"Data loaded into {db_name} successfully")

        # Query the data to verify it was loaded
        query = "SELECT * FROM employees"
        result = conn.read_sql(query, conn)
        print("\nData loaded into the database:")
        print(result.head())  # Print the first few rows of the data from the database

        conn.close()
    except Exception as e:
        print(f"Error in loading data: {e}")

#load_data_to_db(transformed_employee_data)