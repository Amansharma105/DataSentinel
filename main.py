import typer

from connectors.csv_connector import CSVConnector
from connectors.json_connector import JSONConnector

from rules.null_rule import NullRule
from rules.duplicate_rule import DuplicateRule

from schema.schema_validator import SchemaValidator
from anomaly.outlier_detector import OutlierDetector

from reports.report_generator import ReportGenerator
from alerts.notification import Notification
from alerts.email_alert import EmailAlert

from scheduler.task_scheduler import TaskScheduler
from scheduler.jobs import monitor, generate_report

from config.settings import DATABASE_NAME, REPORT_FOLDER

app = typer.Typer(help="DataSentinel CLI")


@app.command()
def start():
    print("DataSentinel Started Successfully")
    print("Database:", DATABASE_NAME)
    print("Reports Folder:", REPORT_FOLDER)


@app.command()
def load_csv(file_path: str):
    data = CSVConnector().load(file_path)
    print(data.head())


@app.command()
def load_json(file_path: str):
    data = JSONConnector().load(file_path)
    print(data.head())


@app.command()
def check_nulls(file_path: str):
    data = CSVConnector().load(file_path)
    print(NullRule().validate(data))


@app.command()
def check_duplicates(file_path: str):
    data = CSVConnector().load(file_path)
    print(DuplicateRule().validate(data))


@app.command()
def validate_schema(file_path: str):
    data = CSVConnector().load(file_path)
    expected = ["Name", "Age", "City"]
    print(SchemaValidator().validate(data, expected))


@app.command()
def detect_outliers(file_path: str):
    data = CSVConnector().load(file_path)
    print(OutlierDetector().detect(data, "Age"))


@app.command()
def report():
    generator = ReportGenerator()
    print(generator.generate("Data Validation Completed Successfully"))


@app.command()
def notify():
    Notification().show("Pipeline Completed Successfully")


@app.command()
def email():
    EmailAlert().send(
        "sender@example.com",
        "receiver@example.com",
        "Pipeline Completed Successfully"
    )


@app.command()
def schedule():
    scheduler = TaskScheduler()
    scheduler.start()
    monitor()
    generate_report()


if __name__ == "__main__":
    app()
