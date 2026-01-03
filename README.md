

# 🌍 Geo-Spatial Financial Fraud Detection System

> **Industry Context:** Banking & Financial Services
> **Cloud Stack:** Azure · Databricks · Spark · SQL
> **Disclaimer:** This project uses **fully synthetic (dummy) data** for demonstration purposes only.



##  Project Overview

This project demonstrates an **end-to-end geo-spatial fraud detection pipeline** for credit card transactions, designed to mirror real-world banking analytics workflows.

The system simulates a realistic transaction dataset, ingests it into **Azure Blob Storage**, processes it using **Apache Spark on Databricks**, applies **geo-spatial anomaly detection**, and analyzes **fraud hotspots using SQL**.

The core objective is to identify:

* **Improbable geographic behavior** (e.g., impossible travel between transactions)
* **Fraud concentration patterns** across cities



##  Objectives

The project was built with the following goals:

1. **Simulate realistic financial transaction data** without using sensitive or proprietary datasets
2. **Demonstrate cloud-native data ingestion** using Azure Blob Storage
3. **Process large-scale data using Spark** on Databricks
4. **Engineer geo-spatial fraud features** using distance-based logic
5. **Identify fraud hotspots using SQL analytics**
6. **Present a complete, well-documented analytics pipeline** suitable for a banking environment

---

##  Synthetic Data Design

To avoid using real financial data, a **synthetic dataset of 10,000 credit card transactions** is generated.

### Key Design Characteristics

* **Class imbalance:** ~2% of transactions labeled as fraudulent
* **Realistic fraud behavior:**

  * Fraud transactions have higher average amounts
  * Fraud events are geographically dispersed
* **Time-based realism:** Transactions span a full year
* **Geographic realism:** Transactions occur near real city centers

### Fields Included

Each transaction includes:

* Transaction ID (unique identifier)
* User ID (cardholder identifier)
* Transaction amount
* Timestamp
* Merchant name
* City
* Latitude & Longitude
* Fraud label (IsFraud)

The dataset intentionally embeds subtle patterns that mimic real fraud scenarios while remaining statistically noisy, as real-world fraud data typically is.

---

##  Cloud Storage Layer (Azure Blob Storage)

Azure Blob Storage is used as the **data lake** for this project.

### Why Blob Storage?

* Scalable object storage
* Commonly used in enterprise analytics pipelines
* Integrates seamlessly with Databricks and Spark

The project documentation includes:

* Azure CLI-based provisioning steps
* Python SDK-based upload examples
* Guidance for using **Azurite** (Azure Storage Emulator) for free local testing

This demonstrates both **cloud familiarity** and **cost-aware development practices**.

---

##  Big-Data Processing with Databricks & Spark

The dataset is processed using **Apache Spark** in **Databricks** (Community Edition or Azure Databricks).

### Spark Responsibilities

* Read data directly from Azure Blob Storage
* Infer schema and handle large-scale processing
* Apply window functions for per-user transaction analysis
* Support both PySpark transformations and SQL analytics

Spark enables this pipeline to scale naturally from thousands to **millions of transactions** with minimal changes.

---

##  Geo-Spatial Fraud Detection Logic

### Core Idea: Impossible Travel Detection

A common fraud signal in banking is **impossible geographic movement**:

* A card used in two distant locations within a short time window

To detect this, the project computes the **distance between consecutive transactions per user** using the **Haversine formula**, which calculates great-circle distance on Earth.

### Engineered Features

For each transaction:

* Distance from previous transaction (km)
* Time since previous transaction (minutes)
* Boolean flag indicating a **spatial anomaly**

### Example Scenario

If a card is used:

* In Toronto
* Then again in Vancouver
* Within 10–30 minutes

…the system flags the second transaction as a **spatial anomaly**, indicating a high likelihood of fraud.

This logic demonstrates **feature engineering grounded in domain knowledge**, not just generic modeling.

---

##  SQL Analytics: Fraud Hotspots

Once enriched, the dataset is queried using **Spark SQL** to uncover geographic fraud patterns.

### Example Insights Produced

* Cities with the **highest number of fraud transactions**
* Cities with the **highest fraud rate** (percentage-based)
* Contribution of each city to **overall fraud volume**

These analyses help identify:

* Fraud concentration areas
* Emerging hotspots
* Locations that warrant closer monitoring

Such SQL-driven insight generation is critical in enterprise banking analytics.

---

##  Outputs Generated

The pipeline produces:

* A cleansed, enriched Spark DataFrame
* Geo-spatial anomaly flags per transaction
* Aggregated fraud statistics by city
* SQL-queryable views for dashboards or reporting

These outputs are suitable for:

* Analyst review
* Rule-based fraud systems
* Feature inputs into ML models

---

##  Technology Stack

* **Python** – Data generation, Spark logic
* **Azure Blob Storage** – Cloud data lake
* **Databricks / Apache Spark** – Distributed processing
* **SQL (Spark SQL)** – Aggregation & analytics
* **Geo-spatial math (Haversine)** – Feature engineering
* **Azure CLI & SDK** – Cloud automation

The stack mirrors real-world banking analytics environments.



##  Results & Interpretation

Using synthetic data, the project demonstrates that:

* Fraud tends to cluster geographically
* Certain cities may contribute disproportionately to fraud volume
* Distance-based features are effective at flagging extreme anomalies

While the data is simulated, the **logic and insights reflect real banking fraud patterns**.



##  Limitations

This is a **prototype**, not a production system:

* Uses synthetic data
* Relies on rule-based spatial thresholds
* Does not include ML model training
* Does not handle real-time streaming

These limitations are intentional and clearly documented.

---

##  Future Enhancements

Possible extensions include:

* Real-time fraud detection using Spark Streaming
* Machine learning models using engineered spatial features
* Integration with alerting systems
* Advanced geospatial clustering
* Secure credential handling using Azure Key Vault

---

##  Why This Project Matters

This project demonstrates:

* Cloud-native data handling
* Scalable big-data processing
* Strong SQL proficiency
* Domain-aware feature engineering
* End-to-end project ownership
* Clear communication and documentation

It reflects the type of analytical thinking and technical execution expected in modern banking data teams.

