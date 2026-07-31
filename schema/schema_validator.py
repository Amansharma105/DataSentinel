class SchemaValidator:

    def validate(self, dataframe, expected_columns):

        actual_columns = list(dataframe.columns)

        return actual_columns == expected_columns
