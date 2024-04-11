# Databricks notebook source
pip install snowflake-connector-python

# COMMAND ----------

import snowflake.connector

warehouse = dbutils.widgets.get("warehouse")
database = dbutils.widgets.get("database")
schema = dbutils.widgets.get("schema")
table = dbutils.widgets.get("table")

conn = snowflake.connector.connect(
    user="drew",
    password="********",
    account="********",
    warehouse=warehouse,
    database=database,
    schema=schema
) # Replace w/ your secret service

refresh_query = f"ALTER ICEBERG TABE {table} REFRESH '{table}/metadata/latest'"
conn.cursor().execute(refresh_query)
