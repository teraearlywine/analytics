"""
ANNUAL HOUSING DEVELOPMENT DATA PROCESSING
Getting data ready to be imported to MySQL 
# Assume the following is all annual #

Independent from the actual analysis, processing for mysql / bigquery injestion
"""

from data_cleaning import (
    started_annual_housing_units, # TODO, start home comparison
    completed_annual_housing_units,
    generate_uuid,
    current_timestamp,
    add_unique_key_and_created_ts
)


# Hard copy to new variable as last leg
data = completed_annual_housing_units()
df = add_unique_key_and_created_ts(data)
completed_housing = df.copy()
print(completed_housing.dtypes) 