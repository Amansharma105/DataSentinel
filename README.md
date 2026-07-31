# DataSentinel

DataSentinel is a Python-based Data Quality and Pipeline Monitoring Platform that helps validate datasets, detect anomalies, monitor data quality, generate reports, and automate monitoring tasks through a Command Line Interface (CLI).

---

## Features

- Command Line Interface using Typer
- CSV Data Connector
- JSON Data Connector
- Data Validation Rules
- Null Value Detection
- Duplicate Data Detection
- Schema Validation
- Column Validation
- Outlier Detection
- Anomaly Summary
- HTML Report Generation
- Report Saving
- Jinja2 Template Rendering
- Email Notification System
- Console Notifications
- Task Scheduling using APScheduler
- Automated Testing using Pytest
- Configuration Management

---

## Project Structure

```text
DataSentinel/
│
├── config/
│   ├── .gitkeep
│   └── settings.py
│
├── connectors/
│   ├── .gitkeep
│   ├── csv_connector.py
│   └── json_connector.py
│
├── rules/
│   ├── .gitkeep
│   ├── null_rule.py
│   └── duplicate_rule.py
│
├── schema/
│   ├── .gitkeep
│   ├── schema_validator.py
│   └── column_checker.py
│
├── anomaly/
│   ├── .gitkeep
│   ├── outlier_detector.py
│   └── anomaly_summary.py
│
├── reports/
│   ├── .gitkeep
│   ├── report_generator.py
│   └── report_saver.py
│
├── templates/
│   ├── .gitkeep
│   ├── base.html
│   └── report.html
│
├── alerts/
│   ├── .gitkeep
│   ├── email_alert.py
│   └── notification.py
│
├── scheduler/
│   ├── .gitkeep
│   ├── jobs.py
│   └── task_scheduler.py
│
├── tests/
│   ├── .gitkeep
│   ├── test_main.py
│   ├── test_scheduler.py
│   └── test_project.py
│
├── data/
│   ├── sample.csv
│   └── sample.json
│
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## Technologies Used

- Python
- Typer
- Pandas
- NumPy
- Great Expectations
- SQLAlchemy
- Jinja2
- Plotly
- APScheduler
- Pytest
- YAML

---

## Requirements

- Python 3.10 or above
- Git
- pip

---

## Project Workflow

1. Load CSV or JSON datasets.
2. Validate dataset schema.
3. Detect null and duplicate values.
4. Identify outliers and anomalies.
5. Generate HTML reports.
6. Send notifications and email alerts.
7. Schedule automated monitoring tasks.
8. Execute automated test cases.

---

## Future Improvements

- Dashboard for monitoring
- PDF report generation
- Excel export support
- Database integration
- REST API support
- Cloud deployment

## Author

### Aman Sharma
