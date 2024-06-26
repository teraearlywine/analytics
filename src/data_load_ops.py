import logging
from core.config_gcp import GCP
from google.cloud import bigquery
from src.data_cleaning import completed_housing_final, started_housing_final


logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d", format="%(levelname)s - %(asctime)s - %(message)s")


def load_dataframe_to_bq(df, target_table):
    """LOAD Pandas Dataframe to Bigquery Table
    Passes create if needed and write truncate parameters to handle data processing
    Data is static and table is new
    """
    gcp = GCP()
    client = bigquery.Client(project=gcp.project_id)
    logging.info(f"Connected to client, proceeding to load data to {target_table}")
    load_job = client.load_table_from_dataframe(
        dataframe=df,
        destination=target_table,
        location=gcp.location,
        job_config=bigquery.LoadJobConfig(
            create_disposition=gcp.create_if_needed,  # Create if not exists parameter
            write_disposition=gcp.write_truncate,  # For this specific use case, data is static
        ),
    )
    try:
        load_job.result()  # Wait for the job to complete.
        logging.info(f"Data loaded successfully to table")
        return True
    except Exception as err:
        logging.error(f"Houston we have a problem, see below: \n\n {err}")
        return False


if __name__ == "__main__":

    comp_target_table = "source.completed_housing_units_annual"
    comp_df = completed_housing_final()
    load_dataframe_to_bq(comp_df, comp_target_table)

    target_table = "source.started_housing_units_annual"
    df = started_housing_final()
    load_dataframe_to_bq(df, target_table)
