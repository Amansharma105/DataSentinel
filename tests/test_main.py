from schema.schema_validator import SchemaValidator


def test_schema():

    validator = SchemaValidator()

    actual = ["Name", "Age", "City"]

    expected = ["Name", "Age", "City"]

    assert validator.validate(actual, expected) is True
