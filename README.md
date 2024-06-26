# Analytics Repository 

This repository is the meat and potatoes -- here's where you'll find the source code supporting research and analytics projects that I'm actively looking into. 

## Core Sub-Directory 

The core sub-directory contains constants and configurations relating to the ELT or ETL scripts going on in src. Currently, there's schema & config_gcp. Schema contains column names in lower case for updating the census headers. Since all of the tabs in each .xlsx file contain the same formatting, this is an appropriate way to normalize the schema headers for future processing. 


## Src Sub-Directory

Following the python 'source' code naming conventions, this sub-directory contains the source code. It may be worthwhile in the future to refactor data cleaning. The pandas transformations are a little verbose and cumbersome. Placing into a class we could use private / public functions for portability purposes. 