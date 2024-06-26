"""CONFIG GOOGLE CLOUD PROJECT 
    
Load Job Config attributes 
https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationLoad.FIELDS.create_disposition

        
"""


class GCP:
    def __init__(self):
        self.project_id = "teradata-development"
        self.location = "US"
        self.create_if_needed = "CREATE_IF_NEEDED"
        self.create_never = "CREATE_NEVER"  # table must already exist
        self.write_truncate = "WRITE_TRUNCATE"
        self.write_append = "WRITE_APPEND"
        self.write_empty = "WRITE_EMPTY"


if __name__ == "__main__":
    GCP()
