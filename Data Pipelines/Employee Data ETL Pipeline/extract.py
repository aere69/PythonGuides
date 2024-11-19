import pandas as pd

# Function to extract data from a CSV file
def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data extracted from {file_path}")
        return data
    except Exception as e:
        print(f"Error in extraction: {e}")
        return None

# Extract employee data
#employee_data = extract_data('/content/employees_data.csv')

# Print the first few rows of the data
#if employee_data is not None:
#    print(employee_data.head())