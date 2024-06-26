"""HOUSING DEVELOPMENT DATA CLEANING 

This data processing script takes the data from census link and
cleans it for further analysis. The data is in raw form and most of the 
formatting has been removed (via column renaming). 

The excel files are the only option available to download from census. They can be found in core/data 
and are current as of 2023
"""
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='openpyxl')

import pandas as pd
import os
import uuid
from datetime import datetime
from core.schema import housing_schema

# Function to generate a UUID
def generate_uuid():
    return str(uuid.uuid4())


def current_timestamp():
    return datetime.now()


def add_unique_key_and_created_ts(data):
    # Adding unique key and record created timestamp to dataframe
    data["uuid"] = data.apply(lambda _: generate_uuid(), axis=1)
    data["created_ts"] = data.apply(lambda _: current_timestamp(), axis=1)
    return data


def completed_annual_housing_units():
    """
    Completed Annual Housing Units
    -------------------------------
    Tracks per year housing units completed.
    Reads excel file and then cleans data from the completed annual housing units dating back to 1974.
    https://www.census.gov/construction/nrc/data/series.html

    Returns
    -------
        Pandas dataframe
    """

    file_path = os.path.join(os.getcwd(), "core/data", "comps_quarterly_cust.xlsx")
    df = pd.read_excel(file_path, header=4)
    df_copy = df.copy() # Copy to preserve original data 
    df_cleaned = df_copy.dropna(how="all")  # Drop rows where all elements are NaN
    df_cleaned.columns = (
        df_cleaned.columns.str.strip()
        .str.replace("\n", " ")
        .str.replace(r"\s+", " ", regex=True)
    )
    df_final = df_cleaned.dropna(subset=["Year"])
    df_final.reset_index(drop=True, inplace=True)
    df_final.columns = housing_schema
    non_numeric_years = df_final[~df_final["year"].astype(str).str.isnumeric()]
    df_final_cleaned = df_final.drop(non_numeric_years.index)
    df_final_cleaned["year"] = df_final_cleaned["year"].astype(int)
    return df_final_cleaned


def started_annual_housing_units():
    """
    Started Annual Housing Units
    -------------------------------
    Tracks per year housing units started.
    Reads excel file and then cleans data from the started annual housing units dating back to 1974.
    https://www.census.gov/construction/nrc/data/series.html

    Returns
    -------
    Pandas dataframe
    """

    file_path = os.path.join(os.getcwd(), "core/data", "starts_quarterly_cust.xlsx")
    df = pd.read_excel(file_path, header=4)
    df_copy = df.copy() # Copy to preserve original data 

    df_cleaned = df_copy.dropna(how="all")  # Drop rows where all elements are NaN
    df_cleaned.columns = (
        df_cleaned.columns.str.strip()
        .str.replace("\n", " ")
        .str.replace(r"\s+", " ", regex=True)
    )
    df_final = df_cleaned.dropna(subset=["Year"])
    df_final.reset_index(drop=True, inplace=True)
    df_final.columns = [
        "year",
        "single_family_total",
        "single_family_built_for_sale",
        "single_family_fee_simple",
        "single_family_contractor_built",
        "single_family_owner_built",
        "single_family_detached",
        "single_family_attached",
        "single_family_median_square_feet",
        "single_family_average_square_feet",
        "multi_family_total",
        "multi_family_for_sale",
        "multi_family_for_rent",
        "multi_family_2_to_4_units",
        "multi_family_5_to_9_units",
        "multi_family_10_to_19_units",
        "multi_family_20_or_more_units",
        "multi_family_median_square_feet_per_unit",
        "multi_family_average_square_feet_per_unit",
    ]
    non_numeric_years = df_final[~df_final["year"].astype(str).str.isnumeric()]
    df_final_cleaned = df_final.drop(non_numeric_years.index)
    df_final_cleaned["year"] = df_final_cleaned["year"].astype(int)
    return df_final_cleaned


if __name__ == "__main__":

    started_annual_housing_units()
    completed_annual_housing_units()
