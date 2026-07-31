import typer

from connectors.csv_connector import CSVConnector
from connectors.json_connector import JSONConnector

from rules.null_rule import NullRule
from rules.duplicate_rule import DuplicateRule

from schema.schema_validator import SchemaValidator

from anomaly.outlier_detector import OutlierDetector

from reports.report_generator import ReportGenerator

app = typer.Typer()


@app.command()
def start():
    print("DataSentinel Started Successfully")


@app.command()
def load_csv(file_path: str):

    connector = CSVConnector()

    data = connector.load(file_path)

    print(data.head())


@app.command()
def load_json(file_path: str):

    connector = JSONConnector()

    data = connector.load(file_path)

    print(data.head())


@app.command()
def check_nulls(file_path: str):

    connector = CSVConnector()

    data = connector.load(file_path)

    rule = NullRule()

    print(rule.validate(data))


@app.command()
def check_duplicates(file_path: str):

    connector = CSVConnector()

    data = connector.load(file_path)

    rule = DuplicateRule()

    print(rule.validate(data))


@app.command()
def validate_schema(file_path: str):

    connector = CSVConnector()

    data = connector.load(file_path)

    validator = SchemaValidator()

    expected_columns = [
        "Name",
        "Age",
        "City"
    ]

    result = validator.validate(data, expected_columns)

    print(result)


@app.command()
def detect_outliers(file_path: str):

    connector = CSVConnector()

    data = connector.load(file_path)

    detector = OutlierDetector()

    result = detector.detect(data, "Age")

    print(result)


@app.command()
def generate_report():

    report = ReportGenerator()

    html = report.generate("Data Validation Completed Successfully")

    print(html)


if __name__ == "__main__":
    app()
