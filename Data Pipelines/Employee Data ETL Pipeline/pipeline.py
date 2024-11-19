from extract import extract_data as extract_employee_data
from transform import transform_data as transform_employee_data
from load import load_data_to_db

def run_etl_pipeline(file_path, db_name='employee_data.db'):
    # Extract
    data = extract_employee_data(file_path)
    if data is not None:
        # Transform
        transformed_data = transform_employee_data(data)
        if transformed_data is not None:
            # Load
            load_data_to_db(transformed_data, db_name)

# Run the ETL pipeline
run_etl_pipeline('/content/employees_data.csv', 'employee_data.db')