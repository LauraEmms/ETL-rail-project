# ETL Pipeline for Rail Performance Data

## Overview
This project implements an end-to-end ETL (Extract, Transform, Load) pipeline built in Python to process UK rail performance data. The pipeline automates data ingestion, cleaning and transformation across multiple datasets and utilises CI/CD automation to produce structured outputs, ready for analysis. The final output is visualised through an interactive Streamlit dashboard for exploratory analysis of railway performance metrics by route and region.

### Data Source
The data source contains public sector information licensed under the Open Government Licence v3.0 from the Office of Rail and Road:
https://dataportal.orr.gov.uk/performance

## Tech Stack
- Python (pandas, numpy)
- Excel (multi-sheet datasets)
- GitHub Actions (CI/CD automation)
- Azure DevOps Pipeline
- _Planned_ Power BI (for visualisation)

## ETL Process
### 1. Extract
- Loads an Excel workbook containing multiple sheets
- Dynamically reads all sheet names
- Excludes non-data sheets (e.g. notes, cover pages)

### 2. Transform
- Removes empty or irrelevant columns
- Standardises column names (lowercase, trimmed, consistent formatting)
- Handles inconsistent values (e.g. “[u]”, “[z]”)
- Adds a `source_sheet` column to preserve traceability across datasets

### 3. Load
- Outputs cleaned data as CSV files
- File naming includes:
  -  Cleaned sheet name
  -  Processing date
- Saves outputs locally and as CI/CD artifacts

### Data Flow Architecture
This diagram shows the end-to-end data pipeline from raw Excel data through transformation and automation to final outputs.

![Data Flow](docs/etl_diagram.png)

## Automation (CI/CD)
#### GitHub Actions Pipeline
The ETL Process is fully automated using GitHub Actions and runs:
- On every push to the `main` branch
- On a daily schedule (08:00 AM)
- Manually via workflow dispatch
  
#### Pipeline Steps:
1. Checkout repository
2. Set up Python environment
3. Install dependencies
4. Run ETL script
5. Upload cleaned CSV outputs as artifacts

This ensures consistent and reproducible data processing.

### Error Handling & Robustness
To ensure robustness, the pipeline:
  - Handles missing or non-numeric sheets gracefully
  - Skips empty datasets without failing the pipeline
  - Prints errors and processing steps to console
  - Ensures failure in one sheet does not interrupt full execution

### Pipeline Workflow 

![ETL Pipeline](docs/etl_pipeline.png)


### Streamlit Dashboard
![Dashboard](docs/dashboard_1.png)
![Dashboard](docs/dashboard_2.png)

### Future Improvements
Planned next steps include:
- Add schema validation for input data
- Replace print-based logging with structured logging
- Introduce unit tests for transformation logic
- Deploy dashboard on Streamlit Cloud

### Key Skills Demonstrated
- ETL pipeline design and implementation
- Data cleaning and transformation using pandas
- Working with real-world and inconsistent multi-sheet datasets
- CI/CD automation using GitHub Actions and Azure DevOps
- Basic data engineering workflow design
- Interactive dashboard development with Streamline using Python
  



