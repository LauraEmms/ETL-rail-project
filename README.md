# ETL Pipeline for Rail Performance Data (Multi-Sheet Excel)

## Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python to process Excel data spread across multiple sheets.
The goals of this project are to:
- Clean and standardise inconsistent data
- Automate processing using CI/CD pipelines (using both GitHub Actions and Azure DevOps)
- Prepare structured outputs for analytics and dashboards

### Data Source
Contains public sector information licensed under the Open Government Licence v3.0 from the Office of Rail and Road:
https://dataportal.orr.gov.uk/statistics/performance/passenger-rail-performance/

## Tech Stack
- Python (pandas, numpy)
- Excel (multi-sheet raw dataset)
- GitHub Actions (CI/CD automation)
- Azure DevOps Pipeline
- _Planned_ Power BI / dashboarding tool to visualise cleaned outputs

## ETL Process
### 1. Extract
- Loads an Excel workbook containing multiple sheets
- Dynamically reads all sheet names
- Skips non-data sheets (e.g. cover pages, notes)

### 2. Transform
- Dropping empty or unnamed columns
- Standardising column names (lowercase, trimmed, consistent spacing)
- Fuzzy renaming of inconsistent column headers
- Handling invalid values (e.g. "[u]", "[z]")
- Adding a `source_sheet` column for tracability for reporting dashboards

### 3. Load
- Outputs cleaned data as CSV files
- Filenames include:
  -  Original sheet name (cleaned)
  -  Processing date
- Saved to:
  - `/output` directory (Azure DevOps) or,
  - Uploaded as artifatcts via GitHub Actions

### Data Flow Architecture
This diagram shows the end-to-end data pipeline from raw Excel data through transformation and automation to final outputs.

![Data Flow](docs/etl_diagram.png)

## Automation (CI/CD)
### GitHub Actions Pipeline
The ETL Process is fully automated using GitHub Actions. The pipeline runs daily and successfully generates CSV outputs, which are stored as downloadable artifacts in each run.

#### Triggers:
- Push to main branch
- Daily scheduled run (8:00 AM)
- Manual Trigger
  
#### Pipeline Steps:
1. Checkout repository
2. Set up Python environment
3. Install depdendencies
4. Run ETL script
5. Upload cleaned CSV outputs as artifacts
   
This ensures consistent, repeatable data processing.

### Error Handling & Robustness
The pipeline includes graceful handling of:
  - Missing or non-numeric sheets
  - Empty datasets and columns
  - Invalid numeric values
- Logging of progress and errors to console output
- Isolation of failures (one bad sheet does not stop the full pipeline)

### Pipeline Workflow 
This image shows how the ETL script is executed automatically through GitHub Actions.

![ETL Pipeline](docs/etl_pipeline.png)

### Future Improvements
Planned next steps include:
1. Build a reporting dashboard using cleaned outputs (Power BI / Tableau)
2. Add data validation checks (e.g. schema enforcement)
3. Improve logging (structured logs instead of print statements)
4. Unit tests for transformation logic
5. Store outputs in a database instead of flat files

### Key Skills Demonstrated
- Data cleansing and transformation with pandas
- Handling messy, real-world datasets
- Writing maintainable ETL pipelines
- CI/CD pipeline setup and automation
- Basic data engineering concepts 
  



