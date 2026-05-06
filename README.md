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
### 1. Extract
- Loads an Excel workbook containing multiple sheets
- Dynamically reads all sheet names
- Skips non-data sheets (e.g. cover pages, notes)

### 2. Transform
- Dropping empty or unnamed columns
- Standardising column names (lowercase, trimmed, consistent spacing)
- Fuzzy renaming of inconsistent column headers
- Handling invalid values (e.g. [u], [z])
- Adding a source_sheet column for tracability

### 3. Load
- Outputs cleaned data as CSV files
- Filenames include original sheet name (cleaned) and processing data
- Saved into the /output directory (Azure DevOps) or as an artifatct using GitHub Actions

## Automation (CI/CD)
### GitHub Actions Pipeline
The ETL Process is fully automated using GitHub Actions:
#### Triggers:
- Push to main branch
- Daily scheduled run (8 AM)
- Manual Trigger
#### Pipeline Steps:
1. Checkout repository
2. Set up Python environment
3. Install depdendencies
4. Run ETL script
5. Upload cleaned CSV outputs as artifacts
This ensures the pipeline runs consistently to produce reproducible outputs.

### Error Handling & Robustness
Graceful handling of:
  - Missing or non-numeric sheets
  - Empty datasets and columns
  - Invalid numeric values
- Logs progress and errors to console output
- Ensures pipeline does not fail entirely due to a single bad sheet

### Future Improvements
The following are planned next steps:
1. Build a reporting dashboard using cleaned outputs (e.g. Power BI, Tableau)
2. Add data validation checks (e.g. schema enforcement)
3. Improve logging (e.g. structured logs instead of print statements)
4. Add unit tests for transformation logic
5. Store outputs in a database instead of flat files

### Data Flow Architecture 
- [Insert Mural Diagram Here]

### Key Skills Demonstrated
- Data cleansing and transformation with Pandas
- Handling messy, real-world datasets
- Writing maintainable ETL scripts
- CI/CD pipeline setup and automation
- Basic data engineering concepts (data lineage, reproducability) 
  



