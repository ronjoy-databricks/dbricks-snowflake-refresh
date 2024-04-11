# Parameterized Refresh of Snowflake Jobs from Databricks

## Description
This is sample code to refresh a Snowflake iceberg table from Databricks Tasks.

1. Notebook code with paramaters to refresh Snowflake Iceberg tables
2. A sample job definition with a Task to run the notebook

Best practice recommendation would be to add this as a task at the end of any workflows that are writing to Uniform Iceberg that will be consumed by Snowflake in order to refresh the metadata immediately.
