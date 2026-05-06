# ETL Pipeline for Cleansing Multi-Sheet Excel Data for Rail Performance
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python to process Excel data spread across multiple sheets.
The goal is to:
- Clean and standardise inconsistent data
- Automate processing using CI/CD pipelines (using both GitHub Actions and Azure DevOps)
- Prepare structured outputs for analytics/dashboards

Contains public sector information licensed under the Open Government Licence v3.0 from the Office of Rail and Road:
https://dataportal.orr.gov.uk/statistics/performance/passenger-rail-performance/

## Tech Stack
- Python (pandas, numpy)
- Excel (multi-sheet raw dataset)
- GitHub Actions (CI/CD automation)
- Azure DevOps Pipelines (additional pipeline setup)
- _Planned_ Power BI / dashboarding tool to visualise cleaned outputs

## ETL Process
1. Extract
- Loads an Excel workbook containing multiple sheets
- Dynamically reads all sheet names
- Skips non-data sheets (e.g. cover pages, notes)

2. Transform
- Dropping empty or unnamed columns
- Standardising column names (lowercase, trimmed, consistent spacing)
- Fuzzy renaming of inconsistent column headers
- Handling invalid values (e.g. [u], [z])
- Adding a source_sheet column for tracability

3. Load
- Outputs cleaned data as CSV files
- Filenames include original sheet name (cleaned) and processing data
- Saved into the /output directory (Azure DevOps) or as an artifatct using GitHub Actions

