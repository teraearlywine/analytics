"""
ANNUAL HOUSING DEVELOPMENT DATA PROCESSING
Getting data ready to be imported to MySQL 
# Assume the following is all annual #

Independent from the actual analysis, processing for mysql / bigquery injestion
"""

from src.data_cleaning import (
    # started_annual_housing_units,  # TODO, start home comparison
    completed_annual_housing_units,
    add_unique_key_and_created_ts,
)
from skimpy import skim 

# Hard copy to new variable as last leg
data = completed_annual_housing_units()
df = add_unique_key_and_created_ts(data)
skim(df)
