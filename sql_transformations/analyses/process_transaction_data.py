import pandas as pd
import os
import re

class Transactions:
    def __init__(self):
        # Define the path to the seed files
        self.seed_files = os.path.join(os.getcwd(), 'sql_transformations/seeds')
        self.file_name = "retail.csv"
        self.file_path = os.path.join(self.seed_files, self.file_name)
        
        # Load the CSV file into a DataFrame
        self.df = pd.read_csv(self.file_path) 

    def get_data(self):
        """Reset index and return the DataFrame."""
        data = self.df.reset_index(drop=True)
        return data

    def convert_columns_to_snake_case(self, data):
        """Convert column names from camel case to snake case."""
        data.columns = [re.sub(r'(?<!^)(?=[A-Z])', '_', col).lower() for col in data.columns]
        return data

    def ensure_unit_price_format(self, data):
        """Ensure unit price is formatted to two decimal places."""
        assert 'unit_price' in data.columns, "unit_price column is missing"
        data['unit_price'] = data['unit_price'].apply(lambda x: f"{x:.2f}" if pd.notnull(x) else x)
        return data

    def ensure_invoice_date_format(self, data):
        """Ensure invoice date is in %Y-%m-%d format."""
        assert 'invoice_date' in data.columns, "invoice_date column is missing"
        data['invoice_date'] = pd.to_datetime(data['invoice_date'], errors='coerce').dt.strftime('%Y-%m-%d')
        return data

    def clean_customer_id(self, data):
        """Rename customer_i_d to customer_id and remove decimal points."""
        assert 'customer_i_d' in data.columns, "customer_i_d column is missing"
        data.rename(columns={'customer_i_d': 'customer_id'}, inplace=True)
        
        # Handle NaN values before converting to integer
        data['customer_id'] = pd.to_numeric(data['customer_id'], errors='coerce').fillna(0).astype(int)  # Convert to integer to remove decimal points
        return data

    def save_cleaned_data(self, data, output_file):
        """Save the cleaned DataFrame to a CSV file."""
        data.to_csv(output_file, index=False)
        print(f"Cleaned data saved to {output_file}")

# Main execution
txn = Transactions()
df = txn.get_data()
df = txn.convert_columns_to_snake_case(df)
df = txn.ensure_unit_price_format(df)
df = txn.ensure_invoice_date_format(df)
df = txn.clean_customer_id(df)

# Save cleaned data to a new CSV file
output_file_path = os.path.join(txn.seed_files, 'cleaned_retail.csv')
txn.save_cleaned_data(df, output_file_path)