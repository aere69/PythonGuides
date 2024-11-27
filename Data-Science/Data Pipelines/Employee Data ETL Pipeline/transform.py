# Function to transform employee data 
def transform_data(data):
    try:
        
        # Ensure salary and age are numeric and handle any errors
        data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce')
        data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

        # Remove rows with missing values
        data = data.dropna(subset=['Salary', 'Age', 'Department'])

        # Create salary bands
        data['Salary_band'] = pd.cut(data['Salary'], bins=[0, 60000, 90000, 120000, 1500000], labels=['Low', 'Medium', 'High', 'Very High'])

        # Create age groups
        data['Age_group'] = pd.cut(data['Age'], bins=[0, 30, 40, 50, 60], labels=['Young', 'Middle-aged', 'Senior', 'Older'])

        # Convert department to categorical
        data['Department'] = data['Department'].astype('category')

        print("Data transformation complete")
        return data
    except Exception as e:
        print(f"Error in transformation: {e}")
        return None

#employee_data = extract_employee_data('/content/employees_data.csv')

# Transform the employee data
#if employee_data is not None:
#    transformed_employee_data = transform_data(employee_data)

    # Print the first few rows of the transformed data
    #print(transformed_employee_data.head())