# Databricks Ingestion & Analysis

1. Create Databricks cluster
2. Set Azure Blob access key:
   spark.conf.set("fs.azure.account.key.<ACCOUNT>.blob.core.windows.net", "<KEY>")

3. Load CSV from Blob Storage
4. Run fraud_spatial_analysis.py
5. Execute SQL queries from fraud_hotspot_queries.sql
6. Visualize fraud hotspots in Databricks UI
