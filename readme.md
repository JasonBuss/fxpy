## ICRM Python scripts
Python scripts for InforCRM

### InforCRM
Scripts designed to manipulate information in a Saleslogix/InforCRM database.
This is all pretty preliminary, so don't expect too much right now.

### Data access
These scripts do not use the Saleslogix OLEDB provider.  Instead, access is done using pymssql.
Access is defined using the sql.config file in the config folder (sample provided).  As Such, any updates 
using these scripts will not be sync-aware.