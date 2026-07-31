from connectors.csv_connector import CSVConnector
from rules.null_rule import NullRule
from schema.schema_validator import SchemaValidator


def test_project():

    connector = CSVConnector()

    assert connector is not None

    validator = SchemaValidator()

    expected = ["Name", "Age", "City"]

    actual = ["Name", "Age", "City"]

    assert validator.validate(actual, expected) is True

    rule = NullRule()

    assert rule is not None
