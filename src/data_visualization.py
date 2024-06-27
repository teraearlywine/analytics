from google.cloud import bigquery
from core.config_gcp import GCP
import os
import pandas as pd

def read_sql(sql_file_path):

    with open(sql_file_path, 'r') as file:
        query = file.read()
    return query

sql_file_path = os.path.join(os.getcwd(), "src/queries", "completed_housing_units_per_annum.sql")

query = read_sql(sql_file_path)

gcp = GCP()
client = bigquery.Client(project=gcp.project_id)
query_job = client.query(query)
result = query_job.result()

df = result.to_dataframe()
